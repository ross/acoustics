#
#
#

import numpy as np

from acoustics.constants import (
    air_density_at_0,
    gamma,
    gas_constant,
    one_atmosphere,
    speed_of_sound,
)

# These are currently focused on materials with easy access (available for purchase locally) the data for them comes
# https://www.bobgolds.com/AbsorptionCoefficients.htm
materials = {
    
    "JM R-11": {
        # R-11 FG Batts https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 1720,
        "thickness": 3.5 * 0.0254,
    },
    "JM R-19": {
        # R-19 FG Batts https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 1674,
        "thickness": 6.5 * 0.0254,
    },
    "JM R-21": {
        # R-21 FG Batts https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 7901,
        "thickness": 5.5 * 0.0254,
    },
    "JM R-30": {
        # R-30 https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 1850,
        "thickness": 10.25 * 0.0254,
    },

    "OC EcoTouch R-11": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 2450,
        "thickness": 3.5 * 0.0254,
    },

    "OC EcoTouch R-13": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 3500,
        "thickness": 3.5 * 0.0254,
    },

    "OC EcoTouch R-15": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 5000,
        "thickness": 3.5 * 0.0254,
    },

    "OC EcoTouch R-19": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 2900,
        "thickness": 6.5 * 0.0254,
    },

    # "OC EcoTouch R-34.2*": {
    #     # R-19 * 1.8
    #     "sigma": 2900,
    #     # this is a handmade fill pulling apart a 2nd layer to make something exactly 12" thick
    #     "thickness": 12 * 0.0254,
    # },

    # https://www.rockwool.com/north-america/products-and-applications/products/safensound/
    'RW Safe n Sound 3"': {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 10000,
        "thickness": 3 * 0.0254,
        # https://www.rockwool.com/siteassets/o2-rockwool/documentation/technical-data-sheets/residential/safensound-fire-and-soundproofing-insulation-techdata.pdf
        "a": {
            125: 0.52,
            250: 0.96,
            500: 1.18,
            1000: 1.07,
            2000: 1.05,
            4000: 1.05,
        },
        "nrc": 1.05,
    },
    'RW Safe n Sound 6"': {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 10000,
        "thickness": 6 * 0.0254,
        # https://www.rockwool.com/siteassets/o2-rockwool/documentation/technical-data-sheets/residential/safensound-fire-and-soundproofing-insulation-techdata.pdf
        "a": {
            125: 1.11,
            250: 1.28,
            500: 1.15,
            1000: 1.06,
            2000: 1.03,
            4000: 1.01,
        },
        "nrc": 1.15,
    },

    # https://www.owenscorning.com/en-us/insulation/products/thermafiber-fire-and-sound-guard-plus
    "OC Fire & Sound Plus R-15": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 20000,
        "thickness": 3.5 * 0.0254,
        # https://dcpd6wotaa0mb.cloudfront.net/mdms/dms/EIS/10025220/10025220-Thermafiber-Fire-and-Sound-Guard-Plus-PDS.pdf?v=1685984089000
        "a": {
            125: 0.51,
            250: 1.28,
            500: 1.21,
            1000: 1.13,
            2000: 1.07,
            4000: 1.03,
        },
        "nrc": 1.15,
    },
    "OC Fire & Sound Plus R-21": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 20000,
        "thickness": 5.5 * 0.0254,
        # https://dcpd6wotaa0mb.cloudfront.net/mdms/dms/EIS/10025220/10025220-Thermafiber-Fire-and-Sound-Guard-Plus-PDS.pdf?v=1685984089000
        "a": {
            125: 0.76,
            250: 1.33,
            500: 1.17,
            1000: 1.11,
            2000: 1.04,
            4000: 1.01,
        },
        "nrc": 1.15,
    },
    "OC Fire & Sound Plus R-30": {
        # https://docs.google.com/spreadsheets/d/19q-20qTpKV5g12PiSc1gNrJlG8DYrtqaFeFoYUCxC68/edit#gid=861262967
        "sigma": 20000,
        "thickness": 7.125 * 0.0254,
        # https://dcpd6wotaa0mb.cloudfront.net/mdms/dms/EIS/10025220/10025220-Thermafiber-Fire-and-Sound-Guard-Plus-PDS.pdf?v=1685984089000
        "a": {
            125: 0.79,
            250: 1.15,
            500: 1.15,
            1000: 1.10,
            2000: 1.07,
            4000: 1.04,
        },
        "nrc": 1.10,
    },
}


def porous_absorber(
    frequencies,
    sigma,
    thickness,
    air_gap,
    angle=0,
    air_temperature=20.0,
    atmospheric_pressure=1.0,
):

    w = 2.0 * np.pi * frequencies
    two_pi_over_c = 2 * np.pi / speed_of_sound
    kair = two_pi_over_c * frequencies
    air_density = (atmospheric_pressure * one_atmosphere) / (
        gas_constant * (273.15 + air_temperature)
    )
    X = (air_density * frequencies) / sigma
    sound_velocity = np.sqrt((gamma * one_atmosphere) / air_density_at_0) * np.sqrt(
        1 + (air_temperature / 273.15)
    )
    air_impedance = sound_velocity * air_density
    zca = air_impedance * (
        1 + 0.0571 * np.power(X, -0.754) + -0.087j * np.power(X, -0.732)
    )
    k = (
        two_pi_over_c
        * frequencies
        * (1 + 0.0978 * np.power(X, -0.7) + -0.189j * np.power(X, -0.595))
    )
    ky = kair * np.sin(angle * np.pi / 180)
    kx = np.sqrt(k * k - ky * ky)
    bporous = np.arcsin(np.abs(ky / k)) * 180 / np.pi
    k_kx = k / kx
    cot_k_times_ta = np.cos(k * thickness) / np.sin(k * thickness)
    if air_gap == 0:
        # no air gap
        zsa = -1j * zca * k_kx * cot_k_times_ta
        zsa_over_rc_times_cos_y = (zsa / air_impedance) * np.cos(angle * np.pi / 180)
        reflection_factor = (zsa_over_rc_times_cos_y - 1) / (
            zsa_over_rc_times_cos_y + 1
        )
        a = 1 - np.power(np.abs(reflection_factor), 2)
        #             pprint({
        #                 'w': w,
        #                 'kair': kair,
        #                 'X': X,
        #                 'zca': zca,
        #                 'k': k,
        #                 'ky': ky,
        #                 'kx': kx,
        #                 'bporous': bporous,
        #                 'k_kx': k_kx,
        #                 'cot_k_times_ta': cot_k_times_ta,
        #                 'zsa': zsa,
        #                 'zsa_over_rc_times_cos_y': zsa_over_rc_times_cos_y,
        #                 'reflection_factor': reflection_factor,
        #                 'a': a,
        #             })
        return a

    # air gap
    kair_y = k * np.sin(bporous * np.pi / 180)
    kair_x = np.sqrt(np.power(kair, 2) - (kair_y * kair_y))
    bair = np.arcsin(np.abs((kair_y / air_impedance))) * 180 / np.pi
    kair_over_kair_x = kair / kair_x
    zair = (
        -1j
        * air_impedance
        * kair_over_kair_x
        * np.cos(kair * air_gap)
        / np.sin(kair * air_gap)
    )
    inter = -1j * zca * cot_k_times_ta
    za_air = ((inter * zair) + (zca * zca)) / (zair + inter)
    inter2 = (za_air / air_impedance) * np.cos(angle * np.pi / 180)
    overall_reflection_factor = (inter2 - 1) / (inter2 + 1)
    a = 1 - np.power(np.abs(overall_reflection_factor), 2)
    #         pprint({
    #             'w': w,
    #             'kair': kair,
    #             'X': X,
    #             'zca': zca,
    #             'k': k,
    #             'ky': ky,
    #             'kx': kx,
    #             'bporous': bporous,
    #             'k_kx': k_kx,
    #             'cot_k_times_ta': cot_k_times_ta,
    #             'kair_y': kair_y,
    #             'kair_x': kair_x,
    #             'bair': bair,
    #             'kair_over_kair_x': kair_over_kair_x,
    #             'zair': zair,
    #             'inter': inter,
    #             'za_air': za_air,
    #             'inter2': inter2,
    #             'overall_reflection_factor': overall_reflection_factor,
    #             'a': a,
    #         })
    return a