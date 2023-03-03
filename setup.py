
from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration


# define PROSAIL Fortran library
prosail_fortran_lib = Extension(
    name='_prosail_model',
    sources = [
        './pyprosail/MODULE_PRO4SAIL.f90',
        './pyprosail/dataSpec_P5B.f90',
        './pyprosail/LIDF.f90',
        './pyprosail/dladgen.f',
        './pyprosail/PRO4SAIL.f90',
        './pyprosail/prospect_5B.f90',
        './pyprosail/tav_abs.f90',
        './pyprosail/volscatt.f90',
        './pyprosail/PyPROSAIL.f90'
    ]
)

# define Python package setup
setup(
    name='pyprosail',
    packages=['pyprosail'],
    version='1.0.2',
    author='Robin Wilson',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python3"
    ],
    ext_modules=[prosail_fortran_lib]
)
