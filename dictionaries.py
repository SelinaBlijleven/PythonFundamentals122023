"""
dictionaries.py

Demo van dictionaries in Python
"""
# Standaard lijst, kan verschillende soorten
# waarden bevatten. We hebben alleen geen labels,
# waardoor we nu niet direct kunnen zien wat elke
# waarde representeert.
# (overigens is de variabelenaam ook erg onduidelijk)
lst = [123, "Ruben", "9", "8"]

# Dezelfde informatie kunnen we opslaan in een dictionary;
# daarbij maken we gebruik van key-value pairs. Je kunt
# dit ook zien als paren van waarden en labels daarvoor.
student = {
    'studentnummer': 123,
    'naam': "Ruben",
    'leeftijd': 9,
    'cijfer_wiskunde': 8
}

# Het verschil in de leesbaarheid van de code wordt
# snel duidelijk zodra we de naam van de student opvragen.
print(f"De student heet: {lst[1]}")
print(f"De student heet: {student['naam']}")