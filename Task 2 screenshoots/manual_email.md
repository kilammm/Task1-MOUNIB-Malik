# 📧 User Manual — Local Email System

## Overview
This manual explains how to use the local email system set up with **hMailServer** and **Thunderbird** on the local network.

---

## 📋 Available Email Accounts

| Name | Email Address |
|------|--------------|
| Admin | admin@local.office |
| Alice | alice@local.office |
| Bob | bob@local.office |
| Charlie | charlie@local.office |
| Diana | diana@local.office |

### Aliases
| Alias | Redirects To |
|-------|-------------|
| contact@local.office | admin@local.office |
| team@local.office | alice@local.office |

---

## 🚀 How to Send an Email

1. Open **Thunderbird**
2. Click **"New Message"** (top left)
3. Fill in the fields:
   - **To** → recipient's email (e.g. alice@local.office)
   - **Subject** → subject of the email
   - **Body** → your message
4. Click **Send**

---

## 📥 How to Receive Emails

1. Open **Thunderbird**
2. Click on your account in the left panel
3. Click **"Inbox"**
4. Your received emails will appear automatically

---

## ⚙️ Account Configuration in Thunderbird

If you need to add your account manually, use these settings:

### Incoming Mail (IMAP)
| Setting | Value |
|---------|-------|
| Server | localhost |
| Port | 143 |
| Security | None |
| Authentication | Normal password |
| Username | your@local.office |

### Outgoing Mail (SMTP)
| Setting | Value |
|---------|-------|
| Server | localhost |
| Port | 25 |
| Security | None |
| Authentication | Normal password |
| Username | your@local.office |

---

## 📎 Attachment Size Limit

The maximum attachment size is **10 MB** (10240 KB).

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| Cannot connect | Check that hMailServer is running |
| Wrong password | Contact the administrator |
| Email not received | Check your Inbox or Spam folder |
| Connection refused | Make sure you are on the local network |

---

## 📞 Contact

For any issues, contact the administrator at: **admin@local.office**
