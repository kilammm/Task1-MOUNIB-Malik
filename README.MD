# 📊 Task 1 — Local Data Analysis of System Logs

---

## 🇬🇧 ENGLISH

### 📝 Description
This project performs a complete workflow of system log analysis, including log retrieval, data extraction, processing, visualization, and automation.

---

### 📁 Project Structure

```
log-analysis/
├── scripts/
│   ├── main.py                  # Main menu to run all scripts
│   ├── generate_logs.py         # Generate fake logs (for testing)
│   ├── get_windows_logs.py      # Retrieve real Windows logs
│   ├── analyse_windows.py       # Windows log analysis + HTML report
│   └── analyse_linux.py         # Linux log analysis + HTML report
├── Logs/
│   └── system.log               # Log file (not tracked by git)
├── data/
│   ├── chart_errors.png         # Error frequency bar chart
│   ├── chart_logins.png         # Activity time series
│   └── chart_distribution.png  # Log level pie chart
├── output/
│   └── rapport_YYYY-MM-DD_HH-MM.html  # Generated reports
├── .gitignore
└── README.md
```

---

### ⚙️ Requirements

Install dependencies with:
```
pip install pandas matplotlib faker pywin32 schedule
```

---

### 🚀 How to Run

Launch the main menu from the `scripts/` folder:
```
cd scripts
python main.py
```

### Menu Options
| Option | Description |
|--------|-------------|
| [1] | Retrieve Windows logs |
| [2] | Run Windows analysis (once) |
| [3] | Run Windows analysis (automatic) |
| [4] | Run Linux analysis (once) |
| [5] | Run Linux analysis (automatic) |
| [6] | Open latest report |
| [7] | List all reports |
| [8] | Open a specific report |
| [9] | Generate fake logs (test) |
| [10] | Clear old reports |

---

### 📊 Visualizations

Three charts are generated automatically:
- **Bar chart** — error frequency by source (System / Application / Security)
- **Time series** — activity by hour and source
- **Pie chart** — log level distribution (INFO / WARNING / ERROR / CRITICAL)

---

### 🖥️ Windows vs 🐧 Linux

| Feature | Windows | Linux |
|--------|---------|-------|
| Log source | Event Viewer (System, Application, Security) | /var/log/syslog, /var/log/auth.log |
| Script | `analyse_windows.py` | `analyse_linux.py` |
| Permissions | Run as Administrator | Run with sudo |

---

### 🔄 Automation
The analysis runs automatically every **2 minutes**, retrieving fresh logs and regenerating charts and reports each time.

---
---

## 🇫🇷 FRANÇAIS

### 📝 Description
Ce projet réalise un workflow complet d'analyse de logs système, incluant la récupération des logs, l'extraction des données, le traitement, la visualisation et l'automatisation.

---

### 📁 Structure du projet

```
log-analysis/
├── scripts/
│   ├── main.py                  # Menu principal pour lancer tous les scripts
│   ├── generate_logs.py         # Génère de faux logs (pour les tests)
│   ├── get_windows_logs.py      # Récupère les vrais logs Windows
│   ├── analyse_windows.py       # Analyse des logs Windows + rapport HTML
│   └── analyse_linux.py         # Analyse des logs Linux + rapport HTML
├── Logs/
│   └── system.log               # Fichier de logs (non suivi par git)
├── data/
│   ├── chart_errors.png         # Graphique en barres des erreurs
│   ├── chart_logins.png         # Série temporelle de l'activité
│   └── chart_distribution.png  # Camembert des niveaux de logs
├── output/
│   └── rapport_YYYY-MM-DD_HH-MM.html  # Rapports générés
├── .gitignore
└── README.md
```

---

### ⚙️ Dépendances

Installe les bibliothèques avec :
```
pip install pandas matplotlib faker pywin32 schedule
```

---

### 🚀 Lancement

Lance le menu principal depuis le dossier `scripts/` :
```
cd scripts
python main.py
```

### Options du menu
| Option | Description |
|--------|-------------|
| [1] | Récupérer les logs Windows |
| [2] | Lancer l'analyse Windows (une fois) |
| [3] | Lancer l'analyse Windows (automatique) |
| [4] | Lancer l'analyse Linux (une fois) |
| [5] | Lancer l'analyse Linux (automatique) |
| [6] | Ouvrir le dernier rapport |
| [7] | Lister tous les rapports |
| [8] | Ouvrir un rapport spécifique |
| [9] | Générer de faux logs (test) |
| [10] | Supprimer les anciens rapports |

---

### 📊 Visualisations

Trois graphiques sont générés automatiquement :
- **Graphique en barres** — fréquence des erreurs par source (System / Application / Security)
- **Série temporelle** — activité par heure et par source
- **Camembert** — distribution des niveaux de logs (INFO / WARNING / ERROR / CRITICAL)

---

### 🖥️ Windows vs 🐧 Linux

| Fonctionnalité | Windows | Linux |
|----------------|---------|-------|
| Source des logs | Event Viewer (System, Application, Security) | /var/log/syslog, /var/log/auth.log |
| Script | `analyse_windows.py` | `analyse_linux.py` |
| Permissions | Lancer en tant qu'Administrateur | Lancer avec sudo |

---

### 🔄 Automatisation
L'analyse se relance automatiquement toutes les **2 minutes**, récupère les nouveaux logs et régénère les graphiques et rapports à chaque fois.