"""
if-else.py

Demonstratie van een if/else statement (en genestte if/else-statements).
Een genestte if/else is een if/else-blok dat binnen een ander if/else-blok staat.
In principe kun je zoveel if/else blokken in elkaar passen als je zou willen,
de limiterende factor hier is je computer.
"""

# Eerst vragen we de gebruiker om een leeftijd.
# We slaan deze eerst op als string.
age_str = input("Wat is je leeftijd? ")

# Met de isnumeric()-functie voor strings kunnen we checken
# of de string veilig om te zetten is naar een getal!
if age_str.isnumeric():

    # We kunnen er nu veilig een getal van maken.
    age_int = int(age_str)

    # Nu kunnen we ook wat informatie voor de gebruiker printen.
    # Omdat dit blok (met if/else) binnen de eerste if-statement staat,
    # wordt deze code alleen uitgevoerd als er een geldige leeftijd is ingevoerd.
    if age_int > 18:
        print("Je bent volwassen!")
    else:
        print("Je bent minderjarig")
# Dit is de else die bij isnumeric hoort. We komen hier dus uit als de gebruiker
# iets anders dan een getal heeft ingevoerd.
else:
    print("Dat is geen geldige leeftijd.")