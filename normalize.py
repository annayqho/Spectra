""" Normalize a spectrum """

import numpy as np
import matplotlib.pyplot as plt


def gaussian_weight_matrix(wl, L):
    """ Matrix of Gaussian weights 

    Parameters
    ----------
    wl: numpy ndarray
        pixel wavelength values
    L: float
        width of Gaussian in pixels

    Return
    ------
    Weight matrix
    """
    return np.exp(-0.5*(wl[:,None]-wl[None,:])**2/L**2)


def smooth_spec(wl, flux, ivar, L):
    """ Smooth a spectrum with a running Gaussian

    Parameters
    ----------
    wl: numpy ndarray
        pixel wavelength values
    flux: numpy ndarray
        pixel flux values
    ivar: numpy ndarray
        pixel inverse variances

    Returns
    ------
    smoothed: numpy ndarray
        smoothed flux values
    """
    w = gaussian_weight_matrix(wl, L)
    bot = np.dot(ivar, w.T)
    top = np.dot(flux*ivar, w.T)
    bad = bot == 0
    smoothed = np.zeros(top.shape)
    smoothed[~bad] = top[~bad] / bot[~bad]
    return smoothed


def normalize(wl, flux, ivar, L):
    """ Normalize by dividing by a Gaussian-weighted smoothed spectrum

    Parameters
    ----------
    wl: numpy ndarray
        pixel wavelength values
    flux: numpy ndarray
        pixel flux values
    ivar: numpy ndarray
        pixel inverse variances
    L: float
        width of Gaussian in pixels

    Return
    ------
    flux: normalized spectrum
    """
    smoothed_spec = smooth_spec(wl, flux, ivar, L)
    norm_flux = flux / smoothed_spec
    norm_ivar = ivar * smoothed_spec**2
    return norm_flux, norm_ivar
