#! /usr/bin/python

from astropy.io import fits

""" 
Dead-simple loading of FITS image data to a numpy 2D array

No information are extracted; Also, we suppose we are only interested in 
the first HDU (in case more than one exist).
"""
def loadFitsImageData(fn: str):
    with fits.open(fn) as hdul: return hdul[0].data

if __name__ == "__main__":
    import sys
    ar = loadFitsImageData(sys.argv[1])
    print(ar.ndim)
    print(ar.shape)
