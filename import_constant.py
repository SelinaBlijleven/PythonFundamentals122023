"""
import_constant.py

In dit bestandje importeren we een constante uit een ander
bestand en gebruiken we deze om een vergoeding te berekenen.

Created on Wed Dec  6 11:03:40 2023
"""

# Haal de kilometervergoeding uit de configuratie
# (hoofdletters geven aan dat dit een constante is)
from config import KM_VERGOEDING

def bereken_vergoeding(kms):
    '''
    Bereken de vergoeding aan de hand van het aantal kilometers.

    :param  kms:        Het aantal kilometers
    :return vergoeding: De totale vergoeding voor het gereden stuk
    '''
    vergoeding = kms * KM_VERGOEDING
    print(f"Je vergoeding is: {vergoeding}")
    return vergoeding

# Bereken de vergoeding voor 60 km rijden.
bereken_vergoeding(60)

# Eventueel kun je de functie ook zo aanroepen, om bijvoorbeeld
# duidelijker te maken welke informatie je doorgeeft.
# bereken_vergoeding(kms=40)