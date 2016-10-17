""" Normalize a spectrum """


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
