"""
klinker_comprehension.py

Een onnodig gecompliceerde uitwerking van de klinkeropdracht,
die gebruik maakt van list comprehension om alle klinkers in een tekst
te kunnen tellen in een regel code.


"""

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, " \
        "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. " \
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa " \
        "qui officia deserunt mollit anim id est laborum."

# Tel alle klinkers uit een tekst bij elkaar op en print het resultaat
print(sum(tekst.count(klinker) for klinker in ['a', 'e', 'i', 'o', 'u', 'y']))