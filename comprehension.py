from schrikkeljaar import leap_year

jaren = list(range(2000, 2031))

# Comprehension
schrikkeljaren = [jaar for jaar in jaren if leap_year(jaar)]

# Zonder comprehension
# Eerst een lege array aanmaken
schrikkeljaren2 = []

# Loop over alle jaren
for jaar in jaren:
    # Is het een schrikkeljaar?
    if leap_year(jaar):
        # Voeg dan toe aan de lijst met schrikkeljaren
        schrikkeljaren2.append(jaar)