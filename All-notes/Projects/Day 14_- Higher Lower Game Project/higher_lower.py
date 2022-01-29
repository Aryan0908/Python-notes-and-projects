import random
from higher_lower_data import data
from higher_lower_art import logo, vs
from replit import clear


def random_data():
    return random.choice(data)

def option_a(random_a):
    return f"Compare A: {random_a['name']}, {random_a['description']}, from {random_a['country']}"

def option_a_value(random_a_follower):
    return random_a_follower['follower_count']

def option_b(random_b):
    return (f"Against B: {random_b['name']}, {random_b['description']}, from {random_b['country']}")
    
def option_b_value(random_b_follower):
    return random_b_follower['follower_count']





print(logo)
final_score = 0
random_data_a = random_data()
random_data_a_list = [0]

user_choice = True
while user_choice == True:
    random_data_b = random_data()
    
    
    
    # Final Score Update
    if final_score > 0:
        print(f"You're right! Your  current score is: {final_score}")
        a_data = option_a(random_a = random_data_a_list[0])
        a_score = option_a_value(random_a_follower = random_data_a_list[0])
        print(a_data)
        print(a_score)
    
    else:
        a_data = option_a(random_a = random_data_a)
        a_score = option_a_value(random_a_follower = random_data_a)
        print(a_data)
        print(a_score)
    
    print(vs)
    
    b_data = option_b(random_b = random_data_b)
    b_score = option_b_value(random_b_follower = random_data_b)
    print(b_data)
    print(b_score)
    
    # User Input
    user_input = input("Which option have more instagram followers, 'A' or 'B'?").lower()
    if user_input == 'a':
        user_input = a_score
    else:
        user_input = b_score
    

    clear()
    print(logo)
    # Comprison
    if a_score > b_score and user_input == a_score:
        
        final_score += 1
        random_data_a_list[0] = random_data_b
        
    elif b_score > a_score and user_input == b_score:
        
        final_score += 1
        random_data_a_list[0] = random_data_b
    else:
        
        print(f"Sorry that's wrong. Final Score: {final_score}")
        user_choice = False
             
    
    
        
        
        
        



