import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = "DailyActivities.xlsx"
df = pd.read_excel(file_path)

# Set the position of bar on X axis
barWidth = 0.25
r1 = range(len(df))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Create the plot
plt.figure(figsize=(12, 8))

# Plot bars with new colors
plt.bar(r1, df['Charles'], color='#4c72b0', width=barWidth, edgecolor='grey', label='Charles')
plt.bar(r2, df['Henry'], color='#55a868', width=barWidth, edgecolor='grey', label='Henry')
plt.bar(r3, df['Susan'], color='#c44e52', width=barWidth, edgecolor='grey', label='Susan')


# Add xticks on the middle of the group bars
plt.xlabel('Area of Interest', fontweight='bold', fontsize=14)
plt.xticks([r + barWidth for r in range(len(df))], df['Area of Interest'], fontsize=12)
plt.yticks(fontsize=12)

# Adding the legend and title
plt.title('Comparison of Daily Activities', fontweight='bold', fontsize=16)
plt.legend(fontsize=12)

# Improve layout and show the plot
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("Daily_Activities_Bar_Chart.png", dpi=300)
plt.show()
