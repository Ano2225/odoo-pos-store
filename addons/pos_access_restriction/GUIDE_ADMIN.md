# Guide d'administration — POS Access Restriction
**Module Odoo 18 · Version 2.0**

---

## Sommaire
1. [Ce que fait le module](#1-ce-que-fait-le-module)
2. [Prérequis](#2-prérequis)
3. [Installation](#3-installation)
4. [Configurer un caissier](#4-configurer-un-caissier)
5. [Configurer un administrateur POS](#5-configurer-un-administrateur-pos)
6. [Assigner les caisses](#6-assigner-les-caisses)
7. [Comportement selon le rôle](#7-comportement-selon-le-rôle)
8. [Désinstallation](#8-désinstallation)
9. [Questions fréquentes](#9-questions-fréquentes)

---

## 1. Ce que fait le module

| Fonctionnalité | Détail |
|---|---|
| **Restriction des caisses** | Chaque caissier ne voit que les caisses qui lui sont assignées |
| **Restriction des commandes** | Un caissier ne voit que les commandes de ses caisses |
| **Menus cachés** | Les sous-menus POS (Reporting, Configuration…) sont cachés aux caissiers |
| **Applications cachées** | Les apps Employés, Comptabilité, Ventes, etc. sont invisibles pour les caissiers |
| **Accueil automatique** | Un caissier atterrit directement sur Point de Vente à la connexion |
| **Blocage à l'ouverture** | Un caissier ne peut pas ouvrir une session sur une caisse non autorisée |
| **Admins POS non affectés** | Les administrateurs POS voient toujours tout, sans aucune restriction |

---

## 2. Prérequis

- Odoo 18 avec le module **Point de Vente** installé
- Accès administrateur Odoo pour installer le module et configurer les utilisateurs

---

## 3. Installation

### Via l'interface Odoo
```
Paramètres → Applications → rechercher "POS Access Restriction" → Installer
```

### Via Docker (ligne de commande)
```bash
# Copier le module dans le dossier addons
cp -r pos_access_restriction/ ./addons/

# Redémarrer le conteneur
docker compose restart odoo

# Mettre à jour la liste des modules dans Odoo
# Paramètres → Applications → Mettre à jour la liste des applications
```

### Ce qui se passe automatiquement à l'installation
- Le menu **Restrictions d'accès** est créé sous Point de Vente
- Les sous-menus POS (Reporting, Commandes, etc.) sont restreints aux administrateurs POS
- Les applications non-POS sont cachées aux caissiers
- Les caissiers déjà existants reçoivent Point de Vente comme page d'accueil

---

## 4. Configurer un caissier

### Étape 1 — Ouvrir la fiche utilisateur
```
Paramètres → Utilisateurs et sociétés → Utilisateurs → [cliquer sur l'utilisateur]
```

### Étape 2 — Définir le rôle POS
Dans l'onglet **Droits d'accès** :

| Section | Valeur à mettre |
|---|---|
| Droits de base | **Tous les employés** ← obligatoire |
| Point de Vente | **Utilisateur** |
| Tout le reste | laisser vide |

> ⚠️ "Tous les employés" est obligatoire. Sans ce droit, l'utilisateur ne peut pas se connecter à Odoo.

### Étape 3 — Assigner les caisses
Dans l'onglet **Caisses POS autorisées** (apparaît après l'onglet Droits d'accès) :

- Cliquer dans le champ et sélectionner les caisses autorisées
- **Laisser vide** = l'utilisateur voit toutes les caisses (aucune restriction)
- **Remplir** = l'utilisateur voit uniquement les caisses sélectionnées

### Étape 4 — Sauvegarder
Cliquer sur **Sauvegarder**. Les restrictions sont actives immédiatement.

---

## 5. Configurer un administrateur POS

> En Odoo 18, le rôle "supérieur" dans Point de Vente s'appelle **Administrateur**
> (et non "Manager"). C'est ce rôle qui donne un accès complet sans restriction.

### Étape 1 — Ouvrir la fiche utilisateur
```
Paramètres → Utilisateurs et sociétés → Utilisateurs → [cliquer sur l'utilisateur]
```

### Étape 2 — Définir le rôle POS
Dans l'onglet **Droits d'accès** :

| Section | Valeur à mettre |
|---|---|
| Droits de base | **Tous les employés** |
| Point de Vente | **Administrateur** |

### Résultat
- Voit **toutes** les caisses sans exception
- Voit tous les sous-menus POS (Reporting, Configuration, Commandes…)
- A accès au menu **Restrictions d'accès** pour gérer les caissiers
- Le champ "Caisses POS autorisées" sur sa fiche n'a **aucun effet**

> L'administrateur Odoo global (`base.group_system`) n'est jamais restreint non plus.

---

## 6. Assigner les caisses

Il existe **trois endroits équivalents**. Toutes les modifications sont synchronisées automatiquement.

### Option A — Depuis la fiche utilisateur
```
Paramètres → Utilisateurs → [utilisateur] → onglet "Caisses POS autorisées"
```
Utile pour configurer un utilisateur à la fois.

### Option B — Depuis la fiche caisse
```
Point de Vente → Configuration → Caisses → [caisse] → onglet "Caissiers autorisés"
```
Utile pour voir et gérer tous les caissiers d'une caisse donnée.

### Option C — Vue dédiée (assignation en masse)
```
Point de Vente → Restrictions d'accès
```
Affiche un tableau avec toutes les caisses et leurs caissiers. Éditable directement ligne par ligne.

---

## 7. Comportement selon le rôle

### Caissier (Point de Vente = **Utilisateur**)

| Élément | Avec caisses assignées | Sans caisses assignées |
|---|---|---|
| Page d'accueil | Point de Vente | Point de Vente |
| Tableau de bord POS | Ses caisses uniquement | Toutes les caisses |
| Reporting, Configuration, Commandes | ❌ Cachés | ❌ Cachés |
| Employés, Comptabilité, Ventes… | ❌ Invisibles | ❌ Invisibles |
| Ouvrir une caisse non autorisée | ❌ Erreur bloquante | — |

### Administrateur POS (Point de Vente = **Administrateur**)

| Élément | Comportement |
|---|---|
| Page d'accueil | Normale (pas de redirection forcée) |
| Tableau de bord POS | Toutes les caisses |
| Sous-menus POS | Tous visibles |
| Menu Restrictions d'accès | Visible et accessible |
| Autres applications | Selon droits avancés configurés séparément |

### Administrateur Odoo global
Aucune restriction. Bypasse toutes les règles du module.

---

## 8. Désinstallation

```
Paramètres → Applications → POS Access Restriction → Désinstaller
```

### Ce qui est restauré automatiquement
- Le menu "Restrictions d'accès" est supprimé
- Les sous-menus POS redeviennent accessibles aux caissiers
- Les menus d'applications (Employés, etc.) redeviennent visibles pour tous
- La page d'accueil POS est retirée des utilisateurs concernés

---

## 9. Questions fréquentes

**Q : Un caissier voit encore toutes les caisses après la configuration.**
→ Vérifier que l'onglet "Caisses POS autorisées" n'est pas vide. Vide = aucune restriction.

**Q : Le caissier ne voit aucune caisse.**
→ Impossible par conception (vide = voit tout). Vérifier que le module est installé et que l'utilisateur a bien le rôle "Utilisateur" en Point de Vente.

**Q : L'administrateur POS ne voit pas le menu Reporting.**
→ Vérifier que l'utilisateur a bien **Administrateur** (et non Utilisateur) dans la section Point de Vente des Droits d'accès.

**Q : Le caissier voit encore l'application "Employés".**
→ Le module cache uniquement les apps dont les modules sont installés. Si elle reste visible, la cacher manuellement via `Paramètres → Technique → Interface utilisateur → Menus`.

**Q : Peut-on avoir un administrateur POS restreint à certaines caisses ?**
→ Non. Le rôle Administrateur donne accès à tout par conception. Pour restreindre à certaines caisses, utiliser le rôle **Utilisateur**.

**Q : Les restrictions s'appliquent-elles à l'API et à l'application mobile ?**
→ Oui. Les règles d'accès (`ir.rule`) s'appliquent à toutes les interfaces : web, mobile, API REST.

---

*Module développé pour Odoo 18 Community/Enterprise.*
*En cas de problème : `docker logs odoo18_pos --tail 100`*
