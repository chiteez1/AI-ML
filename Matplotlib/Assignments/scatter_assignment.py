import matplotlib.pyplot as plt

# 1.
# Dataset 1: Study hours and exam scores
study_hours = [2, 3, 4, 5, 6, 7, 8]
exam_scores = [45, 55, 65, 70, 75, 85, 90]


# Plot a scatter plot:
# X-axis: study_hours
# Y-axis: exam_scores
# Use cmap='plasma' or 'inferno' to color the points based on exam scores.
# Add a colorbar that shows what the colors mean.
# Use s=100 to make points more visible.

plt.scatter(study_hours, exam_scores, c=exam_scores, cmap='coolwarm', s=100)
plt.colorbar(label = 'Score')
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()  


# 2.
# Dataset 2: City area and population
cities = ["City A", "City B", "City C", "City D", "City E"]
city_area = [600, 850, 1200, 400, 950]  # in km²
city_population = [3.2, 5.5, 8.0, 2.5, 6.3]  # in millions

# Create a scatter plot of area vs population.
# Annotate each point with the city name using plt.annotate().
# Use a consistent color (e.g., blue) for all points.
# Make sure annotations don't overlap - optionally, add some xytext offset.

plt.title("Area vs population")
plt.scatter(city_area, city_population, color = 'blue')
for i in range(len(cities)):
    plt.annotate(cities[i], (city_area[i] + 0.1, city_population[i]))
plt.show()


# 3.
# Dataset 3: Exam scores for multiple subjects
students = ["A", "B", "C", "D", "E", "F"]
math_scores    = [80, 60, 90, 55, 70, 85]
science_scores = [75, 65, 88, 60, 68, 80]
english_scores = [85, 70, 82, 58, 75, 78]

# Create a scatter plot with:
# X-axis: student number or name.
# Y-axis: score
# Plot three groups: Math, Science, and English.
# Use different colors or markers for each subject.
# Add a legend to identify the groups.
# Optional: Add titles and labels for clarity.

plt.title("Students and subject marks")
plt.scatter(students, math_scores, color = 'red', label = "Math")
plt.scatter(students, science_scores, color = 'green', label = "Science")
plt.scatter(students, english_scores, color = 'blue', label = "English")
plt.xlabel("Name")
plt.ylabel("Scores")
plt.legend()
plt.show()
