# # Initialize an empty list to store student names and scores
# students = []

# # Number of students
# n = int(input("Enter the number of students: "))

# # Loop to get student names and scores from the user
# for _ in range(n):
#     name = input("Enter student's name: ")
#     score = int(input(f"Enter {name}'s score: "))
#     percentage=float(input(f"enter the {name}'s percentage: "))
#     students.append((name, score,percentage))
# print(students)

# # Print the list of students and their scores
# for name, score,percentage in students:
#     print(f"Student: {name}, Score: {score}, percentage: {percentage}")
def above_average_students(s,avg):
    for name,score in s:
        if score>avg:
            print(f"student {name} is above average student")
        else:
            print(f"student {name} is below average student")

students=[]
n=int(input("Enter the number of students: "))
for _ in range(n):
    name=input("Enter student's name: ")
    score=float(input(f"enter {name}'s score: "))
    students.append((name,score))
print(students)
average_score=float(input("enter the avergae score: "))
above_average_students(students,average_score)
