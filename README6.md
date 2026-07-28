# 🔒 Task 6 — System Hardening and Access Control

---

## 🇬🇧 ENGLISH

### 📝 Description
This project implements system hardening on a Windows machine including user management, folder permissions, firewall configuration, audit logging, and automated security scripts.

---

### 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| PowerShell | Automation and configuration |
| Windows Firewall | Network security |
| Windows Audit Policy | Security logging |
| NTFS Permissions | File access control |

---

### 👥 User Management

| Username | Role | Privileges |
|----------|------|------------|
| malik | Admin | Full control |
| dev_user | Developer | Administrator group |
| guest_user | Guest | Limited access |

**Commands used:**
```powershell
New-LocalUser -Name "guest_user" -Password (ConvertTo-SecureString "Guest123!" -AsPlainText -Force)
New-LocalUser -Name "dev_user" -Password (ConvertTo-SecureString "Dev123!" -AsPlainText -Force)
Add-LocalGroupMember -Group "Administrateurs" -Member "dev_user"
```

---

### 📁 Folder Permissions (NTFS)

| Folder | User | Permission |
|--------|------|------------|
| C:\SecureFolders\Admin | malik | Full Control |
| C:\SecureFolders\Dev | dev_user | Modify |
| C:\SecureFolders\Guest | guest_user | Read & Execute |

---

### 🔥 Firewall Rules

| Rule | Port | Action |
|------|------|--------|
| Block FTP | 21 | Block Inbound |
| Block Telnet | 23 | Block Inbound |
| Allow Flask API | 5000 | Allow Inbound |

**Commands used:**
```powershell
New-NetFirewallRule -DisplayName "Block FTP" -Direction Inbound -Protocol TCP -LocalPort 21 -Action Block
New-NetFirewallRule -DisplayName "Block Telnet" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block
New-NetFirewallRule -DisplayName "Allow Flask API" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
```

---

### 🚫 Disabled Services

| Service | Reason |
|---------|--------|
| Telnet | Insecure protocol, sends data in plain text |
| FTP | Insecure protocol, no encryption |

---

### 📋 Audit Logging

| Category | Status |
|----------|--------|
| Logon/Logoff | Success & Failure |
| File System | Success & Failure |
| Policy Change | Success |

---

### 🤖 Automated Script

Run the full security hardening in one command:
```powershell
powershell -ExecutionPolicy Bypass -File scripts\security_hardening.ps1
```

The script automatically:
1. Creates local users with proper roles
2. Creates secure folders
3. Configures firewall rules
4. Enables audit logging
5. Disables unused services

---

### 💡 Security Recommendations

| Recommendation | Priority |
|----------------|----------|
| Use strong passwords (12+ chars) | 🔴 High |
| Enable Windows Defender | 🔴 High |
| Keep Windows updated | 🔴 High |
| Disable unused accounts | 🟡 Medium |
| Enable BitLocker encryption | 🟡 Medium |
| Regular security audits | 🟢 Low |

---

### 📸 Screenshots

All screenshots available in `screenshots/` folder:
- Local users list
- Firewall rules
- Audit policy configuration
- Secure folders permissions
- Security hardening script output

---
---

## 🇫🇷 FRANÇAIS

### 📝 Description
Ce projet implémente le durcissement d'un système Windows incluant la gestion des utilisateurs, les permissions de dossiers, la configuration du pare-feu, les logs d'audit et des scripts de sécurité automatisés.

---

### 🛠️ Outils Utilisés

| Outil | Rôle |
|-------|------|
| PowerShell | Automatisation et configuration |
| Pare-feu Windows | Sécurité réseau |
| Politique d'audit Windows | Journalisation de sécurité |
| Permissions NTFS | Contrôle d'accès aux fichiers |

---

### 👥 Gestion des Utilisateurs

| Utilisateur | Rôle | Privilèges |
|-------------|------|------------|
| malik | Admin | Contrôle total |
| dev_user | Développeur | Groupe Administrateurs |
| guest_user | Invité | Accès limité |

---

### 📁 Permissions des Dossiers (NTFS)

| Dossier | Utilisateur | Permission |
|---------|-------------|------------|
| C:\SecureFolders\Admin | malik | Contrôle total |
| C:\SecureFolders\Dev | dev_user | Modification |
| C:\SecureFolders\Guest | guest_user | Lecture et exécution |

---

### 🔥 Règles Pare-feu

| Règle | Port | Action |
|-------|------|--------|
| Block FTP | 21 | Bloquer entrant |
| Block Telnet | 23 | Bloquer entrant |
| Allow Flask API | 5000 | Autoriser entrant |

---

### 🚫 Services Désactivés

| Service | Raison |
|---------|--------|
| Telnet | Protocole non sécurisé, données en clair |
| FTP | Protocole non sécurisé, pas de chiffrement |

---

### 📋 Journalisation d'Audit

| Catégorie | Statut |
|-----------|--------|
| Ouverture/Fermeture de session | Succès et échec |
| Système de fichiers | Succès et échec |
| Changement de stratégie | Succès |

---

### 🤖 Script Automatisé

Lance tout le durcissement en une seule commande :
```powershell
powershell -ExecutionPolicy Bypass -File scripts\security_hardening.ps1
```

Le script applique automatiquement :
1. Création des utilisateurs locaux avec les bons rôles
2. Création des dossiers sécurisés
3. Configuration des règles pare-feu
4. Activation des logs d'audit
5. Désactivation des services inutilisés

---

### 💡 Recommandations de Sécurité

| Recommandation | Priorité |
|----------------|----------|
| Utiliser des mots de passe forts (12+ caractères) | 🔴 Haute |
| Activer Windows Defender | 🔴 Haute |
| Maintenir Windows à jour | 🔴 Haute |
| Désactiver les comptes inutilisés | 🟡 Moyenne |
| Activer le chiffrement BitLocker | 🟡 Moyenne |
| Audits de sécurité réguliers | 🟢 Basse |

---

### 📸 Screenshots

Tous les screenshots sont disponibles dans le dossier `screenshots/` :
- Liste des utilisateurs locaux
- Règles pare-feu
- Configuration de la politique d'audit
- Permissions des dossiers sécurisés
- Résultat du script de durcissement