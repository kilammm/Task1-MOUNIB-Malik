# 📬 Task 2 — Local Office Communication System

---

## 🇬🇧 ENGLISH

### 📝 Description
This project sets up a complete local office communication system including a local email server, user accounts, shared folders with role-based access, and a shared printer over the local network.

---

### 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| hMailServer | Local mail server |
| Thunderbird | Email client |
| Windows Shared Folders | File sharing |
| PDFCreator | Virtual shared printer |

---

### 📧 Email System

#### Mail Server — hMailServer
- Domain: `local.office`
- Protocol: IMAP (port 143) / SMTP (port 25)
- Max attachment size: 10 MB

#### User Accounts

| Name | Email |
|------|-------|
| Admin | admin@local.office |
| Alice | alice@local.office |
| Bob | bob@local.office |
| Charlie | charlie@local.office |
| Diana | diana@local.office |

#### Aliases & Forwarders

| Alias | Redirects To |
|-------|-------------|
| contact@local.office | admin@local.office |
| team@local.office | alice@local.office |

---

### 📁 File Sharing

#### Shared Folders

| Folder | Network Path | Access |
|--------|-------------|--------|
| Public | \\KILAM\Public | Everyone |
| Team | \\KILAM\Team | Team members |
| Management | \\KILAM\Management | Admin only |

#### Role-Based Access

| User | Public | Team | Management |
|------|--------|------|------------|
| admin | ✅ Read/Write | ✅ Read/Write | ✅ Full Control |
| alice | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| bob | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| charlie | ✅ Read/Write | ✅ Read/Write | ❌ No Access |
| diana | ✅ Read/Write | ✅ Read/Write | ❌ No Access |

---

### 🖨️ Shared Printer

| Setting | Value |
|---------|-------|
| Printer | PDFCreator |
| Share Name | OfficePrinter |
| Network Path | \\KILAM\OfficePrinter |

---

### 📖 User Manuals

| Manual | Description |
|--------|-------------|
| [manual_email.md](manual_email.md) | How to use the local email system |
| [manual_sharing.md](manual_sharing.md) | How to access shared folders and printer |

---

### 📸 Screenshots

All configuration screenshots are available in the `screenshots/` folder:
- hMailServer accounts and aliases
- Thunderbird email accounts and test messages
- Shared folders (`net share` output)
- Shared printer configuration

---

---

## 🇫🇷 FRANÇAIS

### 📝 Description
Ce projet met en place un système de communication local complet incluant un serveur mail local, des comptes utilisateurs, des dossiers partagés avec accès basé sur les rôles, et une imprimante partagée sur le réseau local.

---

### 🛠️ Outils Utilisés

| Outil | Rôle |
|-------|------|
| hMailServer | Serveur mail local |
| Thunderbird | Client mail |
| Dossiers partagés Windows | Partage de fichiers |
| PDFCreator | Imprimante virtuelle partagée |

---

### 📧 Système Email

#### Serveur Mail — hMailServer
- Domaine : `local.office`
- Protocole : IMAP (port 143) / SMTP (port 25)
- Taille max des pièces jointes : 10 Mo

#### Comptes Utilisateurs

| Nom | Email |
|-----|-------|
| Admin | admin@local.office |
| Alice | alice@local.office |
| Bob | bob@local.office |
| Charlie | charlie@local.office |
| Diana | diana@local.office |

#### Aliases & Redirections

| Alias | Redirige vers |
|-------|--------------|
| contact@local.office | admin@local.office |
| team@local.office | alice@local.office |

---

### 📁 Partage de Fichiers

#### Dossiers Partagés

| Dossier | Chemin réseau | Accès |
|---------|--------------|-------|
| Public | \\KILAM\Public | Tout le monde |
| Team | \\KILAM\Team | Membres de l'équipe |
| Management | \\KILAM\Management | Admin uniquement |

#### Accès par Rôle

| Utilisateur | Public | Team | Management |
|-------------|--------|------|------------|
| admin | ✅ Lecture/Écriture | ✅ Lecture/Écriture | ✅ Contrôle total |
| alice | ✅ Lecture/Écriture | ✅ Lecture/Écriture | ❌ Pas d'accès |
| bob | ✅ Lecture/Écriture | ✅ Lecture/Écriture | ❌ Pas d'accès |
| charlie | ✅ Lecture/Écriture | ✅ Lecture/Écriture | ❌ Pas d'accès |
| diana | ✅ Lecture/Écriture | ✅ Lecture/Écriture | ❌ Pas d'accès |

---

### 🖨️ Imprimante Partagée

| Paramètre | Valeur |
|-----------|--------|
| Imprimante | PDFCreator |
| Nom de partage | OfficePrinter |
| Chemin réseau | \\KILAM\OfficePrinter |

---

### 📖 Manuels Utilisateur

| Manuel | Description |
|--------|-------------|
| [manual_email.md](manual_email.md) | Comment utiliser le système email local |
| [manual_sharing.md](manual_sharing.md) | Comment accéder aux dossiers et à l'imprimante |

---

### 📸 Screenshots

Tous les screenshots de configuration sont disponibles dans le dossier `screenshots/` :
- Comptes et aliases hMailServer
- Comptes Thunderbird et emails de test
- Dossiers partagés (résultat de `net share`)
- Configuration de l'imprimante partagée
