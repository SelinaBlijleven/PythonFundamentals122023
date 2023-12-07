"""
voorvoegsel.py

Dit voorbeeldje laat zien hoe je strings aan elkaar kunt plakken.

Created on Wed Dec  6 11:23:05 2023
"""

'''
Dag 1
'''
firstname = input("Wat is je voornaam? ")
tussenvoegsel = input("Wat is je tussenvoegsel (optioneel)? ")
lastname = input("Wat is je achternaam? ")

# Voor nu hebben we een dubbele spatie als iemand geen tussenvoegsel in de naam heeft zitten :(
name = firstname + ' ' + tussenvoegsel + ' ' + lastname
print(name)

'''
Dag 2
'''
name_valid = False

# Blijf de gebruiker vragen stellen tot ze een naam invullen.
while not name_valid:
    voornaam = input("Wat is je voornaam? ")
    tussenvoegsel = input("Wat is je tussenvoegsel (optioneel)? ")
    achternaam = input("Wat is je achternaam? ")

    # Check of de voornaam en achternaam niet leeg zijn,
    # dit geeft ons een True/False. Tussenvoegsel checken we niet,
    # deze is namelijk optioneel.
    # In een realistisch scenario wil je misschien ook kijken of de naam
    # lang genoeg is etc.
    name_valid = (voornaam != '' and achternaam != '')

# Is het tussenvoegsel leeg? Dan printen we alleen voornaam en achternaam
if (tussenvoegsel == ''):
    print(f"{voornaam} {achternaam}")
else:
    print(f"{voornaam} {tussenvoegsel} {achternaam}")
