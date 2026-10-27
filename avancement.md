# Organisation du code

## `run.py`
- Fichier où l'utilisateur rentre ses paramètres et démarre le programme
- Définition des paramètres de simulation (TLE, coordonnées de la station, dates)
- Contrôle de la simulation et sélection des graphiques à afficher

## `orbit.py`
- Contient les fonctions appelées par `run.py` et effectue les calculs nécessaire aux instants utiles de l'orbite
- `start_simulation` : fonction principale qui exécute la boucle de propagation temporelle sur un passage donné, en appelant les outils physiques. Renvoie les listes de données calculées
- `plot_*` : Série de fonctions dédiées à l'affichage de plots (altitude, vitesse relative, effet Doppler, orbite 3D, visibilité)

## `physics.py`
- Contient les fonctions de calcul liées à la physique pure
- `doppler_speed` : calcul de la projection du vecteur vitesse du satellite sur le vecteur vue (utile pour calculer la nouvelle fréquence Doppler)
- `relativist_doppler` : calcul de l'effet Doppler relativiste
- `non_relativist_doppler` : calcul de l'effet Doppler classique

## `src/model.py`
- Reprise des classes implémentées par model.py venant du projet SatOptLink de AedenLeal, HanafiHanafiHanafi et matteoschiav 
- `Satellite` et `GroundStation` : classes qui contiennent notamment les méthodes `position` et `velocity` qui prennent en paramètre un instant et un repère

## `src/detection.py`
- Gestionnaire d'évènement pour limiter les calculs aux instants où le satellite est en visibilité directe de la station sol
- `sat_pass` : fonction qui permet de paramétrer les dates de recherche (pour éviter les temps de calcul trop longs)