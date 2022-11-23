run = 'yes'
def userInput(surname, firstName, studentID):
    print(f"{firstName} {surname}'s email address is {surname[0:2]}{firstName[0:2]}{studentID}@schools.edu")

while run == 'yes': 
    surname = input("Enter the student's surname: ")
    firstName = input("Enter the student's first name: ")
    studentID = int(input("Enter the student's ID: "))
    surname = surname.lower()
    firstName = firstName.lower()
    if surname and firstName and studentID:
        userInput(surname, firstName, studentID)
        run = input("Continue? ")
        run = run.lower()
    else:
        print("student ID not correct and/or other details incorrect")
        run = input("Try again?")
        run = run.lower()
exit(print("Exiting!"))
