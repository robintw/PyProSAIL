import _prosail_model
import numpy as np

# Common leaf distributions
Planophile = (1, 0)
Erectophile = (-1, 0)
Plagiophile = (0, -1)
Extremophile = (0, 1)
Spherical = (-0.35, -0.15)
Uniform = (0, 0)

def run(N, chloro, caroten, brown, EWT, LMA, psoil, LAI, hot_spot, solar_zenith, solar_azimuth, view_zenith, view_azimuth, LIDF):
	"""
	Runs the ProSAIL model with the given parameters and returns a wavelength-reflectance
	array.

	Arguments:
      
      * ``N`` -- Structure co-efficient
      * ``chloro`` -- Chlorophyll content (ug per cm^2)
      * ``caroten`` -- Carotenoid content (ug per cm^2)
      * ``brown`` -- Brown pigment content (arbitrary units)
      * ``EWT`` -- Equivalent Water Thickness (cm)
      * ``LMA`` -- Leaf Mass per unit area (g per cm^2)
      * ``soil_reflectance`` -- Soil reflectance: wet soil = 0, dry soil = 1
      * ``LAI`` -- Leaf Area Index
      * ``hot_spot`` -- Hot spot parameter
      * ``solar_zenith`` -- Solar zenith angle (degrees)
      * ``solar_azimuth`` -- Solar azimuth angle (degrees)
      * ``view_zenith`` -- View zenith angle (degrees)
      * ``view_azimuth`` -- View azimuth angle (degrees)
      * ``LIDF`` -- Leaf distibution function parameter(s) (see below)

    The leaf distribution function parameter(s) argument can be either:

      * A single number giving the average leaf angle (in degrees) for an elipsoidal distribution. 0 is planophile and 90 is erectophile.
      * A tuple giving (average leaf slope, bimodality parameter). These parameters must sum to be less than 1.0. For
      convenience a number of predefined options are given including:

      		* Planophile
      		* Erectophile
      		* Plagiophile
      		* Extremophile
      		* Spherical
      		* Uniform

    Examples of valid values for the leaf distribution function parameter include:

    	* 30 (a 30 degree average leaf angle)
    	* (0, -1) (an average leaf slope of 0 and a bimodality parameter of -1)
    	* PyProsail.Planophile

    Example usage:

    

	"""

	try:
		l = len(LIDF)
		if l != 2:
			# Raise error
			pass

		TypeLidf = 1
		LIDFa = LIDF[0]
		LIDFb = LIDF[1]
	except TypeError:
		TypeLidf = 2
		LIDFa = LIDF
		LIDFb = 0

	return(_run_prosail(N, chloro, caroten, brown, EWT, LMA, psoil, LAI, hot_spot, solar_zenith, view_zenith, solar_azimuth, TypeLidf, LIDFa, LIDFb))

def _run_prosail(N, Cab, Car, Cbrown, Cw, Cm, psoil, LAI, hspot, tts, tto, psi, TypeLidf, LIDFa, LIDFb):
	# Check parameters here

	# TypeLidf must be either 1 or 2
	if TypeLidf not in [1, 2]:
		# Raise exception
		pass

	if TypeLidf == 1 and LIDFa + LIDFb > 1:
		# Raise exception
		pass

	wavelengths = np.arange(400, 2501)
	res = _prosail_model.run(N, Cab, Car, Cbrown, Cw, Cm, psoil, LAI, hspot, tts, tto, psi, TypeLidf, LIDFa, LIDFb)

	arr = np.transpose(np.vstack( (wavelengths/1000.0, res) ))
	return arr