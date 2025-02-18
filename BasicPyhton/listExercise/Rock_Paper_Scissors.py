import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"The computer chose {game_images[computer_choice]}")
if user_choice>=3 or  user_choice<0:
    print("Invalid input! Please type 0, 1 or 2.")
elif user_choice==0 and computer_choice==2:
    print("Rock crushes Scissors. You win!")
elif user_choice==2 and computer_choice==0:
    print("Paper covers Rock. You lose.")
elif computer_choice>user_choice:
    print(f"Computer wins this round.You lose")
elif user_choice>computer_choice:
    print(f"You win this round!")
elif  user_choice==computer_choice:
    print("It's a tie! No one wins or loses.")

