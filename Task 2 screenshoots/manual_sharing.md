# 📁 User Manual — Shared Resources

## Overview
This manual explains how to access shared folders and the shared printer on the local network.

---

## 📂 Shared Folders

| Folder | Network Path | Access |
|--------|-------------|--------|
| Public | \\KILAM\Public | Everyone |
| Team | \\KILAM\Team | Team members (alice, bob, charlie, diana) |
| Management | \\KILAM\Management | Admin only |

---

## 🔗 How to Access a Shared Folder

### Method 1 — File Explorer
1. Open **File Explorer**
2. In the address bar, type the network path:
   ```
   \\KILAM\Public
   ```
3. Press **Enter**
4. Enter your credentials if prompted

### Method 2 — Map a Network Drive
1. Open **File Explorer**
2. Click **"This PC"** in the left panel
3. Click **"Map network drive"** in the top menu
4. Choose a drive letter (e.g. Z:)
5. Enter the folder path (e.g. `\\KILAM\Public`)
6. Check **"Reconnect at sign-in"**
7. Click **Finish**

---

## 🔐 Role-Based Access

| User | Public | Team | Management |
|------|--------|------|------------|
| admin | ✅ Read/Write | ✅ Read/Write | ✅ Full Control |
| alice | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| bob | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| charlie | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| diana | ✅ Read/Write | ✅ Read/Write | ❌ No Access |

---

## 🖨️ Shared Printer

| Setting | Value |
|---------|-------|
| Printer Name | OfficePrinter |
| Network Path | \\KILAM\OfficePrinter |
| Type | PDFCreator (Virtual Printer) |

### How to Connect to the Shared Printer
1. Open **Settings** → **Bluetooth & devices** → **Printers & scanners**
2. Click **"Add a printer or scanner"**
3. Click **"The printer I want isn't listed"**
4. Select **"Select a shared printer by name"**
5. Enter:
   ```
   \\KILAM\OfficePrinter
   ```
6. Click **Next** and follow the instructions

### How to Print
1. Open any document
2. Press **Ctrl+P**
3. Select **OfficePrinter** from the printer list
4. Click **Print**

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| Cannot access folder | Check you have the right permissions |
| Network path not found | Make sure you are on the local network |
| Printer not found | Check that the host PC is turned on |
| Access denied | Contact the administrator |

---

## 📞 Contact

For any issues, contact the administrator at: **admin@local.office**
