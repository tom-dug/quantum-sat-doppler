import numpy as np
import math
from org.orekit.propagation.events import ElevationDetector
from org.orekit.propagation.events.handlers import PythonEventHandler
from org.hipparchus.ode.events import Action
from org.orekit.propagation import SpacecraftState

from orekit.pyhelpers import datetime_to_absolutedate



class VisibilityHandler(PythonEventHandler):
  def __init__(self):
    super().__init__()
    self.passages = []
    self.current_start = None

  def init(self, *args):
    pass

  def eventOccurred(self, s: SpacecraftState, detector, increasing: bool):
    if increasing:
      self.current_start = s.getDate()

    else:
      if self.current_start is not None:
        self.passages.append((self.current_start, s.getDate()))
        self.current_start = None
    
    return Action.CONTINUE

  def resetState(self, eventDetector, spacecraftState):
    return super().resetState(eventDetector, spacecraftState)
  
  def finish(self, spacecraftState, eventDetector):
    pass


def sat_pass(satellite, ground_station, date_debut_sim, date_fin_sim, min_elevation_angle):
  """
  Provides a list of the satellite's passes over the ground station over a one-year period
  """
  handler = VisibilityHandler()
  min_elevation = math.radians(min_elevation_angle)

  visibility_detector = ElevationDetector(ground_station.frame).withConstantElevation(min_elevation).withHandler(handler)
  satellite.propagator.addEventDetector(visibility_detector)

  satellite.propagator.propagate(datetime_to_absolutedate(date_debut_sim), datetime_to_absolutedate(date_fin_sim))
  sat_pass = handler.passages
  satellite.propagator.clearEventsDetectors()
  
  return sat_pass