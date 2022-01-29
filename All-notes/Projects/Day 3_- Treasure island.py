# Name
name = input("What is your name? ")

# Welcome text
print(f"Hello {name},\n Welcome to the Treasure Island")

# Goal 
print("Your goal is to find the treasure\n")

# Instructions
print("Instructions :- Make good choices\n")

print("The story begins here!")

# Story
print(f"One day you were cleaning up your house and you found a treasure map. You tavelled to the island via your private plane. You followed the map and came across a crossroad.")

# Road
road = input("Choose a road! Left or Right ")
if road == "Left":
  print("Congratulation's you have made a right decision. Good luck finding the treasure!\nBy the end of the road there was an ocean and the map indicated that you have to cross the ocean in order to continue that chase. The distance between the two islands is approx. 25km. You have asked the residence of the island and they told you that a ship sails at 6 p.m. for that island (current time is 12 p.m.).")

  ocean = input("What will you choose? Wait for the boat or swim to the island.\nType Wait or Swim to answer! ")
  if ocean == "Wait":
    print("Congratulations! you choose the right one.\nAfter crossing the ocean and following the map, you came across a cave and the map shows that the tresure is at the other side of the cave. You walked in it and saw that the cave goes in three different direction.")
    cave = input("Which one will you choose?\nLeft, Middle or Right. ")
    if cave == "Left":
      print("Game Over!\nYou walked into Lava. Please try again.")
    elif cave == "Middle":
      print("Game Over!\nYou were frozen to death. Please try again!")
    elif cave == "Right":
      print("Congratulation! You Won.")
    else:
      print("Invalid input :- Please enter Left, Middle or Right.")
  elif ocean == "Swim":
    print("Game Over!\nYou were torn apart by a shark. Please try again.")
  else:
    print("Invalid input :- Please choose from Wait or Swim")
elif road == "Right":
  print("Game Over!\nA hungry tiger was waiting for you at the end of the road. Please try again.")
else:
  print("Invalid input! Please choose from Right or Left")

