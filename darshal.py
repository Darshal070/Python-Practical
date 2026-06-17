# matplotlib_graph.py

import matplotlib.pyplot as plt

# Sample data
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 90, 78, 88, 95]

# Line Graph
plt.figure(figsize=(6, 4))
plt.plot(subjects, marks, marker='o', color='blue')
plt.title("Student Marks (Line Graph)")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


# Bar Graph
plt.figure(figsize=(6, 4))
plt.bar(subjects, marks, color='green')
plt.title("Student Marks (Bar Graph)")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


# Pie Chart
plt.figure(figsize=(6, 4))
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution (Pie Chart)")
plt.show()
