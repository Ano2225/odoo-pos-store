 # odoo-pos-store

Odoo 18 dockerisé avec Point of Sale (POS) et base de données persistante.

---

# Démarrage du projet

```bash
docker compose up -d
```

C’est tout.

Le projet est déjà initialisé avec des volumes Docker persistants.

---

# Accès

Odoo : [http://localhost:8069](http://localhost:8069)

---

# Architecture

* Odoo 18 (container officiel)
* PostgreSQL 16 (volume persistant)
* Modules custom : `./addons`
* Données Odoo : volume Docker (`odoo_postgres_data`)
* Filestore : `./data`

---

# Persistance des données

Ce projet utilise des volumes Docker :

* `odoo_postgres_data` → base de données PostgreSQL
* `./data` → fichiers Odoo (attachments, filestore)
* `./addons` → modules personnalisés

Les données restent intactes après redémarrage.

---

# IMPORTANT

* Ne pas supprimer les volumes Docker
* Ne pas utiliser `docker compose down -v`
* Ne pas recréer la base de données (déjà existante)

---

# Commandes utiles

## Redémarrer le projet

```bash
docker compose restart
```

---

## Voir les logs

```bash
docker logs -f odoo18_pos
```

---

## Arrêter le projet

```bash
docker compose down
```

---

# Ajout de modules custom

Ajouter un module dans :

```bash
./addons/
```

Puis redémarrer :

```bash
docker compose restart
```

---

# Déploiement VPS (Hostinger / Ubuntu)

```bash
git clone <repo>
cd odoo-pos-store
docker compose up -d
```

Accès :

http://IP_DU_SERVEUR:8069

---

# Note importante

Ce projet est déjà initialisé.
Le simple lancement Docker suffit pour le faire fonctionner.

---

# Résumé

Clone → `docker compose up -d` → ça tourne.
