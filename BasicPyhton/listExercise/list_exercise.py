line1 = [" " , " " , " "]
line2 = [" " , " " , " "]
line3 = [" " , " " , " "]
map = [line1,line2,line3]

print("Hiding your treasure X marks the spot")

position = input() #Where do you want to put the treasure?

letter = position[0].lower()  #Converts user input into lowercase letter.
abc = ["a","b","c"]
letter_index = abc.index(letter)   #Finds out which column (column number) the user wants.
number_index = int(position[1]) - 1    #Finds out which row (row number) the user wants.
map[number_index][letter_index] = "X"     #Places an 'X' in the chosen location on the map.
print(f"{line1} \n {line2} \n {line3}")

#Checking if the player has won or lost:
if "X" not in map[0]:
    print("\nCongratulations! You have found the treasure.")
elif "X" not in map[1]:
    print("\nGame Over. Better luck next time.")
else:
    print("\nKeep looking...")






