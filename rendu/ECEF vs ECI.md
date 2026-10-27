---
marp: true
---

# ECEF vs ECI

![bg](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2003/01/artemis_satellite_artist_s_view/9518536-4-eng-GB/Artemis_satellite_artist_s_view_pillars.jpg)

---

# ECEF

![bg right](https://www.neozone.org/blog/wp-content/uploads/2024/02/science-planete-formation-etude-ronde-plate-001.jpg)

## (convention WGS 84)
---

![bg left:30% 100%](https://rennes-le-chateau-archive.com/images/meridien/globe_meridien.gif)

*Earth-centered, Earth-fixed coordinate system* (ECEF) = repère centré sur le centre de masse de la Terre

Rq : Surtout utilisé pour **suivre les satellites depuis la surface de la Terre**.

#### Axes : 
- Oz : Axe orienté du pôle Sud vers le pôle Nord (≠axe de rotation de la Terre), donc bouge dans le temps
- Ox : Dans le plan de l'équateur, Axe orienté depuis 180° de longitude (négatif) (à l'ouest du méridien de Greenwich) vers le méridien de Greenwich à 0° de longitude (positif). (En WGS 84, c'est le IERS)
- Oy : Dans le plan de l'équateur, Axe orienté depuis 90°W longitude (négatif) vers 90°E longitude (positif)

---

![bg left:40% 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ecef_coordinates.svg/1920px-Ecef_coordinates.svg.png)

#### Variables : 
- Distance géocentrique : **R** (rayon centre de masse de la Terre - objet)
- Distance entre le centre de la Terre et un point situé sur l’ellipsoïde de référence, à une latitude donnée : **R0**
- Altitude géocentrique : **h′** = R − R0 (à ne pas confondre avec l'altitude géodésique)

Rq : L'altitude géodésique est normale à la surface

---

![bg right](https://cdn.pixabay.com/photo/2020/02/16/02/49/space-4852442_1280.jpg)

# ECI

## (*Earth-Centered Inertial*)
---

![bg left 30% 90%](https://upload.wikimedia.org/wikipedia/commons/3/32/Earth_Centered_Inertial_Coordinate_System.png)

Repère centré sur le centre de masse de la Terre, mais **non solidaire de la rotation terrestre**.

Rq : il est considéré comme **quasi inertiel** pour l'étude du mouvement des satellites.



### Axes :
- Axe z : pointe vers le pôle Nord (l’axe de rotation terrestre).
- Axe x : pointe vers une direction fixe dans le ciel, souvent le point vernal (équinoxe de printemps)
- Axe y : complète le repère orthogonal.

# Propriétés du repère ECI

#### Caractéristiques :
- Le repère **ne tourne pas avec la Terre**
- La trajectoire d’un satellite y est plus simple à décrire
- Les lois de Newton s’y appliquent de manière approchée sans forces d’inertie de rotation terrestre

#### Utilisation :
- propagation d’orbite
- mécanique spatiale
- calcul des trajectoires de satellites

---

# Lien entre ECI et ECEF

![bg left:35% 90%](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQ-POJWiVzO4HWAbOWTyvQhB1cSfQ2JyCxuMhUF37oriwn2OWNrL11vuD0&s=10)

Les deux repères ont la **même origine** : le centre de la Terre.

La différence essentielle est que :

- le repère **ECEF tourne avec la Terre**
- le repère **ECI reste fixe dans l’espace**

Ainsi, pour passer de **ECI vers ECEF**, on effectue une **rotation autour de l’axe Oz** d’un angle égal à l’angle de rotation de la Terre.

---

# Résumé

| Repère | Origine | Axes fixes par rapport à | Usage principal |
|-------|---------|---------------------------|-----------------|
| ECEF  | Centre de la Terre | la Terre | positionnement au sol, stations, suivi depuis la Terre |
| ECI   | Centre de la Terre | l’espace lointain | dynamique orbitale, mécanique spatiale
---

# Conversion ECI → ECEF

Les deux repères ont :

- la **même origine** : centre de la Terre  
- le **même axe z** : axe de rotation terrestre  

La différence est que :

- **ECI** : repère fixe dans l’espace  
- **ECEF** : repère qui **tourne avec la Terre**

---

## Principe de la conversion


La transformation consiste en une **rotation autour de l’axe z**.

Angle de rotation :

**θ = ωₑ t**

avec

- **ωₑ ≈ 7.2921159 × 10⁻⁵ rad/s**
- vitesse de rotation de la Terre


## Interprétation physique


Dans le repère **ECI** :

- la Terre **tourne sous le satellite**

Dans le repère **ECEF** :

- la Terre est **fixe**
- la trajectoire du satellite **évolue dans le temps**














