---
name: firebase-deploy
description: |
  Deploy web apps to Firebase (Hosting, Auth, Firestore, Cloud Functions, Analytics).
  Use when: deploying to Firebase, setting up Firebase project, configuring Firebase Auth,
  writing Cloud Functions, fixing Firebase deploy errors, Firebase IAM permissions,
  Firebase CI tokens, React+Vite+Firebase setup, payment webhooks with Cloud Functions,
  Firestore data model, Firebase Analytics integration, PostHog + Firebase dual tracking.
  Also triggers on: "firebase deploy", "firebase hosting", "cloud function", "firestore rules",
  "firebase auth", "firebase login:ci", "firebase init".
---

# Firebase Deploy Skill

Deploy React/Vite (or any static) apps to Firebase with full stack: Hosting, Auth, Firestore, Cloud Functions v2, Analytics.

Based on real production deployments. Every gotcha here cost real debugging time.

## Quick Start Checklist

```
1. firebase login              # or firebase login:ci for CI tokens
2. firebase init               # select Hosting + Functions + Firestore
3. npm run build               # Vite → dist/
4. firebase deploy             # hosting + functions
```

## Project Setup

### Create Firebase Project
- Use **Blaze plan** (pay-as-you-go) if you need Cloud Functions. Free Spark plan doesn't support Functions.
- **Region matters**: pick based on audience. US audience → `us-central1`. EU → `europe-west1`.
- Firestore region is set once and cannot be changed. For US: `nam5` (multi-region).

### firebase.json (React SPA)
```json
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      { "source": "**", "destination": "/index.html" }
    ]
  },
  "functions": {
    "source": "functions"
  }
}
```

Key points:
- `"public": "dist"` for Vite. CRA uses `"build"`.
- SPA rewrite sends all routes to `index.html` (client-side routing).
- Functions source is a separate directory with its own `package.json`.

### Vite Config (React + TypeScript)
```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({ plugins: [react()] });
```

No special Firebase config needed in Vite. Firebase SDK is a regular npm dependency.

---

## Firebase Auth

### Setup
Enable providers in Firebase Console → Authentication → Sign-in method.

### Google + Email/Password Pattern
```typescript
import { getAuth, signInWithPopup, GoogleAuthProvider,
         signInWithEmailAndPassword, createUserWithEmailAndPassword,
         updateProfile, signOut, onAuthStateChanged } from "firebase/auth";

const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();

// Google Sign-In
async function signInWithGoogle() {
  const result = await signInWithPopup(auth, googleProvider);
  return result.user; // user.email, user.displayName, user.photoURL
}

// Email Sign-In
async function signInWithEmail(email: string, password: string) {
  const result = await signInWithEmailAndPassword(auth, email, password);
  return result.user;
}

// Email Sign-Up
async function signUpWithEmail(email: string, password: string, name: string) {
  const result = await createUserWithEmailAndPassword(auth, email, password);
  if (name) await updateProfile(result.user, { displayName: name });
  return result.user;
}
```

### Common Auth Error Codes
| Code | User-facing message |
|------|-------------------|
| `auth/invalid-credential` | Wrong email or password |
| `auth/email-already-in-use` | This email is already registered |
| `auth/weak-password` | Password must be at least 6 characters |
| `auth/too-many-requests` | Too many attempts. Try again later |

---

## Firestore

### Data Model Pattern (User-centric)
Use email as document ID for easy lookup:
```
users/{email}
  - email: string
  - name: string
  - first_visit: ISO string
  - last_visit: ISO string
  - visits: number
  - unlocked_bundles: string[]   // or any access control array
  - completed_items: string[]
  - user_data: map               // nested user-generated data
  - last_activity: ISO string
```

Why email as doc ID: direct lookup without queries, webhook handlers can write by email without knowing Firebase UID.

### Client-side CRUD
```typescript
import { getFirestore, doc, setDoc, getDoc, updateDoc } from "firebase/firestore";
const db = getFirestore(app);

// Read
const userDoc = await getDoc(doc(db, "users", email));
if (userDoc.exists()) { const data = userDoc.data(); }

// Create
await setDoc(doc(db, "users", email), { email, visits: 1, ... });

// Update (merge)
await updateDoc(doc(db, "users", email), { last_visit: new Date().toISOString() });
```

### Firestore Security Rules
Test mode expires in 30 days. Set proper rules before launch:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{email} {
      allow read: if request.auth != null && request.auth.token.email == email;
      allow write: if request.auth != null && request.auth.token.email == email;
    }
    // Admin access (server-side via Cloud Functions uses admin SDK, bypasses rules)
  }
}
```

---

## Cloud Functions v2

### Basic Webhook Handler
```javascript
// functions/index.js
const { onRequest } = require("firebase-functions/v2/https");
const { initializeApp } = require("firebase-admin/app");
const { getFirestore } = require("firebase-admin/firestore");

initializeApp();
const db = getFirestore();

exports.myWebhook = onRequest({ region: "us-central1" }, async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).send("Method not allowed");
    return;
  }
  try {
    const { email } = req.body;
    // Process...
    res.status(200).json({ success: true });
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});
```

### functions/package.json
```json
{
  "name": "my-functions",
  "version": "1.0.0",
  "main": "index.js",
  "engines": { "node": "20" },
  "dependencies": {
    "firebase-admin": "^13.7.0",
    "firebase-functions": "^7.2.2"
  }
}
```

Always `cd functions && npm install` before deploying functions.

### Deploy Functions Separately
```bash
firebase deploy --only functions    # just functions
firebase deploy --only hosting      # just hosting
firebase deploy                     # everything
```

---

## Analytics (Firebase + PostHog Dual Tracking)

### Pattern: Single `track()` Function
```typescript
import { getAnalytics, logEvent } from "firebase/analytics";
import posthog from "posthog-js";

const analytics = getAnalytics(app);

// Init PostHog
posthog.init("phc_YOUR_KEY", {
  api_host: "https://us.i.posthog.com",
  autocapture: true,
  capture_pageview: true,
  session_recording: { recordCrossOriginIframes: true }
});

// Dual track
function track(event: string, params?: Record<string, any>) {
  try { logEvent(analytics, event, params); } catch {}
  try { posthog.capture(event, params); } catch {}
}
```

### User Identification (on auth)
```typescript
// After successful login/signup:
setUserId(analytics, user.email);
setUserProperties(analytics, { email: user.email });
posthog.identify(user.email, { email: user.email, name: user.displayName });

// On sign out:
posthog.reset();
```

### Key Events to Track
- `login` (method: google/email), `sign_up`, `logout`
- `tab_switch` (tab name)
- `item_started`, `item_completed`, `item_restarted`
- `step_completed` (item + step index)
- `purchase_clicked`, `unlock_success`, `unlock_failed`
- `new_user` (with UTM params)

PostHog free tier: 1M events/month, 5K sessions/month for replays.

---

## Payment Webhook Pattern (Beehiiv / Stripe / Any)

### Architecture
```
Payment Provider → POST webhook → Cloud Function → Firestore update
```

### Bundle/Product Unlock Pattern
Use a header or body field to identify what was purchased:
```javascript
const bundleId = req.headers["x-bundle-id"] || req.body.product_id;
const email = req.body.subscriber_email || req.body.email;

const ALL_BUNDLES = ["bundle-a", "bundle-b", "bundle-c"];
const toUnlock = bundleId === "all-access" ? ALL_BUNDLES : [bundleId];

const userRef = db.collection("users").doc(email);
const userDoc = await userRef.get();

if (userDoc.exists) {
  const existing = userDoc.data().unlocked_bundles || ["free"];
  const merged = [...new Set([...existing, ...toUnlock])];
  await userRef.update({ unlocked_bundles: merged });
} else {
  await userRef.set({ email, unlocked_bundles: ["free", ...toUnlock] });
}
```

### Client-side Access Check
```typescript
const bundles = await loadUserBundles(email); // returns string[]
const hasAccess = bundles.includes(requiredBundle);
```

---

## Admin Dashboard Pattern

### Admin Check
```typescript
const ADMIN_EMAILS = ["admin@example.com"];
function isAdmin(email: string | null): boolean {
  return !!email && ADMIN_EMAILS.includes(email);
}
```

### Admin Data (client-side, small scale)
For <10K users, reading all docs client-side is fine:
```typescript
const snap = await getDocs(collection(db, "users"));
const users = snap.docs.map(d => ({ id: d.id, ...d.data() }));
```

For larger scale, create a Cloud Function that aggregates stats.

### Conditional Admin Tab
```typescript
const tabs = [
  ["home", "Home"], ["store", "Store"],
  ...(isAdmin(userEmail) ? [["admin", "Admin"]] : [])
];
```

---

## Deployment Workflow

### Authentication Options

**Option 1: CI Token (expires ~1 hour)**
```bash
firebase login:ci
# Copy the token
FIREBASE_TOKEN=your_token firebase deploy
```

**Option 2: Service Account (permanent, recommended)**
1. Create service account in GCP Console → IAM
2. Download JSON key
3. `export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json`
4. `firebase deploy`

**Option 3: Interactive login (dev machine)**
```bash
firebase login   # opens browser
firebase deploy  # uses cached credentials
```

### Full Deploy Sequence
```bash
cd /path/to/project
npm run build                        # Vite build
firebase deploy --only hosting       # deploy frontend
cd functions && npm install && cd .. # ensure function deps
firebase deploy --only functions     # deploy backend
```

---

## Troubleshooting Guide

Read `references/troubleshooting.md` for detailed solutions. Quick reference:

| Problem | Solution |
|---------|----------|
| CI token expired | `firebase login:ci` for new token, or use service account |
| Cloud Function 403 "Permission Denied" | Add `Cloud Datastore User` role to compute service account |
| Cloud Build permission denied | Add `Cloud Build Service Account` + `Artifact Registry Writer` + `Storage Object Viewer` to compute SA |
| Can't make Cloud Function public via API | Organization policy blocks `allUsers`. Set via Cloud Run Console UI manually |
| `firebase deploy` fails with "not logged in" | Run `firebase login` or set `FIREBASE_TOKEN` |
| Firestore "Missing permissions" | Check security rules. Test mode expires in 30 days |
| Functions deploy "no matching engine" | Ensure `"engines": {"node": "20"}` in functions/package.json |
| Git push rejected after deploy | `git pull --rebase` then push (remote may have newer commits) |

---

## File Structure Template

```
project/
├── src/
│   ├── App.tsx           # Main app
│   └── analytics.ts      # Firebase + PostHog init, auth, Firestore helpers
├── functions/
│   ├── index.js          # Cloud Functions
│   └── package.json      # Node 20 + firebase-admin + firebase-functions
├── firebase.json         # Hosting + Functions config
├── .firebaserc           # Project ID
├── firestore.rules       # Security rules
├── vite.config.ts
├── package.json
├── tsconfig.json
└── index.html
```

Keep Firebase config (apiKey, projectId, etc.) in the client code. These are NOT secrets -- they're meant to be public. Security is enforced by Firestore rules and Auth, not by hiding the config.
