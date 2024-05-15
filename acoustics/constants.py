#
#
#

import numpy as np

speed_of_sound = 343
beta = 1.5 / 1.7
rho = 1.1839

gas_constant = 287.05  # J Kg-1 °K-1
one_atmosphere = 101325  # Pa
air_density_at_0 = 1.293  # Kg m-3, Kinsler & Frey, Appendix A10, Table (c)
gamma = 1.402  # Kinsler & Frey, Appendix A10, Table (c)
air_viscosity = 0.00001850  # m2s-1
air_thermal_conductivity = 0.0241
air_specific_heat = 1.01

primes = np.array(
    (
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    )
)