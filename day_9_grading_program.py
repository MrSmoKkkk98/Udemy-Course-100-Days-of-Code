student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if student_scores[score] > 90:
        student_scores[score] = "Outstanding" 
    elif student_scores[score] > 80:
        student_scores[score] = "Exceeds Expectations"
    elif student_scores[score] > 70:
        student_scores[score] = "Acceptable"
    else:
        student_scores[score] = "Fail" 
student_grades = student_scores        
# 🚨 Don't change the code below 👇
print(student_grades)
