import caesar_art

print(caesar_art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(txt, shft, caesar_direction):
    final_text = ""
    for char in txt:
        if char in alphabet:
            position = alphabet.index(char)
            if caesar_direction == "encode":
                new_position = position + shft
            elif caesar_direction == "decode":
                new_position = position - shft
            else:
                print("/nInvalid input! Please enter encode or decode.")
            final_text += alphabet[new_position]
        else:
            final_text += char

    print(f"/nThe {caesar_direction} text is {final_text}")

result = True
while result == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    shift = shift % 26
    caesar(txt=text, shft=shift, caesar_direction=direction)

    user_input = input("\nDo you want to do it again? Type 'yes' or 'no'. ")
    user_input.lower()
    if user_input != "yes":
        result = False
        print("Goodbye")


