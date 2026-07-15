# ⚖️ Task 5 — High Availability with Load Balancing

---

## 🇬🇧 ENGLISH

### 📝 Description
This project sets up a high availability system using Docker containers with two Nginx web servers and an HAProxy load balancer configured with round-robin traffic distribution.

---

### 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Docker | Container platform |
| Docker Compose | Multi-container orchestration |
| Nginx | Web servers (x2) |
| HAProxy | Load balancer |

---

### 🏗️ Architecture

```
                    ┌─────────────┐
                    │   HAProxy   │
         ┌──────────│ 172.20.0.4  │──────────┐
         │          │  Port 8888  │          │
         │          └─────────────┘          │
         ▼                                   ▼
┌─────────────────┐                ┌─────────────────┐
│    Server 1     │                │    Server 2     │
│   172.20.0.2    │                │   172.20.0.3    │
│   Nginx:alpine  │                │   Nginx:alpine  │
└─────────────────┘                └─────────────────┘
```

---

### 📋 Network Configuration

| Container | IP Address | Port | Role |
|-----------|-----------|------|------|
| server1 | 172.20.0.2 | 80 | Web Server 1 |
| server2 | 172.20.0.3 | 80 | Web Server 2 |
| haproxy | 172.20.0.4 | 8888 | Load Balancer |

**Subnet:** 172.20.0.0/24

---

### 🚀 How to Run

```
cd task5
docker-compose up -d
```

Access the load balancer at: **http://localhost:8888**

Access HAProxy stats at: **http://localhost:9999/stats**

---

### ⚙️ HAProxy Configuration

**Algorithm:** Round-Robin
- Each request is distributed alternately between Server 1 and Server 2
- Health checks enabled on both servers
- Automatic failover if a server goes down

---

### 🧪 Tests

#### Round-Robin Test
Refresh **http://localhost:8888** multiple times:
- Request 1 → Server 1 (blue)
- Request 2 → Server 2 (green)
- Request 3 → Server 1 (blue)
- ...

#### Failure Simulation
```
# Stop Server 1
docker stop server1

# All traffic now goes to Server 2
# Verify at http://localhost:8888 → always Server 2

# Restart Server 1
docker start server1

# Traffic distributed again between both servers
```

---

### ✅ Test Results

| Test | Expected | Result |
|------|----------|--------|
| Round-robin distribution | Alternates between servers | ✅ |
| Server 1 failure | All traffic to Server 2 | ✅ |
| Server 1 recovery | Traffic distributed again | ✅ |
| HAProxy stats page | Accessible at /stats | ✅ |

---

### 💡 Benefits of Load Balancing in Enterprise

| Benefit | Description |
|---------|-------------|
| High Availability | If one server fails, others take over automatically |
| Scalability | Add more servers without downtime |
| Performance | Traffic distributed to avoid overloading one server |
| Zero Downtime | Maintenance possible without interrupting service |
| Fault Tolerance | System continues working even with hardware failures |

---

### 🛑 How to Stop

```
docker-compose down
```

---

### 📸 Screenshots

All screenshots are available in the `screenshots/` folder:
- Server 1 response (blue)
- Server 2 response (green)
- Round-robin alternation
- Failure simulation (Server 1 stopped → Server 2 only)
- HAProxy stats dashboard

---
---

## 🇫🇷 FRANÇAIS

### 📝 Description
Ce projet met en place un système haute disponibilité avec Docker, deux serveurs web Nginx et un load balancer HAProxy configuré en round-robin.

---

### 🛠️ Outils Utilisés

| Outil | Rôle |
|-------|------|
| Docker | Plateforme de containers |
| Docker Compose | Orchestration multi-containers |
| Nginx | Serveurs web (x2) |
| HAProxy | Load balancer |

---

### 🏗️ Architecture

```
                    ┌─────────────┐
                    │   HAProxy   │
         ┌──────────│ 172.20.0.4  │──────────┐
         │          │  Port 8888  │          │
         │          └─────────────┘          │
         ▼                                   ▼
┌─────────────────┐                ┌─────────────────┐
│    Serveur 1    │                │    Serveur 2    │
│   172.20.0.2    │                │   172.20.0.3    │
│   Nginx:alpine  │                │   Nginx:alpine  │
└─────────────────┘                └─────────────────┘
```

---

### 📋 Configuration Réseau

| Container | Adresse IP | Port | Rôle |
|-----------|-----------|------|------|
| server1 | 172.20.0.2 | 80 | Serveur Web 1 |
| server2 | 172.20.0.3 | 80 | Serveur Web 2 |
| haproxy | 172.20.0.4 | 8888 | Load Balancer |

**Sous-réseau :** 172.20.0.0/24

---

### 🚀 Lancement

```
cd task5
docker-compose up -d
```

Accès au load balancer : **http://localhost:8888**

Accès aux stats HAProxy : **http://localhost:9999/stats**

---

### ⚙️ Configuration HAProxy

**Algorithme :** Round-Robin
- Chaque requête est distribuée alternativement entre Server 1 et Server 2
- Health checks activés sur les deux serveurs
- Basculement automatique si un serveur tombe

---

### 🧪 Tests

#### Test Round-Robin
Rafraîchis **http://localhost:8888** plusieurs fois :
- Requête 1 → Serveur 1 (bleu)
- Requête 2 → Serveur 2 (vert)
- Requête 3 → Serveur 1 (bleu)
- ...

#### Simulation de Panne
```
# Arrêter le Serveur 1
docker stop server1

# Tout le trafic va vers le Serveur 2
# Vérifier sur http://localhost:8888 → toujours Serveur 2

# Redémarrer le Serveur 1
docker start server1

# Le trafic est à nouveau distribué entre les deux serveurs
```

---

### ✅ Résultats des Tests

| Test | Attendu | Résultat |
|------|---------|----------|
| Distribution round-robin | Alterne entre les serveurs | ✅ |
| Panne Serveur 1 | Tout le trafic vers Serveur 2 | ✅ |
| Récupération Serveur 1 | Trafic redistribué | ✅ |
| Page stats HAProxy | Accessible sur /stats | ✅ |

---

### 💡 Avantages du Load Balancing en Entreprise

| Avantage | Description |
|----------|-------------|
| Haute Disponibilité | Si un serveur tombe, les autres prennent le relais automatiquement |
| Scalabilité | Ajout de serveurs sans interruption de service |
| Performance | Trafic distribué pour éviter la surcharge d'un serveur |
| Zéro Interruption | Maintenance possible sans couper le service |
| Tolérance aux Pannes | Le système continue même en cas de défaillance matérielle |

---

### 🛑 Arrêt

```
docker-compose down
```

---

### 📸 Screenshots

Tous les screenshots sont disponibles dans le dossier `screenshots/` :
- Réponse Serveur 1 (bleu)
- Réponse Serveur 2 (vert)
- Alternance round-robin
- Simulation de panne (Serveur 1 arrêté → Serveur 2 uniquement)
- Dashboard stats HAProxy
