number_of_hurdles = 6
while number_of_hurdles  > 0:
    hurdle_height = int(input("Enter the height of a hurdle in cm : "))
    if hurdle_height >=15 and hurdle_height <=30:
        print("You have successfully cleared the hurdle!")
        break
    else:
        print("Your hurdle is too high or too low. Please try again.")
        number_of_hurdles -= 1
        print("Game Over! You made it to the last hurdle.")
