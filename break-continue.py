"""
break-continue.py

Dit script laat het verschil tussen continue en break zien.
"""

# We stellen een magisch getal in om naar te zoeken
magicnumber = 11

# Loop over de getallen van 1-20
for i in range(1, 21):
    # Zitten we nu op het magische getal?
    if i == magicnumber:
        # Beëindig de loop.
        break
    # Print de getallen zodat we goed kunnen zien wat er gebeurt :)
    print(f"Loop met break: {i}")

# Loop over de getallen van 1-20
for i in range(1, 21):
    # Zitten we nu op het magische getal?
    if i == magicnumber:
        # Ga naar de volgende iteratie
        # (Dus ga verder bij het volgende getal)
        continue
    print(f"Loop met continue: {i}")

