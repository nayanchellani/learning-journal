import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [10, 29, 34, 48, 53, 60, 75, 89]
plt.scatter(hours_studied, scores, color="green", marker='o', label="study hours analysis")
plt.xlabel("Hours Studied")
plt.ylabel("Scores per study hour")
plt.title("Student study hours analysis")
plt.legend()
plt.grid(True)
plt.show()