#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
18/01/2024

@author: schiavon, snailpi

Original description: This script implements the actual moving satellite channel to be used with the
FixedSatelliteLossModel NetSQUID class.

v00     Changes made:
    - removed lowtran dependence
    - removed all calculations other than satellite coordinates

v01     Changes made:
    - added keplerian propagation
"""
import pandas as pd
import orekit

from orekit.pyhelpers import download_orekit_data_curdir, setup_orekit_curdir, datetime_to_absolutedate

import os

import numpy as np

from math import radians

from datetime import datetime, timedelta

# setup orekit
vm = orekit.initVM()

if not os.path.isfile('orekit-data.zip'):
    download_orekit_data_curdir()

setup_orekit_curdir()

# Orekit imports
from org.orekit.propagation.analytical.tle import TLE, TLEPropagator
from org.orekit.propagation.analytical import KeplerianPropagator
from org.orekit.orbits import KeplerianOrbit
from org.orekit.frames import FramesFactory, TopocentricFrame, FactoryManagedFrame
from org.orekit.bodies import OneAxisEllipsoid, GeodeticPoint
from org.orekit.utils import IERSConventions, Constants
from org.orekit.time import AbsoluteDate
from org.hipparchus.geometry.euclidean.threed import Vector3D

# Prepare global variables - time and space reference systems
ITRF = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
earth = OneAxisEllipsoid(Constants.WGS84_EARTH_EQUATORIAL_RADIUS,
                         Constants.WGS84_EARTH_FLATTENING, ITRF)
inertialFrame = FramesFactory.getEME2000()


# utc = TimeScalesFactory.getUTC()


# Define classes for the different objects
class orbitModelError(Exception):
    pass


class Satellite:
    """ Satellite orbit

    This class implements a real satellite orbit.

    The class defines the satellite using different simulation orbit techniques:
        * 'tle': use the two-line elements (TLE) of an existing satellite
        * "kepler": use the Keplerian elements:
            - a
            - e
            - i
            - omega
            - Omega
            - v
        * 'polOrbPass': use the model of polar orbit passage described in
            [Moll et al., PRA 99, 053830 (2019)]
            ⚠️ Ce type de simulation est très simplifié, il n'a besoin que de l'altitude du satellite
            et son angle d'inclinaison lors de son passage

    Paramters
    ---------
    incAngle: float
        Inclination angle of the satellite w.r.t. the ground station [deg].
    satAlt: float
        Altitude of the satellite [km].
    """

    simTypeAllowed = ('tle', 'polOrbPass', "keplerian", '')

    def __init__(self, params, simType='tle', incAngle=0, satAlt=0):
        self.simType = simType

        if simType == 'tle':
            """ Initialization of the satellite orbit from a TLE list """
            self.setSimTLE(params)
        elif simType == 'keplerian':
            """ Initialization of the satellite orbit from a Keplerian list """
            self.setSimKeplerian(params)
        elif simType == 'polOrbPass':
            self.setSimPolOrbPass(incAngle, satAlt)
        else:
            self.simType = ''

    def setSimTLE(self, tle):
        self.simType = 'tle'
        self.tleList = tle
        self.tleObject = TLE(*self.tleList)
        self.propagator = TLEPropagator.selectExtrapolator(self.tleObject)

    def setSimKeplerian(self, kepler):
        self.simType = 'keplerian'
        self.keplerList = kepler
        self.keplerObject = KeplerianOrbit(*self.keplerList)
        self.propagator = KeplerianPropagator(self.keplerObject)

    def setSimPolOrbPass(self, incAngle, satAlt):
        self.simType = 'polOrbPass'
        self.incAngle = radians(incAngle)
        self.satAlt = satAlt * 1e3

    def isPolOrbPass(self):
        return (self.simType == 'polOrbPass')

    def isTLE(self):
        return (self.simType == "tle")

    def isKeplerian(self):
        return (self.simType == 'keplerian')
    
    def position(self, date: AbsoluteDate, repere: FactoryManagedFrame):
        """
        Returns the coordinates of its position vector as an array
        """
        # Asking the propagator for the information
        pv = self.propagator.propagate(date).getPVCoordinates(repere)

        # Extracting the satellite's position vector and velocity vector
        position = pv.getPosition()
        pos_vect = np.array([position.getX(), position.getY(), position.getZ()])
        return pos_vect
    
    def velocity(self, date: AbsoluteDate, repere: FactoryManagedFrame):
        pv = self.propagator.propagate(date).getPVCoordinates(repere)
        velocity = pv.getVelocity()
        vel_vect = np.array([velocity.getX(), velocity.getY(), velocity.getZ()])
        return vel_vect
    
    def altitude(self, date: AbsoluteDate, repere: FactoryManagedFrame):
        """
        Calculates the exact altitude of the satellite relative to the Earth's surface.
        """
        # Retrieving the spatial position
        pv = self.propagator.propagate(date).getPVCoordinates(repere)
        position_spatiale = pv.getPosition()
        
        # We use the global object ‘earth’ (OneAxisEllipsoid) defined at the beginning of model.py
        # Conversion of spatial coordinates to Earth coordinates (latitude, longitude, altitude)
        point_geodesique = earth.transform(position_spatiale, repere, date)
        
        return point_geodesique.getAltitude()


class GroundStation:
    """ Ground station

    This class implements a ground station.

    Parameters
    ----------
    latitude: float
        Latitude of the ground station [degrees]. Positive towards North.
    longitude: float
        Longitude of the ground station [degrees]. Positive towards East.
    altitude: float
        Altitude of the ground station [m].
    name: str
        Name of the station
    """

    def __init__(self, lat, long, alt, name):
        self.latitude = radians(lat)
        self.longitude = radians(long)
        self.altitude = float(alt)
        self.name = name

        # Define the station Topocentric Frame
        self.geodeticPoint = GeodeticPoint(self.latitude, self.longitude, self.altitude)
        self.frame = TopocentricFrame(earth, self.geodeticPoint, self.name)

    def position(self, date: AbsoluteDate, repere: FactoryManagedFrame):
        pv = self.frame.getPVCoordinates(date, repere)
        
        position = pv.getPosition()
        pos_vect = np.array([position.getX(), position.getY(), position.getZ()])

        return pos_vect
    
    def velocity(self, date: AbsoluteDate, repere: FactoryManagedFrame):
        pv = self.frame.getPVCoordinates(date, repere)
        velocity = pv.getVelocity()
        vel_vect = np.array([velocity.getX(), velocity.getY(), velocity.getZ()])
        return vel_vect