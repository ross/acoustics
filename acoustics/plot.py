#
#
#

import matplotlib.pyplot as plt
import numpy as np


def plot(f, data, title=None, loc=None, legend=True, vline=None, height=6, width=12, xscale='log'):
    fig = plt.figure()
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax = fig.add_subplot()

    for name, d in data.items():
        n = len(d)
        if n == 3 and isinstance(d[2], dict):
            ax.plot(d[0], d[1], label=name, **d[2])
        elif len(d) == 2:
            ax.plot(*d, label=name)
        else:
            ax.plot(f, d, label=name)

    if vline is not None:
        ax.axvline(vline)
    
    ax.set_xscale(xscale)
    if legend:
        ax.legend(loc=loc or 'upper right')
    if title:
        ax.set_title(title)

    xt = [10, 20, 40, 60, 80, 100, 140, 200, 400, 800, 1600, 3200, 6400, 12800, 20000]
    xt = [i for i in xt if f[0] <= i and i <= f[-1]]
    ax.set_xticks(xt)
    xticklabels = [f'{i:d}' for i in xt]
    ax.set_xticklabels(xticklabels)

    return ax

def compare(f, a_name, a, b_name, b, title, vline=None):
    ax1 = plot(f, {
        a_name: a,
        b_name: b,
    }, title, loc='lower left', vline=vline)
    ax2 = plot(f, {
        'diff': a - b,
    }, 'Difference', legend=False, vline=vline)
    return ax1, ax2


def plot_impulse_responses(rate, data, title, tmax=1.0, loc=None, legend=True, height=6, width=12):
    fig = plt.figure()
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax = fig.add_subplot()

    n = int(rate * tmax + 0.5)
    for name, d in data.items():
        ax.plot(d[:n], label=name)

    if legend:
        ax.legend(loc=loc or 'upper right')
    if title:
        ax.set_title(title)
    
    xt = np.arange(0, n + 0.00001, rate * tmax / 10.0)
    ax.set_xticks(xt)
    xticklabels = np.arange(0, tmax + 0.00001, tmax / 10.0)
    ax.set_xticklabels(xticklabels)

    return ax

def compare_impulse_responses(rate, a_name, a, b_name, b, title, tmax=1.0):
    ax1 = plot_impulse_responses(rate, {
        a_name: a,
        b_name: b,
    }, title, tmax=tmax, loc='lower left')