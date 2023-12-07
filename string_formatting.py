"""
string_formatting.py

Resultaten printen in je terminal op drie manieren :)
"""
a = 5

# Normaal printen (geen variabelen)
print("Hello world")
print(a)

# Printen met concatenation: hierbij mogen we alleen strings (teksten)
# aan elkaar plakken. Variabelen die een getal gebruiken moeten we eerst
# naar een string casten: str(var).
print("Dit is het resultaat van je sommetje: " + str(a))

# Printen met f-strings
# Het formatteren van Strings is de netste manier om resultaten te printen.
# Je kunt de string laten formatteren door een f voor de eerste quote (' of ") te zetten.
print(f"Dit is het resultaat van je sommetje: {a}")

# Er zijn nog veel meer manieren, maar de f-string is over het algemeen de
# meest gebruiksvriendelijke en leesbare manier.
