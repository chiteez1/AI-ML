import matplotlib.pyplot as plt

# Today we will learn about scatter plot in matplotlib. It is used to find the relationship between two datasets.

study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores = [40, 45, 50, 55, 60, 65, 75, 85, 90]

# the greater the marks, the bigger the dots
sizes = [x * 2 for x in exam_scores]

# red if marks < 50
colors = ['red' if x < 50 else 'green' for x in exam_scores]

plt.title("Study hours and marks")
plt.scatter(study_hours, exam_scores, s = sizes, c=colors)

# colormap
plt.scatter(study_hours, exam_scores, c=exam_scores, cmap="coolwarm")
plt.colorbar(label = "Scores")  # color legend for reference.

# colors based on another variable:
age = [10, 10, 11, 12, 12, 13, 14, 15, 15]
plt.scatter(study_hours, exam_scores, c=age, cmap="coolwarm")

# annotate
for i in range(len(exam_scores)):
    plt.annotate(exam_scores[i], (study_hours[i] + 0.1, exam_scores[i] - 2))

plt.xlabel('Hours')
plt.ylabel('Marks')
plt.show()

# multiple plots: It produces a generalised xy axis and then plots both of them.
class_a_hours = [2, 4, 6, 8]
class_a_scores = [45, 55, 65, 85]
class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 90]
plt.scatter(class_a_hours, class_a_scores, color='red', label = 'Class A')
plt.scatter(class_b_hours, class_b_scores, color='blue', label = 'Class B')
plt.legend()
plt.show()