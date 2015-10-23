import numpy as np


def gen_rayleigh(sigma=1.0, *args):
    return np.sqrt(sigma/2.0) * np.random.randn(*args) +\
        np.sqrt(sigma/2.0) * np.random.randn(*args) * 1j


def gen_rician(k=10, sigma=1.0, *args):
    return np.sqrt(k/float(k+1))*sigma*np.exp(1j) +\
        np.sqrt((1.0/(k+1))*sigma/2.0) * np.random.randn(*args) +\
        np.sqrt((1.0/(k+1))*sigma/2.0) * np.random.randn(*args) * 1j


def gen_logNshadowing(sigma=4, *args):
    """
    Log-Normal shadowing
    Kwargs:
    sigma (float): dB. std of log noraml
    """
    return sigma * np.random.randn(*args)
