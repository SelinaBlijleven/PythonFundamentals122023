import calendar

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MIN_YEAR = 1900
MAX_YEAR = 2031

years = list(range(1900, 2031))
print(years)
data = pd.DataFrame({'Year': years, 'LeapYear': [calendar.isleap(year) for year in years]})
print(data.head())

# Set up Seaborn style
sns.set(style="whitegrid")

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Year', y='LeapYear', data=data, hue='LeapYear')

# Customize the plot
plt.title('Leap Years Visualization')
plt.xlabel('Year')
plt.ylabel('Leap Year')
plt.yticks([0, 1], ['No', 'Yes'])

# Show the plot
plt.show()