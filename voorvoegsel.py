"""
voorvoegsel.py

Dit voorbeeldje laat zien hoe je strings aan elkaar kunt plakken.

Created on Wed Dec  6 11:23:05 2023
"""

firstname = input("Wat is je voornaam? ")
tussenvoegsel = input("Wat is je tussenvoegsel (optioneel)? ")
lastname = input("Wat is je achternaam? ")

# Voor nu hebben we een dubbele spatie als iemand geen tussenvoegsel in de naam heeft zitten :(
name = firstname + ' ' + tussenvoegsel + ' ' + lastname
print(name)
