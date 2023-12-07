"""
schrikkeljaar.py

Dit bestand vergelijkt een eigen implementatie van leap year met
de ingebouwde versie.

Wil je je eigen code testen? Vervang de code in leap_year (de functie) dan door
je eigen code.
"""
# Werken met kalenderdata
import calendar


def leap_year(year):
    '''
    Bepaal of een gegeven jaar een schrikkeljaar is.

    Deze code kun je vervangen door je eigen code, om te testen of
    deze het juiste resultaat geeft.

    Let op! Als je functie geen True/False teruggeeft, kan de test
    niet succesvol runnen.

    :param:     int     Jaartal
    :return:    bool    Schrikkeljaar?
    '''
    if year % 4 != 0:
        return False

    return year % 400 == 0 or year % 100 != 0


def main():
    # Maak een lijst met alle jaren tussen het jaar 1900 en 2030 (het eindgetal zelf, 2031 in dit geval, telt niet mee!)
    years = list(range(1900, 2031))

    # Vraag alle schrikkeljaren op met de ingebouwde methode uit de calendar-package.
    leap_years_cal = [year for year in years if calendar.isleap(year)]
    # Vraag alle schrikkeljaren op met je eigen methode (zo lang deze maar leap_year heet)!
    leap_years = [year for year in years if leap_year(year)]

    # Test of de functie die we zelf hebben geschreven werkt.
    # Assert geeft aan dat we in dit geval dezelfde lijsten horen te krijgen.
    assert leap_years_cal == leap_years

    print("Test geslaagd! :)")


if __name__ == "__main__":
    main()
