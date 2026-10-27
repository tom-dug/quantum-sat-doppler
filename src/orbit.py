import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- INITIALISATION D'OREKIT ---
import orekit
from orekit.pyhelpers import download_orekit_data_curdir, setup_orekit_curdir, datetime_to_absolutedate, absolutedate_to_datetime

# orekit.initVM()
# download_orekit_data_curdir()
# setup_orekit_curdir()


from org.orekit.frames import FactoryManagedFrame, FramesFactory
from org.orekit.time import AbsoluteDate
from org.hipparchus.geometry.euclidean.threed import Vector3D
from org.orekit.propagation.events import ElevationDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
# from org.orekit.propagation.analytical.tle import TLE, TLEPropagator
from org.orekit.utils import Constants


from src.physics import altitude, doppler_speed, elevation_angle, relativist_doppler, non_relativist_doppler, visibilite_hom



def start_simulation(satellite, ground_station, passage, inertial_frame, frequency, spectral_width):
    # Arrays for storing satellite coordinates and velocities as X, Y, Z triplets
    sat_pos = []
    sat_vel = []

    # Arrays for storing station information
    station_pos = []
    station_vel = []


    # --- THE PROPAGATION LOOP ---
    print("Calculating the orbit...")

    start_date, end_date = absolutedate_to_datetime(passage[0]), absolutedate_to_datetime(passage[1])
    pass_duration = end_date - start_date
    print(f"Duration of stay : {pass_duration.total_seconds()} seconds")
    time_step_seconds = 5

    time = []
    ps_plot = []
    rel_doppler_freq = []
    non_rel_doppler_freq = []
    sat_altitude = []
    sat_elevation = []
    visibility = []

    for second in range(0, int(pass_duration.total_seconds()), time_step_seconds):
        # We calculate the current time in the loop and convert it for Orekit
        current_date = start_date + timedelta(seconds=second)
        orekit_date = datetime_to_absolutedate(current_date)

        # Fill in the satellite position and velocity lists
        sat_pos.append(satellite.position(orekit_date, inertial_frame))
        sat_vel.append(satellite.velocity(orekit_date, inertial_frame))

        # The same applies to the ground station in the same coordinate system
        station_pos.append(ground_station.position(orekit_date, inertial_frame))
        station_vel.append(ground_station.velocity(orekit_date, inertial_frame))


        # Calculating the velocity to be used for the Doppler effect
        ps = doppler_speed(satellite, ground_station, current_date, inertial_frame)

        ps_plot.append(ps)
        time.append(second)
        rel_doppler_freq.append(relativist_doppler(ps, frequency))
        non_rel_doppler_freq.append(non_relativist_doppler(ps, frequency))

        visibility.append(visibilite_hom(frequency, rel_doppler_freq[-1], spectral_width))

        # Calculation of the satellite-to-station distance
        sat_altitude.append(altitude(sat_pos[-1], station_pos[-1]))
        sat_elevation.append(elevation_angle(sat_pos[-1], station_pos[-1]))

    return time, sat_altitude, ps_plot, non_rel_doppler_freq, rel_doppler_freq, visibility, sat_elevation



# --- FUNCTION TO DISPLAY PLOTS ---
def plot_altitude(sat_altitude, time):
    """
    Displays the distance between the satellite and the station during the pass
    """
    plt.figure()
    plt.plot(time, sat_altitude, color='orange', linewidth=2)
    plt.title("Satellite altitude at the time of overpass")
    plt.ylabel("Altitude (km)")
    plt.xlabel("Time (s)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plot_relative_speed(ps_plot, time):
    """
    Displays the satellite's relative speed during its pass
    """
    plt.plot(time, ps_plot)
    plt.title("Relative speed as a function of time")
    plt.ylabel("Relative speed (m/s)")
    plt.xlabel("Time (s)")
    plt.show()

def plot_nrel_doppler(non_rel_doppler_freq, time):
    """
    Displays the Doppler effect using a non-relativistic calculation
    """
    plt.plot(time, non_rel_doppler_freq)
    plt.title("Received frequency (non-relativistic) as a function of time")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.show()

def plot_rel_doppler(rel_doppler_freq, time):
    """
    Displays the Doppler effect using relativistic calculations
    """
    plt.plot(time, rel_doppler_freq)
    plt.title("Received frequency (relativistic) as a function of time")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.show()

def plot_doppler_difference(rel_doppler_freq, non_rel_doppler_freq, time):
    """
    Shows the difference between the relativistic and non-relativistic calculations of the Doppler effect
    """
    plt.plot(time, np.array(rel_doppler_freq)-np.array(non_rel_doppler_freq))
    plt.title("Difference in Doppler calculation (relative vs. non-relative) as a function of time")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.show()

def plot_3D_orbit(satellite, inertial_frame, ground_station,start_time, duration_minutes=100):
    """
    Displays a 3D representation of the satellite in Earth orbit
    """
    # --- 3D VISUALIZATION WITH MATPLOTLIB ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Making the Earth (in km)
    rayon_terre_km = Constants.WGS84_EARTH_EQUATORIAL_RADIUS / 1000.0
    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
    x_terre = rayon_terre_km * np.cos(u) * np.sin(v)
    y_terre = rayon_terre_km * np.sin(u) * np.sin(v)
    z_terre = rayon_terre_km * np.cos(v)
    ax.plot_surface(x_terre, y_terre, z_terre, color='lightblue', alpha=0.4, edgecolor='none')

    # Representation of the satellite's orbit
    x_sat, y_sat, z_sat = [], [], []

    # Simulating for the specified duration
    for minute in range(duration_minutes):
        current_date = start_time + timedelta(minutes=minute)
        plot_date_orekit = datetime_to_absolutedate(current_date)

        pos_vect_metres = satellite.position(plot_date_orekit, inertial_frame)
        
        # Converting from meters to kilometers for plotting
        x_sat.append(pos_vect_metres[0] / 1000.0)
        y_sat.append(pos_vect_metres[1] / 1000.0)
        z_sat.append(pos_vect_metres[2] / 1000.0)
    
    ax.plot(x_sat, y_sat, z_sat, color='red', linewidth=2, label="Orbite du satellite")

    ax.scatter(x_sat[0], y_sat[0], z_sat[0], color='green', s=50, label="Point de départ")

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title("Simulation of the 3D orbit")
    ax.legend()

    # D. Représentation de la station sol (à la date de départ)
    plot_date_orekit = datetime_to_absolutedate(start_time)
    pos_station_metres = ground_station.position(plot_date_orekit, inertial_frame)
    x_station = pos_station_metres[0] / 1000.0
    y_station = pos_station_metres[1] / 1000.0
    z_station = pos_station_metres[2] / 1000.0
    
    pos_norme = np.array([x_station, y_station, z_station])
    vecteur_vertical = pos_norme / np.linalg.norm(pos_norme)
    
    # On ajoute une élévation artificielle de 250 km pour que le point "flotte" 
    # juste au-dessus de la surface bleue et ne soit plus masqué
    elevation_visuelle = 250.0 
    pos_visuelle = pos_norme + vecteur_vertical * elevation_visuelle
    
    # 3. On trace le point avec l'élevation et l'argument zorder=5 pour le mettre au premier plan
    ax.scatter(pos_visuelle[0], pos_visuelle[1], pos_visuelle[2], 
               color='gold', s=150, marker='^', edgecolor='black', zorder=5,
               label=f"Station : {ground_station.name}")

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title("Simulation of the 3D orbit")
    
    # --- CONFIGURATION DE LA VUE ET DE LA LÉGENDE ---
    ax.legend() # Placé ici, il captera automatiquement le label de la station sol

    # Forcer les axes à avoir la même échelle
    limite = 8000
    ax.set_xlim([-limite, limite])
    ax.set_ylim([-limite, limite])
    ax.set_zlim([-limite, limite])
    ax.set_box_aspect([1, 1, 1])

    long_deg = np.degrees(ground_station.longitude)
    
    # ax.view_init(elev=30, azim=long_deg)

    plt.show()

def plot_visibility(visibility, time):
    """
    Displays the visibility using relativistic calculations
    """
    plt.plot(time, visibility)
    plt.title("Visibility as a function of time")
    plt.ylabel("Visibility")
    plt.xlabel("Time (s)")
    plt.show()

def plot_elevation(sat_elevation, time):
    """
    Displays the elevation angle of the satellite relative to the ground station during its pass
    """
    plt.plot(time, sat_elevation)
    plt.title("Satellite Elevation Angle as a function of time")
    plt.ylabel("Elevation Angle (degrees)")
    plt.xlabel("Time (s)")
    plt.show()