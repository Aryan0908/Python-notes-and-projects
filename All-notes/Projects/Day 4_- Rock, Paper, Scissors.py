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

#Write your code below this line 👇
rps = [rock, paper, scissors]

user = int(input(f"What do you want to choose?\nType 0 for rock, 1 for Paper or 2 for Scissors :- "))
print(f"\nYou choose:\n{rps[user]}")

computer = random.randint(0,2)
print(f"\nComputer choose:\n{rps[computer]}")

if (user == 0) and (computer == 2):
  print("You Win!")
elif (computer == 0) and (user == 2):
  print("You Loose!")
elif (user >= 3) or (computer >= 3):
  print("Invalid number.\nYou Lose!")
elif user > computer:
  print("You Win!")
elif computer > user:
  print("You Lose!")
else:
  print("Invalid entry.\nYou Lose!")




