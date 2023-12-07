"""
while_demo.py

Demonstratie van een while loop. Een while-loop gebruiken we in situaties
waar we een onbekend aantal iteraties gaan maken.

In dit geval passen we de while-loop toe om te zorgen
dat we altijd een geldige leeftijd ontvangen van de gebruiker.
"""

geldige_waarde = False

while not geldige_waarde:
    # Vraag om een leeftijd
    leeftijd = input("Wat is je leeftijd? ")

    # Is de leeftijd numeriek (dus geldig)
    if leeftijd.isnumeric():
        leeftijd_int = int(leeftijd)
        geldige_waarde = True
    else:
        print("Dat is geen geldige leeftijd.")