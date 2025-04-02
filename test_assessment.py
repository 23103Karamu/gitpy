## Student details 
Student_name = ""
while Student_name == "":
    Student_name = input("Enter your name: ")
    if Student_name == "": ## If they don't input a name the program will loop back to the question so they have to input a name
        print("Please input a name")
        Student_name = ""
    else:
        break
Student_age = None
while Student_age is None: ## If the student doesn't input an integer for their age the program will loop back to the question until it's answered
    try:
        Student_age = int(input("Enter an age: "))
    except ValueError:
        print("Please input an integer")
    except Student_age <= 0 or Student_age >= 100:
        print("Are you sure that is your age?")
        Student_age = None
    else:
        break

## Checking if the student is eligible for the Club Day
Student_eligibility = False
if Student_age <= 11 or Student_age >= 18:
    print("Sorry but you are not eligible for the Club Day")
else:
    Student_eligibility = True

## The activities
Cost = 0
Are_going = None
Chosen_activity = None
while Chosen_activity == None and Student_eligibility == True: ## Using a while Chosen_activity = "": so if they put a number that is not availible it'll loop back
    Chosen_activity = int(input("\nChoose an activity:\n1. Music Jam Session (2 hours, easy, $5 fee)\n2. Science Experiments Lab (3 hours, moderate, $10 fee)\n3. Sports Leadership Training (4 hours, challenging, $12 fee)\nEnter the number of your chosen activity: "))
    if Chosen_activity == 1:
        Chosen_activity = "Music Jam Session (2 hours, easy)"
        Cost = Cost + 5
        break
    elif Chosen_activity == 2:
        Chosen_activity = "Science Experiments Lab (3 hours, moderate)"
        Cost = Cost + 10
        break
    elif Chosen_activity == 3:
        Chosen_activity = "Sports Leadership Training (4 hours, challenging)"
        Cost = Cost + 12
        break
    elif Chosen_activity != 1 or 2 or 3:
        print("Invalid choice, try again.")
        Chosen_activity = None
Chosen_meal = None
while Chosen_meal == None and Student_eligibility == True:
    Chosen_meal = int(input("\nMeal options:\n1. Standard\n2. Vegetarian\n3. Dairy-free\n4. No meal\nEnter the number of your meal choice: "))
    if Chosen_meal == 1:
        Chosen_meal = "Standard"
        Cost = Cost + 7
    elif Chosen_meal == 2:
        Chosen_meal = "Vegetarian"
        Cost = Cost + 7
    elif Chosen_meal == 3:
        Chosen_meal = "Dairy-free"
        Cost = Cost + 7
    elif Chosen_meal == 4:
        Chosen_meal = "None"
        Cost = Cost 
        break
    else:
        print("Invalid choice, try again.")
        Chosen_meal = None

    while Are_going == None and Student_eligibility == True:
        Are_going = input(f'\n{Student_name}, age {Student_age}, activity chosen: {Chosen_activity}, meal option: {Chosen_meal}, cost ${Cost}. Are you attending (yes/no)? ').lower()
        if Are_going == "yes" or Are_going == "y":
            print(f"\n{Student_name} is confirmed for {Chosen_activity}. See you there!")
            break
        elif Are_going == "no" or Are_going == "n":
            print(f"\n{Student_name} will not be attending tonight.")
            break
        else:
            print("Invalid choice, try again.")
            Are_going = ""