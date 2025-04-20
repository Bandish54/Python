import numpy as np


num_subjects = int(input("Enter the number of subjects: "))

subject_names = []
for i in range(num_subjects):
    name = input(f"Enter the name of subject {i + 1}: ")
    subject_names.append(name)


marks = []
print("\nEnter the marks for each subject:")
for i in range(num_subjects):
    mark = float(input(f"{subject_names[i]}: "))
    marks.append(mark)


marks_array = np.array(marks)

average = np.mean(marks_array)
highest = np.max(marks_array)
lowest = np.min(marks_array)
highest_subject = subject_names[np.argmax(marks_array)]
lowest_subject = subject_names[np.argmin(marks_array)]


print("\n--- Student Marks Analysis ---")
for i in range(num_subjects):
    print(f"{subject_names[i]}: {marks[i]}")

print(f"\nAverage Marks: {average:.2f}")
print(f"Highest Marks: {highest} in {highest_subject}")
print(f"Lowest Marks: {lowest} in {lowest_subject}")
