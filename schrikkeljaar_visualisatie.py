"""
schrikkeljaar_visualisatie.py

Het volgende script was voornamelijk bedoeld om de antwoorden op
de schrikkeljaar-vraag te kunnen valideren. Je kunt deze wel draaien,
maar de grafiek ziet er niet heel overzichtelijk uit.

Known issues:
- Er staat True/False onderin de grafiek alsof het een bar graph is. Dit kun je negeren.
"""

import calendar

# Data science libraries:
# - Pandas voor dataverwerking
# - Matplotlib voor plotten
# - Seaborn als extensie voor het plotten
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stel de seaborn stijl in
sns.set(style="whitegrid")

# Begin- en eindjaar
MIN_YEAR = 2000
MAX_YEAR = 2031

years = list(range(MIN_YEAR, MAX_YEAR))
data = pd.DataFrame({'Year': years, 'LeapYear': [calendar.isleap(year) for year in years]})

# Set up Seaborn style
# Reshape the DataFrame for heatmap
heatmap_data = data.pivot_table(index='Year', columns='LeapYear', aggfunc=len, fill_value=0)

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cbar=False)

# Customize the plot
plt.title('Welke jaren zijn schrikkeljaren?')
plt.ylabel('Jaar')

# Show the plot
plt.show()