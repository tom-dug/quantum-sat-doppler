# Effet Doppler et réseaux quantiques par satellites - SUIVI.md

Le fichier n'ayant pas complété avant le 24/04, les commits présents sur le git ont été exportés pour tracer le travail effectué.

## Feb 13, 2026 :
- Tom Dugail : Added SatOptLink submodule

## Feb 14, 2026 :
- Tom Dugail : Update README.md

- Tom Dugail : Added .gitignore

- Tom Dugail : Fix (?) calcul SatOptLink/visibility.py et début de plan

## Feb 18, 2026 :
- Alexis Durieu : Add csv files and  another exemple (with TLE) (x2)

- Alexis Durieu : Changed 'Codes' to 'src'

- Alexis Durieu : Add new file exampleMiciusParis.ipynb to run the programm with conda

- Alexis Durieu : Add new file exampleMiciusParis.py with little modifications

- Alexis Durieu : Add new file model.py with some minor modifications

- Alexis Durieu : Add new directory Codes to put the .py and .inbpy files

- Baptiste Gimenez : Edit plan.md (x3)

- Maxime Lussien : Edit plan.md

## Feb 19, 2026 :
- Baptiste Gimenez : Edit plan.md

## Feb 19, 2026 :
- Baptiste Gimenez : Edit plan.md (x6)

## Feb 20, 2026 :
- Maxime Lussien : Edit plan.md (x4)

- Baptiste Gimenez : Edit plan.md (x5)

- Tom Dugail : Modified gitignore

- Baptiste Gimenez : Edit plan.md

## Feb 23, 2026 :
- Baptiste Gimenez : Edit presentation.md (x2)

- Tom Dugail : Updated ignore (x2)

- Baptiste Gimenez : Edit presentation.md (x3)

- Baptiste Gimenez : maj git local image


- Baptiste Gimenez : .

- Tom Dugail : Edit PITCHME.md

- Baptiste Gimenez : Edit PITCHME.md (x3)

- Maxime Lussien : Edit PITCHME.md

- Alexis Durieu : Change display

## Feb 23, 2026 :
- Baptiste Gimenez : Edit ECEF vs ECI.md (x9)

- Baptiste Gimenez : changement nom présentation

- Maxime Lussien : Edit presentation.md (x3)

- Baptiste Gimenez : Edit presentation.md (x15)

---

## Mar 13, 2026 :
- Tom Dugail : Début code de calcul des orbites

## Mar 14, 2026 :
- Tom Dugail : Fonctions -> méthodes + nettoyage

- Tom Dugail : Nettoyage et ajout calcul vitesse

## Mar 16, 2026 :
- Maxime Lussien : parametres ECI et ECEF

- Baptiste Gimenez : paramètres képlériens

- Maxime Lussien : Edit ECEF vs ECI.md

- Tom Dugail : Fixes + ajout doppler

- Baptiste Gimenez : paramètres képlérien

- Alexis Durieu : Tracé 3D des ellipses

## Mar 16, 2026 :
- Tom Dugail : Ajout effet Doppler relativiste et non relativiste

- Tom Dugail : Implémentation de l'effet Doppler relativiste et non 
relativiste

- Maxime Lussien : Edit ECEF vs ECI.md (x4)

- Maxime Lussien : resolve conflict

- Maxime Lussien : dugail

- Baptiste Gimenez : phase 2

- Maxime Lussien : Edit ECEF vs ECI.md (x5)

- Baptiste Gimenez : TLE

- Baptiste Gimenez : resolve conflict

## Mar 19, 2026 :
- Tom Dugail : Petits fix

- Tom Dugail : Modif README

- Tom Dugail : Ajout fichier avancement et petits fix

- Tom Dugail : Fix effet doppler

- Maxime Lussien : documentation

## Mar 20, 2026 :
- Tom Dugail : Edit README.md (x2)

## Mar 24, 2026 :
- Tom Dugail : Nettoyage phases précédentes

---

## Apr 02, 2026 :
- Tom Dugail : Ajout de la détection d'évènement + fixes

## Apr 20, 2026 :
- Maxime Lussien : Edit ECEF vs ECI.md

- Tom Dugail : Ajout du calcul de l'altitude

- Maxime Lussien : V relative fct du Temps

- Maxime Lussien : Commentaire (x2)

## Apr 21, 2026 : 
Présentation de l'avancement de notre projet à nos encadrants avec une présentation de 20min.

## Apr 30, 2026 :
- Tom : réflexion sur la nouvelle structure du programme et transformation des plots en fonction appellables

---

## May 01, 2026 :
- Tom : début de la restructuration du code

## May 02, 2026 :
- Tom : avancement sur la restructuration, il sera nécessaire de reprendre la reprendre à cause d'imports circulaires

## May 03, 2026 :
- Tom : Afin d'améliorer la clarté et la modularité du projet, le code a été entièrement réorganisé :
    * **`physics.py`** (anciennement `orbit.py`) : Centralisation de tous les calculs liés à la physique.
    * **`detection.py`** (anciennement `visibility.py`) : Regroupement du gestionnaire et des fonctions de détection d'événements.
    * **`run.py`** (nouveau) : Création d'un point d'entrée unique facilitant le lancement du programme par l'utilisateur, sans nécessiter de connaissances préalables du code source.
- Tom : modification du calcul de l'altitude pour donner la distance satellite-station sol

## May 05, 2026 :

Reunion avec Matteo pour disucter de l'avancée du projet et de la partie quantique. Planification d'une réunion semaine prochaine avec les 2 encadrants pour presenter la quantique necessaire à l'elboration du projet.

- Alexis, Tom : -> Préparation de l'entretien avec notre encadrant M. Schiavon.
                -> Entretien en visio

- Alexis : compréhension du document "Interference at the Single Photon Level Along Satellite-Ground Channels"

- Maxime : documentation, ajout de sources et appropriation des notions de quantique, lecture du document "Interference at the Single Photon Level Along Satellite-Ground Channels" 

## May 13, 2026 :

- Alexis, Tom, Baptiste, Maxime : réunion de 1h30 avec les encadrants MATTEO SCHIAVON et Nicolas Fabre
        - établir la suite du projet pour la partie physique
        - calculs laborieux de physique quantique et de relativité restreinte
        - après entretien : reprise et retranscription des calculs en Latex

# May 23, 24, 2026 :

- Alexis :
    - préparation des slides pour l'audit du 27 mai
    - écriture des scripts pour chaque slide pour la présentation

- Maxime : préparation pour la présentation du 27 mai

---

# June 6, 7, 2026 :

- Tom : lecture de documentation pour la quantique (calcul de visibilité notamment)

# June 9, 2026 :

- Tom : implémentation des calculs quantique de visibilité et plots
- Maxime : relecture et analyse des retours de l'audit du 27 mai, appropriation des notions de quantique et calculs de visibilité.

# June 10 2026 :

- Alexis : mise en format LaTeX du calcul de modification d'un paquet d'onde par effet Doppler et avec transformation de Lorentz
- Tom : lecture de biblio et début de calcul du taux de coincidences

# June 12, 13, 14 2026 :

- Baptiste : Début du poster et exécution des derniers morceaux de code

<<<<<<< HEAD
# June 15 2026 :

- Tom, Baptiste, Maxime, Alexis: travail et realisation du poster, calcul de visibilité quantique.

# June 22 2026 :

- Alexis, Tom, Maxime : réunion avec Nicolas Fabre (encadrant) pour discuter du rendu final et avancer les calculs de physique quantique
- Alexis : résolution du début du TD sur la téléportation quantique
- Maxime : travail sur le TD de téléportation quantique et résolution de la seconde partie du TD
- Tom : début de la restitution du rapport sur le code

=======
# June 23, 2026 :
- Alexis : fin du travail sur la téléportation quantique et mise en cohérence des résultats
- Tom : avancement sur la partie du rapport expliquant le code (architecture, usage). Ajout du calcul de l'élévation dans le code et vérification des résultats avec différents satellites et différentes station sol. Autres modifications du code
- Baptiste : travail sur le poster et sur la partie physique du rapport
- Maxime : travail sur la teleportation quantique et sur le rapport

# June 24, 2026 :
Matin :
- Alexis, Tom : calculs de quantique et restranscription sur Overleaf
- Tom : recherche d'exemples pour tester le code dans différentes configurations
- Baptiste : correction des erreurs présentes dans le rapport
- Maxime : travail quantique 

Après-midi :
- Alexis, Tom, Baptiste : 2 réunions avec Nicolas Fabre pour revoir les calculs, le poster et les attendus pour le rapport
- Alexis : avancement sur les calculs de visibilité avec largeur spectrale modifiée par Doppler
- Baptiste : travail sur le poster et lecture de documentation sur le cadre global du projet pour le rapport
- Tom : retranscription des calculs sur Overleaf, amélioration du code et ajout d'exemples

# June 25, 2026 :
- Maxime : finalisation du poster et du rapport, preparation de la présentation finale.
- Baptiste : finalisation du poster.
- Alexis : finalisation des calucls de visibilité et retranscription sur Overleaf des résultats du TD de téléportation quantique pour le rapport