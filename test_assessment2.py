## Student details 
Student_name = ""
while Student_name == "":
    Student_name = input("Enter your name: ")
    if Student_name == "":
        print("Please input a name")
        Student_name = ""

Student_age = None
while Student_age is None:
    try:
        Student_age = int(input("Enter an age: "))
    except ValueError:
        print("Please input an integer")
    else:
        break


## Checking if the student is eligible for the Club Day
Student_eligibility = False
if Student_age <= 11 or Student_age >= 18:
    print("Sorry but you are not eligible for the Club Day")
else:
    Student_eligibility = True
Activities = {
    'Activity': "Science"
}


print('\nChoose an activity: ')

print(f"\n{Activities['Activity']} ({hours}, {challenge}, ${cost} fee)")