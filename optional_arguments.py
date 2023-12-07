"""
optional_arguments.py

Deze code komt grotendeels uit het boek "A crash course in Python".
"""

def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print("\nFlight booked from %s to %s" % (fromairport, toairport))
    print("Number of adults: %d" % numadults)
    print("Number of children: %d" % numchildren)

# Roep de functie aan met alle argumenten
book_flight("BRS", "VER", 2, 2)

# Roep de functie aan met alleen een gegeven aantal volwassenen
# Let op: dit kan dus alleen als de volwassenen het eerste optionele argument zijn.
book_flight("LHR", "VIE", 4)

# Boek een vlucht met de standaardwaarden.
book_flight("LHR", "OSL")

# Als we wél het aantal kinderen door willen geven, maar niet het aantal volwassenen
# moeten we duidelijk aangeven dat we alleen een waarde instellen voor kinderen.
book_flight("AMS", "ROT", numchildren=10)
