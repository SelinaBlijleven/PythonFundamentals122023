"""
if-elif-else.py

Demonstratie van de mogelijkheden van de if/elif/else.

If/elif/else is met name geschikt op het moment dat we
kijken naar meerdere mogelijke waarden voor een variabele.
Als we bijvoorbeeld al weten dat maand 1 vertaalt naar Januari,
hoeven we uiteraard de andere maanden niet meer te checken.
"""

# Uit de datetime module importeren we de klasse datetime.
# Dit is een representatie van een datum + tijd.
from datetime import datetime

# Format (nodig voor datetime)
# Deze wordt even opgeslagen in een variabele, zodat we dit niet apart
# hoeven te typen voor elke datum. Ze zijn immers allemaal met dezelfde format
# opgeslagen.
f = '%d-%m-%Y'

# Datums kunnen we het beste gebruiken i.c.m. de datetime module.
# We stellen nu een datum in, zodat we straks met de datetime module
# kunnen bepalen welke naam van de maand daarbij hoort.
datum = datetime.strptime('06-05-2023', f)

# We beginnen met if; is de maand de eerste?
if datum.month == 1:
    print("Januari")
# Dit checken we alleen als de datum niet in Januari is.
elif datum.month == 2:
    print("Februari")
# Dit checken we alleen als de datum niet in Januari of Februari is.
elif datum.month == 3:
    print("Maart")
# Etc...
elif datum.month == 4:
    print("April")
elif datum.month == 5:
    print("Mei")
elif datum.month == 6:
    print("Juni")
elif datum.month == 7:
    print("Juli")
else:
    # De rest van de maanden wordt hier herkent.
    # Als datum.month een andere waarde dan 1-12 zou kunnen
    # hebben, zou die waarde ook deze conditie vervullen.
    print("Datum is na Juli")
