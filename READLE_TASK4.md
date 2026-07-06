# 🔐 Task 4 — Secure Local API Configuration

---

## 🇬🇧 ENGLISH

### 📝 Description
This project implements a secure REST API using Flask (Python) with JWT authentication, role-based access control, HTTPS with self-signed certificates, and a logging dashboard.

---

### 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Flask | REST API framework |
| Flask-JWT-Extended | JWT token authentication |
| Cryptography | Self-signed HTTPS certificates |
| Postman | API testing |

---

### ⚙️ Installation

Install dependencies:
```
pip install flask flask-jwt-extended cryptography
```

Generate self-signed certificates:
```
cd scripts
python -c "from cryptography import x509; ..."
```

---

### 🚀 How to Run

```
python scripts/app.py
```

The API will be available at: **https://127.0.0.1:5000**

---

### 👥 Users & Roles

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | admin |
| alice | alice123 | user |
| bob | bob123 | user |

---

### 📡 API Endpoints

#### 🔓 Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /api/login | Get JWT token | ❌ |

**Request body:**
```json
{
    "username": "admin",
    "password": "admin123"
}
```

**Response:**
```json
{
    "role": "admin",
    "token": "eyJhbGci..."
}
```

---

#### 📱 Devices (CRUD)
| Method | Endpoint | Description | Role Required |
|--------|----------|-------------|---------------|
| GET | /api/devices | List all devices | user / admin |
| GET | /api/devices/:id | Get one device | user / admin |
| POST | /api/devices | Create a device | admin only |
| PUT | /api/devices/:id | Update a device | admin only |
| DELETE | /api/devices/:id | Delete a device | admin only |

**Using the token in Postman:**
- Go to **Authorization** tab
- Select **Bearer Token**
- Paste your JWT token

---

#### 📊 Logs Dashboard
| Method | Endpoint | Description | Role Required |
|--------|----------|-------------|---------------|
| GET | /api/logs | View all logs | admin only |

---

### 🔐 Security Features

| Feature | Implementation |
|---------|---------------|
| Authentication | JWT tokens (1 hour expiry) |
| Authorization | Role-based (admin/user) |
| HTTPS | Self-signed certificate (cert.pem / key.pem) |
| Logging | All requests logged with IP, timestamp, user, status |

---

### 🧪 Test Results

| Test | Expected | Result |
|------|----------|--------|
| POST /api/login (admin) | 200 OK + token | ✅ |
| GET /api/devices (with token) | 200 OK + list | ✅ |
| POST /api/devices (admin token) | 201 CREATED | ✅ |
| POST /api/devices (user token) | 403 FORBIDDEN | ✅ |
| GET /api/logs (admin token) | 200 OK + logs | ✅ |
| HTTPS connection | SSL active | ✅ |

---

### 📸 Screenshots

All screenshots are available in the `screenshots/` folder:
- Login request with JWT token response
- GET /api/devices with Bearer Token
- POST /api/devices (201 Created - admin)
- POST /api/devices (403 Forbidden - user)
- GET /api/logs dashboard
- HTTPS connection in Postman

---
---

## 🇫🇷 FRANÇAIS

### 📝 Description
Ce projet implémente une API REST sécurisée avec Flask (Python), authentification JWT, contrôle d'accès par rôles, HTTPS avec certificat auto-signé et un dashboard de logs.

---

### 🛠️ Outils Utilisés

| Outil | Rôle |
|-------|------|
| Flask | Framework API REST |
| Flask-JWT-Extended | Authentification par token JWT |
| Cryptography | Certificats HTTPS auto-signés |
| Postman | Tests de l'API |

---

### ⚙️ Installation

Installe les dépendances :
```
pip install flask flask-jwt-extended cryptography
```

---

### 🚀 Lancement

```
python scripts/app.py
```

L'API sera disponible sur : **https://127.0.0.1:5000**

---

### 👥 Utilisateurs & Rôles

| Utilisateur | Mot de passe | Rôle |
|-------------|-------------|------|
| admin | admin123 | admin |
| alice | alice123 | user |
| bob | bob123 | user |

---

### 📡 Endpoints de l'API

#### 🔓 Authentification
| Méthode | Endpoint | Description | Auth requise |
|---------|----------|-------------|--------------|
| POST | /api/login | Obtenir un token JWT | ❌ |

**Corps de la requête :**
```json
{
    "username": "admin",
    "password": "admin123"
}
```

**Réponse :**
```json
{
    "role": "admin",
    "token": "eyJhbGci..."
}
```

---

#### 📱 Devices (CRUD)
| Méthode | Endpoint | Description | Rôle requis |
|---------|----------|-------------|-------------|
| GET | /api/devices | Lister tous les devices | user / admin |
| GET | /api/devices/:id | Obtenir un device | user / admin |
| POST | /api/devices | Créer un device | admin only |
| PUT | /api/devices/:id | Modifier un device | admin only |
| DELETE | /api/devices/:id | Supprimer un device | admin only |

---

#### 📊 Dashboard des Logs
| Méthode | Endpoint | Description | Rôle requis |
|---------|----------|-------------|-------------|
| GET | /api/logs | Voir tous les logs | admin only |

---

### 🔐 Fonctionnalités de Sécurité

| Fonctionnalité | Implémentation |
|----------------|----------------|
| Authentification | Tokens JWT (expiration 1 heure) |
| Autorisation | Basée sur les rôles (admin/user) |
| HTTPS | Certificat auto-signé (cert.pem / key.pem) |
| Logging | Toutes les requêtes loguées avec IP, timestamp, user, status |

---

### 🧪 Résultats des Tests

| Test | Attendu | Résultat |
|------|---------|----------|
| POST /api/login (admin) | 200 OK + token | ✅ |
| GET /api/devices (avec token) | 200 OK + liste | ✅ |
| POST /api/devices (token admin) | 201 CREATED | ✅ |
| POST /api/devices (token user) | 403 FORBIDDEN | ✅ |
| GET /api/logs (token admin) | 200 OK + logs | ✅ |
| Connexion HTTPS | SSL actif | ✅ |

---

### 📸 Screenshots

Tous les screenshots sont disponibles dans le dossier `screenshots/` :
- Requête login avec réponse token JWT
- GET /api/devices avec Bearer Token
- POST /api/devices (201 Created - admin)
- POST /api/devices (403 Forbidden - user)
- Dashboard GET /api/logs
- Connexion HTTPS dans Postman