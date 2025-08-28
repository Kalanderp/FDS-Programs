import numpy as np
import matplotlib.pyplot as plt
student_scores = np.array([
    [85, 90, 78, 88],
    [70, 80, 65, 72],
    [92, 88, 95, 90],
    [60, 75, 70, 68]
])  
avg_scores = np.mean(student_scores, axis=0)
subjects = ["Math", "Science", "English", "History"]
highest_subject = subjects[np.argmax(avg_scores)]
print("Average scores per subject:", dict(zip(subjects, avg_scores)))
print("Subject with highest average:", highest_subject)
colors = ['blue','green','orange','red']
highlight_index = np.argmax(avg_scores)
colors[highlight_index] = 'purple'  
plt.bar(subjects, avg_scores, color=colors)
plt.title("Average Scores per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.show()