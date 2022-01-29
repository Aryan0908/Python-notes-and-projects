
with open("Input/Names/invited_names.txt") as names:
    person_names = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in person_names:
        stripped_name = name.strip()
        new_content = letter_content.replace("[name]", f"{stripped_name}")
        final_content = new_content.replace("Angela", "Aryan")
        with open(f"Output/letter_of_{stripped_name}", "w") as current_letter:
            current_letter.write(f"{final_content}")





