import random
import replit
import blackjack_art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    all_info = {
        "player_card":{
            "cards": [], 
            
            "total": 0
        },
        "computer_card":{
            "cards": [], 
            
            "total": 0
        }
        
    }


    def all_player_cards():
        return all_info["player_card"]["cards"]

    def all_player_score():
        all_info["player_card"]["total"] = sum(all_info["player_card"]["cards"])
        return all_info["player_card"]["total"]

    def all_computer_cards():
        return all_info["computer_card"]["cards"]

    def all_computer_score():
        all_info["computer_card"]["total"] = sum(all_info["computer_card"]["cards"])
        return all_info["computer_card"]["total"]

    def random_cards():
        return random.choice(cards)



    player_cards = all_player_cards()
    computer_cards = all_computer_cards()



    play = True
    play_again = input("Do you want to play BlackJack. For yes type 'Y' or for no type 'N'. ").lower()
    if play_again == "y":
        replit.clear()
        print(blackjack_art.logo)

        # Starting Player card
        player_start_card = player_cards.extend([random_cards(), random_cards()])
        player_start_score = all_player_score()

        print(f"    Your card: {player_cards}, current_score: {player_start_score}")

        # Starting computer card
        computer_start_card = computer_cards.extend([random_cards(), random_cards()])
        computer_start_score = all_computer_score()

        print(f"    Computer first card: {computer_cards[0]}")

        user_choice = True
        while user_choice == True:
            if all_player_score() < 21:
                user_input = input("Type 'Y' to get another card or 'N' to pass. ").lower()

                if user_input == 'y':
                    player_new_card = player_cards.extend([random_cards()])
                    player_new_score = all_player_score()
                    print(f"    Your card: {player_cards}, current score: {player_new_score}")
                    print(f"    Computer first card: {computer_cards[0]}")

                    if all_computer_score() <= 16:
                        computer_new_card = computer_cards.extend([random_cards()])
                    

                
                elif user_input == "n":
                    user_choice = False
                    print(f"    Your final hand: {player_cards}, final score: {all_player_score()}")
                    print(f"    Computer final hand: {computer_cards}, final score: {all_computer_score()}")
                    
                    if all_player_score() > all_computer_score() and all_player_score() <= 21:
                        print("You win!")
                    
                    elif all_player_score() == all_computer_score() and all_player_score() <= 21:
                        print("Draw")
                    
                    elif all_computer_score() > all_player_score() and all_computer_score() <= 21:
                        print("Computer Wins!")
                    
                    elif all_computer_score() > 21:
                        print("Computer exceeded. You Win!")
                    else:
                        print("You've exceeded. You loose!")  
                
            else:
                user_choice = False
                print(f"Your final hand: {player_cards}, final score: {all_player_score()}")
                print(f"Computer final hand: {computer_cards}, final score: {all_computer_score()}")
                
                if all_player_score() > all_computer_score() and all_player_score() <= 21:
                    print("You win!")
                    
                elif all_player_score() == all_computer_score() and all_player_score() <= 21:
                    print("Draw")
                    
                elif all_computer_score() > all_player_score() and all_computer_score() <= 21:
                    print("Computer Wins!")
                    
                elif all_computer_score() > 21:
                    print("Computer exceeded. You Win!")
                else:
                    print("You've exceeded. You loose!")   
                
                
        blackjack()

    
    else:
        play = False

blackjack()