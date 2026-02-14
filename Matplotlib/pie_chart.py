import matplotlib.pyplot as plt

# Today we will learn about pie chart in matplotlib.

hours = [8, 9, 2, 5]
activity = ['Sleep', 'Work', 'Eating', 'Free time']
plt.title("Day-to-day life")
plt.pie(hours,
        explode=[0.1, 0, 0, 0],
        labels=activity,
        autopct="%1.1f%%",
        colors=["r", 'g', 'b', 'y'],
        shadow=True,
        wedgeprops={'edgecolor': 'k', 'linestyle': '--', 'linewidth': 1},
        startangle=90)
plt.show()

# Here,
# explode : used to highlight a particular piece

# shadow: used to toggle 3d shadow

# wedgeprops: key:value pairs given as args to customise the chart. To know more; search online.

# autopct: toggle percentages

# colors: customise the pieces' colors.

# startangle: used to rotate the pie chart. You can imagine it as a circle's straight radius on the right side and use it as the basis to rotate.

# labels: legend
