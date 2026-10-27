"""
Examples of the satellites and ground stations that can be used in the simulation
You can modify these parameters in run.py to simulate different scenarios
"""


"""
Satellites
"""
# Micius (Polar Orbit)
tle_line_1 = "1 41731U 16051A   24016.15735159  .00011450  00000-0  34540-3 0  9998"
tle_line_2 = "2 41731  97.3167 289.0989 0012522  59.2544 300.9930 15.34373256413200"

# SpooQy (Orbit with a 51° incline)
tle_line_1 = "1 44331U 19034B   24016.15735159  .00015420  00000-0  24510-3 0  9992"
tle_line_2 = "2 44331  51.6341 120.4321 0008542 110.2341 250.9432 15.54321076241320"

# IXPE (Equatorial Orbit)
tle_line_1 = "1 49954U 21119A   24016.50000000  .00002231  00000-0  10355-3 0  9996"
tle_line_2 = "2 49954   0.2012  64.5388 0012211  52.8368 307.3015 15.15582310118187"


"""
Ground stations
"""
# Paris
sol_params = [48.8566, 2.3522, 80, "Paris"]

# Cote d'Azur
sol_params = [43.7547, 6.9214, 1270, "Cote_Azur"]

# Equateur
sol_params = [-0.2149, -78.5025, 2818, "Quito"]

# NUS
sol_params = [1.2984, 103.7763, 15, "NUS"]

# FHNW
sol_params = [47.5345, 7.6419, 200, "FHNW"]