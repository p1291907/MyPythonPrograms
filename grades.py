# Function that converts grades to letter grade
def grade_conversion():
    if float(grade) >= 90 and float(grade) <= 100:
        print(name, "Congrats you made an A")
    elif float(grade) >= 80 and float(grade) < 90:
        print(name, "You made a B, you could do better")
    elif float(grade) >= 70 and float(grade) < 80:
        print(name,"You made a C, study more next time")
    elif float(grade) <= 69 and float(grade) >= 60:
        print(name, "You made a D, you must have not studied")
    else:
        print(name, "You made an F, you must study")
# prompts the user for their name
# prompts the user for their grade as long as they don't enter -1
# While grade is not -1 keep calling the grade conversion function
counter = 0
total = 0.0
grade = 0.0
while grade != -1:
    name = input("Enter your name: ")
    grade = float(input("Enter your grade, grade should be a positive number and less than 101, to quit enter -1: "))
    (grade_conversion())
    if grade != -1:
        counter += 1
        total += grade
print("There are", counter, "students in your class")
# tests the nonzeros for counter
if counter:
    average = total / counter
    print("Average of class is", average)
else:
    print("No grades entered")

   







