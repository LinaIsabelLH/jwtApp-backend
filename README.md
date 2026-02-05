# TP Sécuriser son Application Web - Backend Django

## Description
API RESTful Django pour gérer l'authentification et l'autorisation avec JWT.  
Permet de tester différents niveaux d'accès (`FREE`, `PREMIUM`, `UNLIMITED`) et endpoints sécurisés.

---

## Stack
- Python 3.11+
- Django 5.2
- Django REST Framework
- Simple JWT

---

## Installation

1. **Cloner le projet**
```bash
git clone https://github.com/LinaIsabelLH/jwtApp-backend
cd config
```

2. **Créer et activer l'environnement virtuel**

```bash
python3 -m venv env
source env/bin/activate   # macOS / Linux
env\Scripts\activate      # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations**

```bash
python manage.py migrate
```

5. **Lancer le serveur**
```bash
python manage.py runserver
```

Serveur disponible sur : http://127.0.0.1:8000/

---

## Endpoints principaux

- POST /api/auth/token/ → Connexion (retourne access et refresh JWT)
- POST /api/auth/token/refresh/ → Rafraîchir l’access token
- GET /api/me/ → Profil utilisateur (tous les users)
- GET /api/admin/panel/ → Réservé aux is_staff=True
- GET /api/premium-data/ → Réservé aux utilisateurs PREMIUM ou UNLIMITED
