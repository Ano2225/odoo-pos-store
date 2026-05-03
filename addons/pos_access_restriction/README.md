# POS Access Restriction — Odoo 18 (v2)

## Approche

Configuration côté **utilisateur** (inspirée de Cybrosys Technologies) :
- On assigne les caisses autorisées **sur chaque utilisateur**
- La règle d'accès utilise `user.allowed_pos.ids` — natif Odoo, très fiable
- La vue hérite de `base.view_users_form` — stable dans toutes les versions

## Tableau des droits

| Fonctionnalité | Caissier | Manager | Admin |
|---|---|---|---|
| Voir ses caisses assignées | ✅ | ✅ | ✅ |
| Voir toutes les caisses | ❌ | ✅ | ✅ |
| Voir ses commandes uniquement | ✅ | ✅ | ✅ |
| Menu Commandes/Produits/Config/Reporting | ❌ | ✅ | ✅ |

## Installation Docker

```bash
# Supprimer l'ancienne version
docker exec -it odoo18_pos rm -rf /mnt/extra-addons/pos_access_restriction

# Extraire la nouvelle
tar -xzf pos_access_restriction.tar.gz -C ./addons/

# Redémarrer
docker compose restart odoo
```

Puis : Applications → Mettre à jour la liste → Installer **POS Access Restriction**

## Configuration

1. **Paramètres → Utilisateurs & Sociétés → Utilisateurs**
2. Ouvrir un caissier
3. Onglet **Caisses POS autorisées**
4. Sélectionner les caisses qu'il peut utiliser
5. Sauvegarder

> Champ vide = accès à toutes les caisses (pas de restriction)
