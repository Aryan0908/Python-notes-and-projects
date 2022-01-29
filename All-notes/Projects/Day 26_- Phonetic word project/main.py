import pandas

names_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {value.letter: value.code for (index, value) in names_data.iterrows()}

correct_entry = False
while not correct_entry:
    user_name = input("What is your name? ").upper()

    try:
        phonetic_names = [alpha_dict[word] for word in user_name]
    except KeyError:
        print("Sorry, only letters are taken as input.")
    else:
        correct_entry = True
        print(phonetic_names)
