"""
comprehension.py

Dit bestand bevat een voorbeeldscriptje voor een stukje list comprehension.
"""
# In schrikkeljaar heb ik een functie geschreven om schrikkeljaren
# te berekenen, dus die kan ik hier simpelweg weer importeren.
from schrikkeljaar import leap_year

# Maak een lijst van getallen binnen de gegeven range.
# We zetten deze range wel nog om naar een lijst, omdat
# dit een generator object is. Om alle waarden in een lijst te krijgen
# hebben we dus de list() functie nodig.
jaren = list(range(2000, 2031))

# Maak een lijst aan, waarin we alle jaartallen toevoegen
# die in onze lijst met jaren staan, én een schrikkeljaar zijn.
schrikkeljaren = [jaar for jaar in jaren if leap_year(jaar)]

'''
Equivalent zonder comprehension
'''
# Eerst een lege array aanmaken
schrikkeljaren2 = []

# Loop over alle jaren
for jaar in jaren:
    # Is het een schrikkeljaar?
    if leap_year(jaar):
        # Voeg dan toe aan de lijst met schrikkeljaren.
        # Hier hebben we dus de append-functie voor nodig, terwijl
        # dat hierboven niet het geval is.
        schrikkeljaren2.append(jaar)

# Beide implementaties gedragen zich hetzelfde. Bepaal aan de hand
# van het gemak waarmee je code schrijft en de leesbaarheid welke
# optie het meest geschikt is.