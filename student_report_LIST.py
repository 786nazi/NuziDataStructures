# Sample data for students
students_data = [
    {"name": "Alice", "roll_no": 1, "marks": [85, 90, 88]},
    {"name": "Bob", "roll_no": 2, "marks": [78, 82, 80]},
    {"name": "Charlie", "roll_no": 3, "marks": [92, 95, 93]},
    {"name": "David", "roll_no": 4, "marks": [35, 40, 38]},
    {"name": "Eva", "roll_no": 5, "marks": [45, 48, 49]}
]
# Function to calculate grade based on average marks
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average < 40:
        return 'D (Fail)'
    elif average < 50:
        return 'C'
    elif average <= 70:
        return 'B'
    else:
        return 'A'

# Using list comprehension to create a list of formatted student details with grades
formatted_students = [
    f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}, Grade: {calculate_grade(student['marks'])}"
    for student in students_data
]

# Print the formatted student details
for student in formatted_students:
    print(student)
