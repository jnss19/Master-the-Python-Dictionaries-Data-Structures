# Creating a dictionary of students and their grades
students_grades = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B+',
    'Student5': 'C-'
}

print("Students and their grades:", students_grades)


print("Grade of third student:", students_grades['Student3'])

students_grades['Student2'] = 'A'

del students_grades['Student5']

print("Last key-value pair in the dictionary:", list(students_grades.items())[-1])
