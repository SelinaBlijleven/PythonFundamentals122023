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