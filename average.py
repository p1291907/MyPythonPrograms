# Asks 12 students for their names and average
def average():
    name = input("Enter your name: ")
    grade = float(input("Enter your average: "))
# raises an exception when a user enters an invalid grade
    if grade < 0 or grade > 100:
        raise ValueError("Grade cannot be less than 0 or greater than 100")
    return(name, grade)
max_students = 12
for i in range(max_students):
    try:
        name, grade = average()
# Creates grades.txt in an append mode and writes the names and average into it
# Closes the text file
# To display the contents of file enter cat grades.txt on the terminal
        with open("grades.txt", "a") as file:
            file.write(f"{name}, average is:, {grade}\n")
    except ValueError:
        print("Invalid grade, it cannot be less than 0 or greater than 100: ")

 
    
        
