#creates the grades file and questions the user for the
#data of each student

import csv
#this function questions the user about the student's
#information and stores it inside the file grades.csv
def writeGrades():
#creates the file grades.csv
    filename = "grades.csv"

 # gathers the number of students
    numStudents = input("Enter the number of students: ")
    while not numStudents.isdigit():
        print("PLease enter a number.")
        numStudents = input("Enter the number of students: ")
    numStudents = int(numStudents)
#formats the file properly
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
#gathers information for each student
        for i in range(numStudents):
# gets first and last names
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")

 #gets exam scores, adding them to the list
            examScores = []
            for i in range(1, 4):
                score = input(f"Enter Exam {i} score ")
                while not score.isdigit():
                    print("Please enter a number.")
                    score = input(f"Enter Exam {i} score ")
                examScores.append(int(score))
#adds everything to the file
            writer.writerow([firstName, lastName] + examScores)


writeGrades()
