# Firebase Deploy Troubleshooting

Real issues encountered in production deployments with detailed solutions.

## 1. Firebase CI Token Expiration

**Symptom:** `firebase deploy` fails with "not logged in" or "token expired" after ~1 hour.

**Root cause:** `firebase login:ci` tokens are short-lived (~1 hour).

**Fix (temporary):**
```bash
firebase login:ci
# Paste new token
FIREBASE_TOKEN=<new-token> firebase deploy
```

**Fix (permanent):** Use a GCP service account:
1. Go to GCP Console → IAM & Admin → Service Accounts
2. Create service account with roles: `Firebase Admin`, `Cloud Functions Admin`
3. Create and download JSON key
4. Set env: `export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json`
5. Deploy without token: `firebase deploy`

---

## 2. Cloud Build Permission Denied

**Symptom:** `firebase deploy --only functions` fails with permission errors during build.

**Root cause:** Compute service account lacks Cloud Build permissions.

**Fix:** In GCP Console → IAM, find `{PROJECT_NUMBER}-compute@developer.gserviceaccount.com` and add these roles:
- `Cloud Build Service Account`
- `Artifact Registry Writer`
- `Storage Object Viewer`

These are needed for the first deploy. Cloud Build uses the compute service account to build and push container images for Cloud Functions v2.

---

## 3. Cloud Function Not Publicly Accessible

**Symptom:** Cloud Function returns 403 Forbidden when called from external webhook.

**Root cause:** Organization policies may block adding `allUsers` as Cloud Run invoker via API/CLI.

**Fix (when API blocked):**
1. Go to GCP Console → Cloud Run
2. Click on the function's service
3. Click "Permissions" tab
4. Click "Add Principal"
5. Principal: `allUsers`, Role: `Cloud Run Invoker`
6. If blocked, look for "Allow public access" toggle in the service settings

**Alternative:** If org policy is strict, use API Gateway or set up a service account for the webhook caller.

---

## 4. Firestore Permission Denied (Cloud Function)

**Symptom:** Cloud Function gets `PERMISSION_DENIED` when reading/writing Firestore.

**Root cause:** The Cloud Functions service account doesn't have Firestore access.

**Fix:** Add `Cloud Datastore User` role to `{PROJECT_NUMBER}-compute@developer.gserviceaccount.com` in IAM.

Note: `firebase-admin` SDK in Cloud Functions uses the default service account, not Application Default Credentials.

---

## 5. Firestore Test Mode Expiration

**Symptom:** All Firestore reads/writes suddenly fail after ~30 days.

**Root cause:** Default test mode rules have a timestamp expiration:
```
allow read, write: if request.time < timestamp.date(2025, 4, 25);
```

**Fix:** Replace with proper security rules:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{email} {
      allow read, write: if request.auth != null && request.auth.token.email == email;
    }
  }
}
```

Deploy: `firebase deploy --only firestore:rules`

---

## 6. Functions Deploy "No Matching Engine"

**Symptom:** `firebase deploy --only functions` fails with engine compatibility error.

**Fix:** Ensure `functions/package.json` has:
```json
{
  "engines": { "node": "20" }
}
```

Node 18 is deprecated for Cloud Functions. Use Node 20.

---

## 7. Git Push Rejected After Deploy

**Symptom:** `git push` fails because remote has newer commits (someone else deployed/committed).

**Fix:**
```bash
git stash                  # save local changes
git pull --rebase          # get remote changes
git stash pop              # re-apply local changes
git push                   # push
```

Never force-push to main. Rebase is the safe approach.

---

## 8. PostHog Session Recording Not Working

**Symptom:** PostHog shows events but no session replays.

**Possible causes:**
- Free tier limit (5K sessions/month) exceeded
- `session_recording` not enabled in init:
```typescript
posthog.init("phc_KEY", {
  api_host: "https://us.i.posthog.com",
  session_recording: { recordCrossOriginIframes: true }  // must be present
});
```
- Ad blockers blocking `us.i.posthog.com`

---

## 9. Firebase Analytics Not Showing Data

**Symptom:** Events sent but not visible in Firebase Console.

**Root cause:** Firebase Analytics has a 24-48 hour delay for some reports. DebugView shows real-time.

**Fix for dev:**
- Use DebugView in Firebase Console
- Or install Firebase Analytics Debugger browser extension
- Events appear in real-time in DebugView, but standard reports take hours

---

## 10. Vite Build Fails with Firebase Imports

**Symptom:** Build errors related to Firebase module resolution.

**Fix:** Ensure Firebase is installed as a regular dependency (not devDependency):
```bash
npm install firebase
```

For functions:
```bash
cd functions && npm install firebase-admin firebase-functions
```

Don't mix Firebase Web SDK (`firebase`) with Admin SDK (`firebase-admin`) in client code. Web SDK is for the browser, Admin SDK is for Cloud Functions/server.

---

## 11. xRDP Keyboard Layout Reset

**Symptom:** After reconnecting to xRDP, keyboard layout reverts to English.

**Fix:** Edit `/etc/xrdp/reconnectwm.sh` and add your layout setup command:
```bash
setxkbmap -layout us,ua -option grp:alt_shift_toggle
```

This ensures layout survives reconnections.

---

## 12. Beehiiv Webhook Test Data

**Symptom:** Cloud Function crashes on Beehiiv test webhook with "unknown bundle" error.

**Root cause:** Beehiiv test webhooks send fake data (e.g., tier "Silver", "Gold") that doesn't match your real bundle IDs.

**Fix:** Don't throw errors on unknown bundle IDs. Return a warning instead:
```javascript
if (!VALID_BUNDLES.includes(bundleId) && bundleId !== "all-access") {
  res.status(200).json({ warning: `Unknown bundle: ${bundleId}`, processed: false });
  return;
}
```

This way test webhooks don't trigger error alerts.

---

## 13. CORS Issues with Cloud Functions

**Symptom:** Browser requests to Cloud Function blocked by CORS.

**Fix:** Cloud Functions v2 with `onRequest` handle CORS automatically for simple requests. For complex requests (custom headers), add:
```javascript
exports.myFunction = onRequest({ region: "us-central1", cors: true }, async (req, res) => {
  // ...
});
```

Or handle manually:
```javascript
res.set("Access-Control-Allow-Origin", "*");
if (req.method === "OPTIONS") {
  res.set("Access-Control-Allow-Methods", "POST");
  res.set("Access-Control-Allow-Headers", "Content-Type, X-Bundle-Id");
  res.status(204).send("");
  return;
}
```

---

## 14. Firebase Hosting Cache

**Symptom:** Old version still showing after deploy.

**Fix:**
- Hard refresh: Ctrl+Shift+R
- Firebase Hosting serves with `Cache-Control: no-cache` by default for `index.html`
- Static assets (JS/CSS with hash in filename) are cached aggressively, which is correct
- If issue persists, check if a CDN or Cloudflare is in front of Firebase Hosting
