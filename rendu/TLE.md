---
marp: true
---

# TLE

Standardized data format that encodes the orbital elements of an Earth-orbiting object at a given epoch. It provides the parameters needed to predict a satellite’s position and velocity.


Each TLE entry typically has an optional title line followed by two fixed-column numeric lines.

- Line 1 encodes identification data—satellite catalog number, international designator, epoch time, derivatives of mean motion, drag term (BSTAR), and checksum.

- Line 2 provides classical orbital elements—inclination, right ascension of ascending node, eccentricity, argument of perigee, mean anomaly, mean motion (revolutions per day), and revolution count at epoch.

---

Spaces and column positions are significant, and each line ends with a modulo-10 checksum for error detection.
Computational basis

From these, a satellite’s position and velocity can be predicted for short-term intervals—typically within about 1 km accuracy a few days from the epoch for low-Earth-orbit objects.