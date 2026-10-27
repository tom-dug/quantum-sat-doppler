from src import orbit
from src import detection
from src import model
from org.orekit.frames import FramesFactory
from datetime import datetime


# Ground station parameters, format: [x, y, altitude, “name”]
sol_params = [48.8566, 2.3522, 80, "Paris"]

# Satellite parameters (TLE)
# Micius (Orbite Polaire)
tle_line_1 = "1 41731U 16051A   24016.15735159  .00011450  00000-0  34540-3 0  9998"
tle_line_2 = "2 41731  97.3167 289.0989 0012522  59.2544 300.9930 15.34373256413200"


# Communication settings
transmission_frequency = 370e12
spectral_width = 10e9

# Simulation parameters
START_TIME = datetime(2024, 1, 16)
END_TIME = datetime(2024, 1, 18)

# Minimum elevation angle required for the satellite to be considered visible from the ground station
MIN_ELEVATION_ANGLE = 10  # degrees

# Available plots :
PLOT_ALTITUDE = False
PLOT_RELATIVE_SPEED = True
PLOT_NON_RELATIVIST_DOPPLER = False
PLOT_RELATIVIST_DOPPLER = True
PLOT_DOPPLER_DIFFERENCE = False
PLOT_ORBITE_3D = False
PLOT_VISIBILITY = True
PLOT_ELEVATION = True


# Select a certain passage
PASSAGE_INDEX = 0  # 0 for the first passage, 1 for the second, etc.

# --- DEFINITION OF THE SATELLITE ---
tle = (tle_line_1, tle_line_2)
satellite = model.Satellite(tle)

# --- DEFINITION OF THE GROUND STATION ---
ground_station = model.GroundStation(*sol_params)

# --- SETTING THE TIME AND SPACE ---
# We choose the EME2000 reference frame (inertial, fixed relative to the stars)
inertial_frame = FramesFactory.getEME2000()

# Select the simulation duration (choose a sat_pass segment)
passages = detection.sat_pass(satellite, ground_station, START_TIME, END_TIME, MIN_ELEVATION_ANGLE)

if len(passages) == 0:
    print("No satellite passes found for the given time period and minimum elevation angle.")
    exit()
else:
    passage = passages[PASSAGE_INDEX]  # Select the desired passage for the simulation


# Simulation results
time, sat_altitude, ps_plot, non_rel_doppler_freq, rel_doppler_freq, visibility, sat_elevation = orbit.start_simulation(satellite, ground_station, passage, inertial_frame, transmission_frequency, spectral_width)


if PLOT_ALTITUDE:
    orbit.plot_altitude(sat_altitude, time)

if PLOT_RELATIVE_SPEED:
    orbit.plot_relative_speed(ps_plot, time)

if PLOT_ELEVATION:
    orbit.plot_elevation(sat_elevation, time)

if PLOT_NON_RELATIVIST_DOPPLER:
    orbit.plot_nrel_doppler(non_rel_doppler_freq, time)

if PLOT_RELATIVIST_DOPPLER:
    orbit.plot_rel_doppler(rel_doppler_freq, time)

if PLOT_DOPPLER_DIFFERENCE:
    orbit.plot_doppler_difference(rel_doppler_freq, non_rel_doppler_freq, time)

if PLOT_ORBITE_3D:
    orbit.plot_3D_orbit(satellite, inertial_frame, ground_station, START_TIME, duration_minutes=100)

if PLOT_VISIBILITY:
    orbit.plot_visibility(visibility, time)
