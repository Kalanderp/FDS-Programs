import numpy as np
import matplotlib.pyplot as plt
attendance_data = np.array([
    [1, 1, 1, 0, 1],  # Student 1
    [1, 0, 1, 1, 1],  # Student 2
    [1, 1, 1, 1, 1],  # Student 3
    [0, 1, 0, 1, 0]   # Student 4
])
total_attendance = np.sum(attendance_data, axis=1)
top_student = np.argmax(total_attendance) + 1
print("Total attendance per student:", total_attendance)
print("Student with highest attendance: Student", top_student)
students = [f"Student {i+1}" for i in range(len(total_attendance))]
colors = ['lightblue', 'lightgreen', 'orange', 'pink']
colors[top_student-1] = 'purple'
plt.pie(total_attendance, labels=students, autopct='%1.1f%%', colors=colors)
plt.title("Student Attendance Distribution")
plt.show()