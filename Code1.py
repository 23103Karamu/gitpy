#Find if they have a motorcycle
car_or_motorcycle = ""
while car_or_motorcycle == "":
    car_or_motorcycle = input("Do you have a car or motorcycle? ")
    #Check for valid input, if good then break out of loop
    if car_or_motorcycle.lower() == "car" or car_or_motorcycle.lower() == "motorcycle":
        break
    else:
        print("Please enter 'car' or 'motorcycle'")
        car_or_motorcycle = ""
#Find the size of the tyre
Wheel_size = int(input("What is the width of the tyre? "))

#Print the cost based on the size and if car or motorcycle
if car_or_motorcycle.lower() == "car":
    if Wheel_size > 14:
        print("The car tyre will cost $250")
    else:
        print("The car tyre will cost $180")
if car_or_motorcycle.lower() == "motorcycle":
    if Wheel_size > 14:
        print("The motorcycle tyre will cost $350")
    else:
        print("The motorcycle tyre will cost $280")