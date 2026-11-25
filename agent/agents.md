# Projet : Système de Gestion de Bibliothèque avec CustomTkinter

## Description

Le projet actuel est un système de gestion de bibliothèque développé en C++ avec une interface console.

L'objectif de la partie 3 est de remplacer l'interface console par une interface graphique Python utilisant CustomTkinter tout en réutilisant la logique métier C++ grâce à pybind11.

## État actuel

- Partie 1 terminée
- Partie 2 terminée
- Application console fonctionnelle
- Ollama configuré
- Continue configuré
- Analyse du projet C++ réalisée

## Classes principales

### Book

Représente un livre.

- titre
- auteur
- ISBN
- disponibilité
- emprunteur

### User

Représente un utilisateur.

- nom
- identifiant
- liste des livres empruntés

### Library

Classe principale du système.
Responsable de la gestion :

- des livres
- des utilisateurs
- des emprunts
- des statistiques

### FileManager

Gère :

- la sauvegarde des données
- le chargement des données

## Fonctionnalités existantes

- Ajouter un livre
- Supprimer un livre
- Rechercher un livre
- Afficher les livres
- Afficher les livres disponibles
- Ajouter un utilisateur
- Afficher les utilisateurs
- Emprunter un livre
- Retourner un livre
- Afficher les statistiques
- Sauvegarder les données

## Dépendances

- Library utilise Book
- Library utilise User
- Library utilise FileManager
- FileManager assure la persistance des données

## Objectif de la partie 3

Créer une interface graphique avec CustomTkinter permettant d'accéder à toutes les fonctionnalités actuellement disponibles dans l'interface console.

La communication entre Python et C++ sera réalisée avec pybind11.

## Plan de réalisation

1. Créer les maquettes de l'interface
2. Installer CustomTkinter
3. Concevoir la fenêtre principale
4. Configurer pybind11
5. Exposer les classes C++ à Python
6. Relier les écrans GUI aux fonctionnalités C++
7. Effectuer les tests
8. Finaliser la documentation

## Maquettes GUI

Voici le design proposé pour chaque écran :

### Écran 1: Accueil / Menu Principal

- **Nom**: Accueil
- **Boutons**:
  - "Gérer les livres"
  - "Gérer les utilisateurs"
  - "Effectuer des emprunts"
  - "Afficher les statistiques"
  - "Quitter"
- **Champs**: Aucun
- **Affichage**:
  - Logo de la bibliothèque
  - Titre "Système de Gestion de Bibliothèque"
  - Menu principal
- **Actions**: Navigation vers les autres écrans

### Écran 2: Gestion des Livres

- **Nom**: Gestion des Livres
- **Boutons**:
  - "Ajouter un livre"
  - "Supprimer un livre"
  - "Rechercher un livre"
  - "Afficher tous les livres"
  - "Retour à l'accueil"
- **Champs** (pour les actions):
  - "Ajouter" : champs pour titre, auteur, ISBN
  - "Supprimer" : champ pour ISBN
  - "Rechercher" : champs pour titre, auteur ou ISBN
- **Affichage**:
  - Liste des livres avec ISBN, titre, auteur
  - Statut de disponibilité
  - Emprunteur si indisponible

### Écran 3: Détails d'un livre

- **Nom**: Détails du livre
- **Boutons**:
  - "Emprunter" (si disponible)
  - "Retour"
- **Champs**: Aucun
- **Affichage**:
  - ISBN
  - Titre
  - Auteur complet
  - Année de publication
  - Genre
  - Rayon
  - Disponibilité
  - Emprunteur si indisponible

### Écran 4: Gestion des Utilisateurs

- **Nom**: Gestion des Utilisateurs
- **Boutons**:
  - "Ajouter un utilisateur"
  - "Afficher tous les utilisateurs"
  - "Retour à l'accueil"
- **Champs** (pour les actions):
  - "Ajouter" : champs pour nom, identifiant
- **Affichage**:
  - Liste des utilisateurs avec nom et identifiant

### Écran 5: Détails d'un utilisateur

- **Nom**: Détails de l'utilisateur
- **Boutons**:
  - "Effectuer un emprunt"
  - "Retour"
- **Champs**: Aucun
- **Affichage**:
  - Nom complet
  - Identifiant unique
  - Liste des livres empruntés
  - Date d'emprunt
  - Date prévue de retour

### Écran 6: Gestion des Emprunts

- **Nom**: Gestion des Emprunts
- **Boutons**:
  - "Emprunter un livre"
  - "Retourner un livre"
  - "Afficher l'historique"
  - "Retour à l'accueil"
- **Champs**:
  - "Emprunter" : champ pour ISBN du livre, identifiant du membre
  - "Retourner" : champ pour ISBN du livre

### Écran 7: Statistiques

- **Nom**: Statistiques
- **Boutons**:
  - "Retour à l'accueil"
- **Champs**: Aucun
- **Affichage**:
  - Graphiques :
    - Taux d'utilisation des livres
    - Nombre d'utilisateurs actifs
    - Statistiques d'emprunts par période
  - Tableaux :
    - Répartition par catégorie
    - Liste des livres les plus populaires

### Écran 8: Confirmation

- **Nom**: Messages
- **Boutons**:
  - "OK"
- **Champs**: Aucun
- **Affichage**:
  - Messages de confirmation ("Livre ajouté avec succès")
  - Messages d'erreur ("ISBN déjà utilisé")

## Avancement Phase 1

✅ Analyse du projet C++
✅ Identification des classes principales
✅ Création du fichier agents.md
✅ Conception des maquettes GUI
✅ Définition de l'architecture Python

## Architecture retenue

- main.py
- gui/
- core/
- assets/
- tests/

## Checklist

- [x] Analyse du projet C++
- [ ] Création des maquettes GUI
- [ ] Installation de CustomTkinter
- [ ] Configuration de pybind11
- [ ] Développement de la fenêtre principale
- [ ] Développement des écrans secondaires
- [ ] Intégration C++ / Python
- [ ] Tests
- [ ] Remise finale

## Dernière mise à jour

24/11/2026

Analyse complète du projet C++ réalisée.
Préparation de la phase de conception GUI.
