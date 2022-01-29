from replit import clear
import random
import hangman_words
import hangman_art

print(hangman_art.logo)

lives = 6
word_list = hangman_words.word_list
word_list_length = len(word_list)



chosen_word = word_list[random.randint(0, word_list_length - 1)]
chosen_word_len = len(chosen_word)
print(chosen_word)


blank_list = []
for blank in range(1, chosen_word_len + 1):
  blank_list += "_"

chosen_word_list = []
for chosen_list in chosen_word:
  chosen_word_list += chosen_list


lives = 6

while blank_list != chosen_word_list and lives > 0:
      user_input = input("Which word you you want to pick? ").lower()
      clear()
      if user_input in blank_list:
        print(f"You have already entered the letter '{user_input}'\nPlease try again!")
      
      elif user_input in chosen_word:
        for position in range(chosen_word_len):
          if user_input == chosen_word_list[position]:
            letter = chosen_word_list[position]
            blank_list[position] = letter
            
      else:
        lives -= 1
        print("Sorry you have guessed a wrong word. You loose a life.")
      
      print(f"{' '.join(blank_list)}")
      print(hangman_art.stages[lives])
    
if blank_list == chosen_word_list:
  print("You Win!")
elif lives == 0:
  print("You Loose!")



