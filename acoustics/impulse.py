#
#
#

from IPython.display import Audio
import numpy as np
from scipy.signal import fftconvolve


def convolve(sound, impulse_response):
    out_l = fftconvolve(sound[:, 0], impulse_response)
    out_r = fftconvolve(sound[:, 1], impulse_response)
    return np.vstack((out_l / max(out_l), out_r / max(out_r)))


def convolve_display(sound, rate, impulse_response):
    return Audio(convolve(sound, impulse_response), rate=rate)