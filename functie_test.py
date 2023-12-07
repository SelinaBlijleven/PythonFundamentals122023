"""
functie_test.py

Het volgende bestand bevat een testje voor een functie,
gebaseerd op de scope van variabelen in python.
"""
# Dit is een globale variabele
a = 5


def kwadraat(a):
    """
    Bereken het kwadraat van een gegeven getal.py

    :param  a:  Getal
    :return     Kwadraat
    """
    return a * a


def kwadraat_globaal():
    """
    Bereken het kwadraat op basis van de waarde
    van variabele a in de globale scope.
    """
    # Het zou netter zijn om hier even duidelijk aan te geven dat we
    # een globale variabele gebruiken, maar de code werkt ook zonder.
    # global a

    return a * a


# We geven het getal 6 direct mee, dus de functie berekent deze op
# basis van het getal 6.
print(kwadraat(6))

# We geven geen getal mee. Variabele a bestaat wel, dus gelukkig krijgen we geen error.
# Wel kan het resultaat er wat onverwacht uitzien.
print(kwadraat_globaal())
