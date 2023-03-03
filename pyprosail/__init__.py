"""
A module that allows easy running of the ProSAIL (PROSPECT + SAIL) leaf and canopy
reflectance model.

The main function is `run`, which runs the ProSAIL model and returns the results as an array.

# Copyright (C) 2013  Robin Wilson, Modifications regarding code readability and function interfaces by Lukas Valentin Graf

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import annotations

import numpy as np
from _prosail_model import run as run_fortran

# Common leaf distributions
Planophile = (1, 0)
Erectophile = (-1, 0)
Plagiophile = (0, -1)
Extremophile = (0, 1)
Spherical = (-0.35, -0.15)
Uniform = (0, 0)

def run(
    n: float,
    cab: float,
    car: float,
    cbrown: float,
    cw: float,
    cm: float,
    psoil: float,
    lai: float,
    hspot: float,
    tts: float,
    tto: float,
    psi: float,
    typelidf: int,
    lidfa: int | float,
    lidfb: int | float
) -> np.ndarray:
    """
    Runs the ProSAIL model with the given parameters and returns a wavelength-reflectance
    array.

    Arguments:
      
      * ``n`` -- Structure co-efficient
      * ``cab`` -- Chlorophyll content (ug per cm^2)
      * ``car`` -- Carotenoid content (ug per cm^2)
      * ``cbrown`` -- Brown pigment content (arbitrary units)
      * ``cw`` -- Equivalent Water Thickness (cm)
      * ``cm`` -- Leaf Mass per unit area (g per cm^2)
      * ``psoil`` -- Soil reflectance: wet soil = 0, dry soil = 1
      * ``lai`` -- Leaf Area Index
      * ``hot_spot`` -- Hot spot parameter
      * ``tts`` -- Solar zenith angle (degrees)
      * ``tto`` -- Observer zenith angle (degrees)
      * ``psi`` -- relative azimuth angle (degrees)
      * ``typelidf`` -- Type of leaf angle distribution to use
      * ``lidfa`` -- Leaf distribution function parameter a (see below)
      * ``lidfb`` -- Leaf distribution function parameter b (see below)
      
    Returns:

      * ``arr`` -- a two-dimensional array with wavelengths in nm and 
        PROSAIL bi-directional reflectance factors

    If TypeLidf is 1 ``typelidf=1``:
        LIDFa and LIDFb define the average leaf slope and bimodality. These parameters must sum to be
        less than 1.0. For convenience a number of predefined options are given including:

              * Planophile
              * Erectophile
              * Plagiophile
              * Extremophile
              * Spherical
              * Uniform

    If TypeLidf is 2 ``typelidf=2``:

      * A single number defines the average leaf angle (in degrees) for an elipsoidal distribution.
      0 is planophile and 90 is erectophile.

    Examples of valid values for the leaf distribution function parameter include:

        * 30 (a 30 degree average leaf angle)
        * (0, -1) (an average leaf slope of 0 and a bimodality parameter of -1)
        * PyProsail.Planophile
    """
    
    # Check parameters here
    # TypeLidf must be either 1 or 2
    if typelidf not in [1, 2]:
        raise ValueError(f'TypeLidf must be either 1 or 2, got {typelidf}')

    if typelidf == 1 and lidfa + lidfb > 1:
        raise ValueError('If TypeLidf is 1 the sum of LIDFa and LIDFb must not be greater than 1.')

    wavelengths = np.arange(400, 2501)
    res = run_fortran(n, cab, car, cbrown, cw, cm, psoil, lai, hspot, tts, tto, psi, typelidf, lidfa, lidfb)
    arr = np.transpose(np.vstack((wavelengths, res)))

    return arr
