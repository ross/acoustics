#
#
#

from os import listdir
from os.path import join

import numpy as np
from scipy.io.wavfile import read


def rew_measurements(directory):
    measurements = {}
    for filename in listdir(directory):
        if not filename.endswith('.txt') or filename.startswith('RT60_'):
            continue
        with open(join(directory, filename)) as fh:
            line = fh.readline()
            while line.startswith('*'):
                line = fh.readline()
            freq = []
            spl = []
            phase = []
            for line in fh:
                d = line.split()
                f = float(d[0])
                freq.append(f)
                spl.append(float(d[1]))
            key = filename.replace('.txt', '')
            measurements[key] = {
                'freq': np.array(freq),
                'spl': np.array(spl),
                'phase': np.array(phase),
            }

    return measurements


def rew_rt60s(directory):
    rt60s = {}
    for filename in listdir(directory):
        if not filename.startswith('RT60_'):
            continue
        with open(join(directory, filename)) as fh:
            freqs = []
            edts = []
            topts = []
            for line in fh.readlines()[14:-3]:
                freq, bw, _, edt, t20, _, t30, _, topt, _ = line.split(" ", 9)
                freqs.append(int(freq))
                edts.append(float(edt))
                topts.append(float(topt))

        key = filename.replace('RT60_', '').replace('.txt', '')
        rt60s[key] = {
            'freq': np.array(freqs),
            'edt': np.array(edts),
            'topt': np.array(topts),
        }

    return rt60s


def rew_impulses(directory, threshold=0.25):
    impulses = {}
    
    for filename in listdir(directory):
        if not filename.endswith('.wav'):
            continue
        rate, data = read(join(directory, filename))
        key = filename.replace('.wav', '')
        try:
            # drop to mono if it happens to be stereo
            data = data[:,0]
        except IndexError:
            pass

        # find the max value (positive or negative) for the impulse
        data_abs = abs(data)
        data_max = max(data_abs)
        # use that max to normalize the absolute data
        data_abs_norm = data_abs / data_max
        # and then find the point at which we cross the threshold, our start
        start = np.argmax(data_abs_norm>=threshold)

        # normalize
        data = data / data_max
        
        impulses[key] = {
            'rate': rate,
            'data': data,
            'start': start,
        }

    return impulses