#this program reaads the file created by the previous
#program, then prints it all out in the correct format.

import csv
#this function opens up the grades file, reads information.
#then prints it out
def readGrades():
    filename = "grades.csv"
#opens the file in read mode and reads it
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
#turns the read information into lists
        data = list(reader)

#prints the table with its information about the students
    print("\n{:<12} {:<12} {:<7} {:<7} {:<7}".format(*data[0]))
    print("-" * 50)


    for row in data[1:]:
        print("{:<12} {:<12} {:<7} {:<7} {:<7}".format(*row))


readGrades()
