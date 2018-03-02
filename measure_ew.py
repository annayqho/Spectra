""" Measure the equivalent width of a spectral line """

import scipy.integrate as integrate

def measure_ew(wl, flux, start_wl, end_wl):
    """ Takes normalized spectrum """
    integrand = 1-flux
    ew = integrate.quad(integrand, start_wl, end_wl)
    return ew
