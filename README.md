## Note

This repository is a copy that serves as a showcase for a project I worked on. Although I was responsible for the code available here, a significant part of the project involved performing quantum physics calculations on paper, which are therefore not available here.


# Doppler Effect and Satellite Quantum Networks

An orbital and quantum simulator for evaluating the impact of the relativistic Doppler effect on the spectral overlap of photons in the context of satellite quantum communications (e.g., the Micius space experiment).

## To run the code
1. Open the `run.py` file.
2. Modify the desired parameters (dates, selection of graphs to display via the Boolean variables `PLOT_*`, ...).
3. Run the `run.py` file.

## Project Organization

#### `plan.md`
- Overall plan and project development milestones (Phases 1 through 5).

#### `avancement.md`
- Log and detailed summary of changes made to the code (architecture, added modules, resolved bugs).

#### `run.py`
- Main entry point. Handles user parameters, runs calculations, and displays results.

#### `src/orbit.py`
- Simulation module containing the orbital propagation loop and graphing functions (Matplotlib).

#### `src/physics.py`
- Module containing the pure physical equations (calculation of relative radial velocities, Doppler effect formulas).

#### `src/model.py`
- File defining physical objects (`Satellite`, `GroundStation`) that serve as the bridge to the Orekit space engine (Earth, inertial reference frames).

#### `src/detection.py`
- Orekit module that handles event detection to analytically determine the exact visibility windows of the satellite as it passes over the ground station.