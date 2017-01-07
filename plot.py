import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font', family='serif')
rc('text', usetex=True)

def plot(wl, flux, ivar):
    fig = plt.figure(figsize=(8,6))
    plt.step(wl, flux, c='k', where='mid', lw=0.5)
    plt.xlabel(r"Wavelength $\lambda (\AA)$")
    plt.ylabel("Flux")
    return fig
