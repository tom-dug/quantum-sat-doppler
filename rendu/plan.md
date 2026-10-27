# Plan définitif du projet Artishow

Réunion tous les vendredis matin afin d'expliquer son avancement et ses recherches.
Les dates de rendu peuvent être amménées à être modifiées en fonction des difficultés non prévues rencontrées.

PLANNING PROJET
Simulation orbitale - Effet Doppler - quantique : Février → Juin

Le but du projet est de :
- Développer un simulateur d’effet Doppler relativiste pour un satellite
- Évaluer l’impact de cet effet sur les performances d’un réseau quantique satellite-sol
- Étudier l’impact du décalage fréquentiel sur l’interférence de Hong-Ou-Mandel et l’efficacité d’une mesure de Bell



# 1. Phase 1 – Bases théoriques et architecture logicielle

https://en.wikipedia.org/wiki/Earth-centered,_Earth-fixed_coordinate_system
https://en.wikipedia.org/wiki/Earth-centered_inertial
https://en.wikipedia.org/wiki/Orbital_elements


25 février → 11 mars

Objectifs
- 	Comprendre les systèmes de coordonnées orbitaux
-	Comprendre les paramètres orbitaux et les TLE
-	Se familiariser avec les outils de simulation d’orbites
-	Définir l’architecture du simulateur



1.1 Étude des systèmes de coordonnées
- Système ECI (Earth-Centered Inertial)
- Système ECEF (Earth-Centered Earth-Fixed)
- Transformations ECI <-> ECEF
- Position d’une station sol en coordonnées terrestres
- Position d’un satellite en orbite

Travail pour réunion :
- Note explicative
- Implémentation test des transformations


1.2 Paramètres orbitaux et propagation
- 6 paramètres képlériens
- Lecture de TLE
- Propagation orbitale
- Calcul position et vitesse

Travail pour réunion :
- Script simple calculant position et vitesse à un instant donné
- Note explicative


1.3 Étude des outils
- Installation d’Orekit (wrapper Python)
- Tests simples
- Comparaison avec autres bibliothèques si nécessaire (Skyfield, SatOptLink)

Travail pour réunion :
- Choix de l’outil principal
- Structure du dépôt Git
- Note explicative


1.4 Architecture du simulateur

Travail pour réunion :
- Squelette du projet
- Documentation interne minimale


==> Objectif de la phase 1 : expliquer à chaque membre du groupe ses recherches, afin d'arriver à une architecture définitive du code

## Répartition phase 1 :
- A : Coordonnées et transformations
- B : Paramètres orbitaux et TLE
- C : Étude des bibliothèques
- D : Architecture logicielle et mise en place du code





# 2. Phase 2 – Simulation orbitale complète (synthèse de la phase 1)

https://gitlab.orekit.org/orekit-labs/python-wrapper
https://www.orekit.org
https://github.com/matteoschiav/SatOptLink
https://rhodesmill.org/skyfield/
https://en.wikipedia.org/wiki/Two-line_element_set

11 mars → 25 mars

Objectifs
- Simuler une orbite complète
- Calculer la position et la vitesse d'un satellite
- Calculer la visibilité depuis une station sol
- Calculer la vitesse radiale satellite–station



Implémentation
- Lecture de TLE
- Propagation sur une orbite complète
- Conversion en coordonnées station
- Calcul : distance satellite–station, angle d’élévation, vitesse radiale



Travail pour réunion (25 mars)
- Simulation orbitale fonctionnelle
- Graphiques : position vs temps, distance vs temps, vitesse radiale vs temps

==> Le but de cette phase est de repgrouper le code écrit par chacun en phase 1 afin d'obtenir le module de calcul d'orbite



# 3. Phase 3 – Simulateur d’effet Doppler

https://en.wikipedia.org/wiki/Relativistic_Doppler_effect
https://en.wikipedia.org/wiki/Doppler_effect
https://www.feynmanlectures.caltech.edu/I_34.html#Ch34-S6


25 mars → 15 avril

Objectifs
- Implémenter l’effet Doppler
- Calculer le décalage fréquentiel reçu au sol
- Étudier l’influence des paramètres orbitaux


Travail théorique
- Formule du Doppler classique
- Formule du Doppler relativiste
- Définition d’une fréquence centrale du photon


Implémentation
- Calcul de la fréquence reçue
- Simulation sur un passage satellite
- Étude paramétrique : altitude, inclinaison, géométrie de passage, vitesse


Travail pour réunion :

8 avril :
- Note explicative de l'effet Doppler
- Note sur les fréquences utilisées pour les communications satellite

15 avril :
- Module Doppler validé

22 avril :
- Simulation complète orbite + Doppler
- Graphique fréquence reçue vs temps
- Comparaison des résultats avec la réalité (tableau fournie phase 1)

## Répartion phase 3 :

Personne 1 – Fondements théoriques Doppler

Responsabilités
	- Étudier l’effet Doppler classique
	- Étudier l’effet Doppler relativiste
	- Comparer les deux régimes

Production attendue (8 avril)
	- Note explicative claire contenant : dérivation du Doppler classique, formule relativiste, discussion sur l’ordre de grandeur des vitesses orbitales, justification du modèle retenu


Personne 2 – Fréquence

Responsabilités :
	- Identifier les longueurs d’onde typiques en communication quantique satellite-sol
	- Définir une fréquence centrale réaliste

Production attendue (8 avril)
	- Note sur les fréquences utilisées en communications satellite
	- Tableau récapitulatif : fréquence centrale, vitesse orbitale typique, décalage attendu (permet la vérification de la cohérence du modèle quand il sera codé)


Personne 3 – Implémentation du module Doppler

Responsabilités
- Implémenter la formule retenue (quand elle sera fournie par la personne 1)
- Prendre en entrée : vitesse radiale, fréquence émise
- Calculer : fréquence reçue, décalage fréquentiel

Production attendue (15 avril)
- Module doppler
- Effectuer des tests unitaires simples
- Vérifier cohérence numérique du module Dopller

Personne 4 – Simulation complète et étude paramétrique

Responsabilités
- Intégrer le module Doppler à la simulation orbitale
- Simuler un passage satellite complet
- Générer : fréquence reçue vs temps, décalage vs temps
- Étudier l’influence de : altitude, inclinaison, géométrie de passage, vitesse

Production attendue (22 avril)
- Simulation complète orbite + Doppler
- Graphiques fréquence reçue vs temps
- Analyse comparative des paramètres



# 4. Phase 4 – Impact sur les communications quantiques

https://arxiv.org/abs/1509.07855
https://arxiv.org/abs/quant-ph/0512023
https://arxiv.org/pdf/2202.01817

29 avril → 13 mai

Objectifs
- Comprendre la distribution d’intrication
- Étudier l’interférence Hong-Ou-Mandel
- Étudier l’efficacité d’une mesure de Bell
- Évaluer l’impact du décalage fréquentiel


Travail théorique
- Distribution d’intrication satellite-sol
- QKD
- Mesure de Bell
- Effet Hong-Ou-Mandel
- Recouvrement spectral de deux photons


Modélisation
- Modèle simplifié de recouvrement spectral
- Influence du décalage fréquentiel
- Calcul de visibilité d’interférence


Travail pour réunion : (13 mai)
- Note théorique structurée
- Modèle numérique simplifié reliant : vitesse radiale, décalage Doppler, perte d’efficacité d’interférence

## Répartition phase 4 (peut etre amené à être modifiée car peu de connaissances actuelles sur la quantique)

Personne 1 – Distribution d’intrication satellite-sol

Responsabilité unique :
Clarifier le cadre physique du scénario étudié.

Travail :
- Comprendre la distribution d’intrication par satellite
- Identifier : où est la source d’intrication, où a lieu la mesure de Bell, à quel moment l’interférence est requise

Travail pour réunion : (6 mai) :
- Schéma clair du scénario physique
- Description précise de la configuration étudiée
- Hypothèses simplificatrices explicitement listées


Personne 2 – Interférence Hong-Ou-Mandel et mesure de Bell

Responsabilité unique :
Relier différence de fréquence → perte d’interférence.

Travail :
- Définir le principe de l’effet Hong-Ou-Mandel
- Définir une mesure de Bell
- Définir la visibilité d’interférence

Travail poour réunion : (6 mai) :
- Note théorique structurée :
- rôle du recouvrement spectral
- Lien avec mesure de Bell


Personne 3 – Modèle mathématique du recouvrement spectral

Responsabilité unique :
Construire un modèle simple exploitable numériquement.

Travail :
- Choisir un modèle simple de photon :
- Écrire le recouvrement entre : photon sol, photon satellite décalé de Δf
- Obtenir une expression analytique du type :


Travail pour réunion : (10 mai) :
- Expression mathématique claire
- Paramètres physiques identifiés : largeur spectrale σ, décalage Δf


Personne 4 – Intégration numérique avec le Doppler

Responsabilité unique :
Relier la dynamique orbitale au modèle quantique.

Travail :
- Calculer : visibilité vs temps, perte moyenne sur un passage
- Étudier influence de : altitude, inclinaison, largeur spectrale du photon

Travail pour réunion : (13 mai) :
- Graphique : visibilité vs temps
- Analyse : moment de perte maximale, impact global sur la performance



# 5. Phase 5 – Consolidation et rédaction

Mi-mai → Juin

Objectifs
- Nettoyage du code
- Tests
- Documentation technique
- Rédaction du rapport
- Préparation de la présentation


Livrables finaux

Fin mai :
- Version stable du simulateur
- Figures finales

Début juin :
- Rapport final structuré
- Présentation orale
