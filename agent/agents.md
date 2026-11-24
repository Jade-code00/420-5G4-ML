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
