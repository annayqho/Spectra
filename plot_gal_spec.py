import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import numpy as np
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')
import sys
sys.path.append("/Users/annaho/Dropbox/Research/Spectra")
from normalize import *


def load_data(filename):
    direc = "/Users/annaho/Data/Second_Year_Proj"
    inputf = direc + "/" + filename # (07:53:50, +42:42:22)
    dat = np.loadtxt(inputf)
    wl = dat[:,0] # wavelength
    flux = dat[:,1] # flux
    err = dat[:,3] # flux uncertainty
    return wl, flux, err


def plot_spectrum(wl, flux, ivar, min_wl, max_wl):
    err = 1/np.sqrt(ivar)
    fig = plt.figure(figsize=(10,4))
    plt.step(wl, flux, where='mid', c='k', lw=0.5, label='_none')
    #plt.fill_between(wl, flux-err, flux+err, color='k', alpha=0.2)
    choose = np.logical_and(wl > min_wl, wl < max_wl)
    plt.ylim(min(flux[choose]), max(flux[choose]))
    plt.xlim(min_wl, max_wl)
    plt.xlabel("Wavelength $\lambda (\AA)$", fontsize=20)
    plt.ylabel("Flux [erg/s/cm${}^2/\AA$]", fontsize=20)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.tight_layout()
    return fig


def fit_gaussian(x, y, center):
    g1 = models.Gaussian1D(amplitude=-1., mean=center, stddev=1.)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g1, x, y)
    print(g)
    xvals = np.linspace(min(x), max(x), 1000)
    return xvals, g(xvals)+1


def fit_double_gaussian(x, y, mean1, mean2):
    g1 = models.Gaussian1D(amplitude=-1., mean=mean1, stddev=1.)
    g2 = models.Gaussian1D(amplitude=-1., mean=mean2, stddev=1.)
    g_init = g1 + g2
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, x, y)
    print(g)
    xvals = np.linspace(min(x), max(x), 1000)
    return xvals, g(xvals)+1


if __name__=="__main__":
    min_wl = 5390
    max_wl = 5540
    #filename = "lrisShri_galA.spec" # (07:53:50, +42:42:22)
    filename = "lrisAnna_gal_08.0.spec"
    wl, flux, err = load_data(filename) 
    ivar = 1/err**2
    n_flux, n_ivar = normalize(wl, flux, ivar, L=40)
    choose = np.logical_and(wl > min_wl, wl < max_wl)
    xvals, gaus = fit_gaussian(wl[choose], n_flux[choose]-1, 5460)

    #plot_spectrum(wl, flux, ivar, min_wl, max_wl)
    plt.step(wl, n_flux, where='mid', c='k', lw=0.5)
    plt.step(xvals, gaus, where='mid', c='r', lw=1)
    plt.xlabel("Wavelength", fontsize=16)
    plt.ylabel("Flux", fontsize=16)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlim(min_wl, max_wl)
    plt.ylim(-1, 7)
    plt.tight_layout()
    #plt.show()
    plt.savefig("gal2_fit_oii.png")
    # 
    
