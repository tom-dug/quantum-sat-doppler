from src.model import Satellite, GroundStation
from datetime import datetime, timedelta
from org.orekit.frames import FactoryManagedFrame
from orekit.pyhelpers import datetime_to_absolutedate
import numpy as np

c = 299792458

# --- FUNCTIONS RELATED TO PHYSICAL CALCULATIONS OF THE DOPPLER EFFECT ---
# Calculating the dot product to determine relative velocity
def doppler_speed(sat: Satellite, station: GroundStation, date: datetime, repere: FactoryManagedFrame):
    """
    Calculates the dot product of the satellite's velocity and the line-of-sight vector between the satellite
    and the ground station.
    Inputs:
    - sat: an object of the Satellite class
    - station: an object of the GroundStation class
    """
    p_sat = sat.position(datetime_to_absolutedate(date), repere)
    v_sat = sat.velocity(datetime_to_absolutedate(date), repere)
    diff_norm = np.linalg.norm(p_sat - station.position(datetime_to_absolutedate(date), repere))
    time_change = diff_norm/c
    p_station = station.position(datetime_to_absolutedate(date + timedelta(seconds=time_change)), repere)
    v_station = station.velocity(datetime_to_absolutedate(date + timedelta(seconds=time_change)), repere)

    # Creating the line-of-sight vector
    relative_pos_vector = p_sat - p_station
    norm_relative_vect = relative_pos_vector/np.linalg.norm(relative_pos_vector)

    vitesse_relative = v_sat - v_station
    return np.dot(vitesse_relative, norm_relative_vect)

def relativist_doppler(speed: float | np.ndarray, frequency: float) -> float:
    """
    Takes as arguments the satellite's speed relative to the ground station and the
    transmission frequency. Returns the signal's reception frequency.
    Speeds in m/s
    """
    return frequency*np.sqrt((1-speed/c)/(1+speed/c))

def non_relativist_doppler(speed: float | np.ndarray, frequency: float) -> float:
    """
    Takes as arguments the satellite's speed relative to the ground station and the
    transmission frequency. Returns the signal's reception frequency.
    Speeds in m/s
    """
    return frequency/(1+speed/c)


def altitude(sat_pos: np.ndarray, station_pos: np.ndarray) -> float:
    """
    Calculates the distance between the satellite and the ground station.
    Inputs:
    - pos_sat: Satellite position vector (numpy array)
    - pos_station: Ground station position vector (numpy array)
    Returns:
    - Distance in kilometers
    """
    distance_vector = sat_pos - station_pos
    distance_meters = np.linalg.norm(distance_vector)
    return distance_meters / 1000.0  # Convert to kilometers

def elevation_angle(sat_pos: np.ndarray, station_pos: np.ndarray) -> float:
    """
    Calculates the elevation angle of the satellite relative to the ground station.
    Inputs:
    - pos_sat: Satellite position vector (numpy array)
    - pos_station: Ground station position vector (numpy array)
    Returns:
    - Elevation angle in degrees
    """
    # Normalized vector from station to satellite
    relative_vector = sat_pos - station_pos
    norm_relative_vector = relative_vector / np.linalg.norm(relative_vector)
    
    # Using the position vector of the ground station to define the local vertical direction
    local_vertical = station_pos / np.linalg.norm(station_pos)
    
    # Calculate the dot product and then the angle
    dot_product = np.dot(norm_relative_vector, local_vertical)
    elevation_rad = np.arccos(dot_product)
    
    # Convert radians to degrees
    elevation_deg = 90 - np.degrees(elevation_rad)
    
    return elevation_deg



# --- FONCTIONS LIEES A LA PHYSIQUE QUANTIQUE (EFFET HOM) ---

def visibilite_hom(frequence_ref: float, frequence_obs: float | np.ndarray, largeur_spectrale: float) -> float | np.ndarray:
    """
    Calculates the visibility of Hong-Ou-Mandel (HOM) interference between two photons.
    Based on the spectral overlap of two Gaussian wave packets.

    Inputs:
    - ref_frequency: Frequency of the ground-based photon (Hz) (omega_0)
    - obs_frequency: Frequency of the photon received from the satellite, shifted (Hz) (omega_obs)
    - spectral_width: Width of the photon's spectral band (Hz) (sigma_f)

    Returns:
    - Visibility (between 0 and 1)
    """
    frequence_obs_np = np.array(frequence_obs)
    delta_f = frequence_obs_np - frequence_ref
    
    visibilite = np.exp(- (delta_f**2) / (2 * largeur_spectrale**2))
    return visibilite
