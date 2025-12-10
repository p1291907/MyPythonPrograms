# function that has an empty list
def add_students(students):
# sorting students 
    students.sort()
    students.reverse()
    return(students)
students = ["Renee"]
# Ask the name of the student 12 times then add it to the list   
for i in range(12):
    name = input("Enter your name: ")
    students.append(name)
    (add_students(students))
# Write the names to the names.txt file
with open ("names.txt", "a") as names:
        names.write(f"{students}\n")