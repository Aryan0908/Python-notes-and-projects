import replit
import art

print(art.logo)

def bidder_info(user_name, bid_amount):
    user_info = {}
    user_info["Name"] = user_name
    user_info["Bidding Amount"] = bid_amount
    all_information.append(user_info)

user_choice = True
all_information = []
while user_choice == True:
    name = input("Enter the bider name. \n")
    

    amount = int(input("\nWhat is your bid anount? \n$"))

    bidder_info(user_name = name, bid_amount = amount)

    other_bidders = input("\nAre their any other bidders? Type 'Y' for yes or 'N' for no ")
    other_bidders.lower()


    highest_bidder_name = ""
    highest_bidder_amount = 0
    

    if other_bidders == "y":
        replit.clear()
    else:
        user_choice = False
        replit.clear()
        for highest_bid in all_information:
            if highest_bid["Bidding Amount"] > highest_bidder_amount:
                highest_bidder_amount = highest_bid["Bidding Amount"]
                highest_bidder_name = highest_bid["Name"]
        
        print(f"\nThe highest bidder name is {highest_bidder_name} and the the bid amount is ${highest_bidder_amount}")








