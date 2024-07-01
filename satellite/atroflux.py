#-*- coding: utf-8 -*-

import numpy as np
from scipy.ndimage.interpolation import rotate

def fluxError(a1,sa1,a2,sa2):
    if a1 != 0e0 and a2 != 0e0:
        par1 = sa1 / a1
        par2 = sa2 / a2
        error = (a1 * 100e0 / a2) * np.sqrt(par1 * par1 + par2 * par2)
    else:
        error = 0
    return error

def ratioError(a1,sa1,a2,sa2):
    if a1 != 0e0 and a2 != 0e0:
        par1 = sa1 / a1
        par2 = sa2 / a2
    else:
        par1 = par2 = 0e0
    return np.sqrt(par1*par1+par2*par2)

def specific_line_analysis(flux,flux_err,angle):
    # https://github.com/xanthospap/SATELLITE/blob/main/satellite/satellite/specific_line_analysis_script.py
    flux_rot = rotate(flux, angle, order=5)
    ha_rot = rotate(haa, angle, order=5)
    hb_rot = rotate(hbb, angle, order=5)
    size_rotx = flux_rot.shape[0]
    size_roty = flux_rot.shape[1]
    maxvalue = np.amax(flux)
    minvalue = maxvalue / 1000e0
    pixels_conversion = 1
    xoffset = x_slit_old - x_cs_old
    yoffset = y_slit_old - y_cs_old
    centerx = (size_rotx) / 2e0 + (xoffset * np.cos((-1) * np.pi * angle / 180) - yoffset * np.sin((-1) * np.pi * angle / 180))
    centery = (size_roty) / 2e0 + (xoffset * np.sin((-1) * np.pi * angle / 180) + yoffset * np.cos((-1) * np.pi * angle / 180))

"""
parameters:
    
"""
def specificPaLineFluxes(dict: cdct):
    # https://github.com/xanthospap/SATELLITE/blob/main/satellite/satellite/specificPA_line_fluxes_script.py
    pixscale = float(cdct['pixel_scale']) * 1e-2
    energy = 10**(float(cdct['energy_parameter']))
    energy_conversion = energy * pixscale * pixscale

    # for each slit
    for i in range(cdct['number_of_slits']):

