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

"""
Given two 2D arrays flux and fluxer, zero-out all elements in the arrays 
for which:
 a) flux(i,j) == 0 or
 b) fluxer(i,j) / flux(i,j) >= limit
"""
def remove_problematic_values(flux_matrix, flux_error_matrix, limit=2e0):
    flux = deepcopy(flux_matrix)
    fluxer = deepcopy(flux_error_matrix)
    with np.nditer(nparray, op_flags=['readwrite'], flags=['multi_index']) as it:
        for x in it:
            if x == 0e0 or fluxer[it.multi_index] / x >= limit:
                x[...] = 0e0
                fluxer[it.multi_index] = 0e0
    return flux, fluxer

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

