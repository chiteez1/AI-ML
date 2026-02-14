import matplotlib.pyplot as plt

# 1.
# Data:
platforms = ['Instagram', 'Facebook', 'Twitter', 'LinkedIn']
votes = [40, 30, 20, 10]

# Task:
# Plot a pie chart showing:
# - Each platform as a labeled slice
# - Percentage values on each slice

plt.title("I am too lazy for titles")
plt.pie(votes, labels=platforms, autopct="%1.1f%%")
plt.show()

# 2.
# Data:
activities = ['Sleep', 'School', 'Homework', 'Free Time']
hours = [8, 7, 3, 6]

# Task:
# Create a pie chart that:
# - Explodes the "School" slice to emphasize it
# - Includes percentage, labels
# - Has a shadow for visual depth

plt.title("I will do it in the next question. I promise!")
plt.pie(hours, labels=activities, autopct="%1.1f%%", explode=[0, 0.1, 0, 0], shadow=True)
plt.show()


# 3.
# Data:
departments = ['HR', 'IT', 'Marketing', 'Logistics']
budget = [25, 35, 20, 20]

# Task:
# Plot a pie chart with:
# - Custom colors (any four distinct ones)
# - A start angle of 90 degrees (so the first slice starts from the top)
# - Percentage, labels

plt.title("Department-wise budget. I am a man of my words")
plt.pie(budget, colors=['r', 'g', 'b', 'y'], startangle=90, labels=departments, autopct="%1.1f%%")
plt.show()
