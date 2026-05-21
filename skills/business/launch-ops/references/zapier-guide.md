# Zapier Automation Guide

## Critical Automation: Purchase -> Skool Access

This is the most important automation. When a customer purchases, they automatically get added to the Skool group.

### Setup Steps

1. **Trigger:** New sale/payment on your payment platform
   - Gumroad: "New Sale" trigger
   - Stripe: "New Payment" trigger
   - Stan Store: "New Sale" trigger

2. **Action:** Add member to Skool group
   - Use Skool's Zapier integration
   - Map customer email from trigger to Skool invite

3. **Test:** Run a test purchase to verify the automation fires correctly

## Additional Automations

### Purchase -> Tag in Email Platform
- **Trigger:** New sale on payment platform
- **Action:** Add tag "Customer" to subscriber in email platform (ConvertKit/Beehiiv/Mailchimp)
- **Why:** Exclude customers from sales sequences, send them customer-only content

### Purchase -> Remove from Objection Sequence
- **Trigger:** New sale on payment platform
- **Action:** Remove subscriber from "Clickers" segment/sequence
- **Why:** Stop sending objection-handling emails to people who already bought

### EEC Complete -> Newsletter Segment
- **Trigger:** Subscriber completes Day 5 of EEC (email platform automation rule)
- **Action:** Move subscriber to "Weekly Newsletter" segment
- **Why:** Transition from EEC to ongoing nurture

## Testing Checklist

- [ ] Test purchase triggers the Skool invite
- [ ] Test purchase tags subscriber as "Customer"
- [ ] Test purchase removes from Clickers segment
- [ ] Test EEC completion transitions to newsletter
- [ ] Verify no duplicate emails sent
- [ ] Verify timing (automations fire within minutes, not hours)
