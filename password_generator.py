# Semi-random password generator.
# No doubt there is a much better way to do this, but wanted the practice.
# Version 1.0 - Improvements forthcoming

from random import choice

lower_alpha = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

upper_alpha = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '-', '+')

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

how_many = input("\nHow many passwords dost thou desire?: ")
pass_length = input("What password length dost thou desire?: ")
first_character_choice = (0, 1)
character_choice = (0, 1, 2, 3)
n = 0

def generator():
    generated_pass = []
    while len(generated_pass) < int(pass_length):
        if len(generated_pass) == 0:
            character_type = choice(first_character_choice)
            if character_type == 0:
                generated_pass.append(choice(lower_alpha))
            elif character_type == 1:
                generated_pass.append(choice(upper_alpha))
        else:
            character_type = choice(character_choice)
            if character_type == 0:
                generated_pass.append(choice(lower_alpha))
            elif character_type == 1:
                generated_pass.append(choice(upper_alpha))
            elif character_type == 2:
                generated_pass.append(choice(symbols))
            elif character_type == 3:
                generated_pass.append(choice(numbers))

    for i in generated_pass:
        print(i, end = "")
    print("\n".strip())

if int(how_many) == 1:
    print("\nThy password, sire:")
else:
    print("\nThy passwords, sire:")

while n < int(how_many):
    generator()
    n = n + 1

if int(how_many) ==1:
    print("\nMight I offer thee some words with which to cleanse thy clipboard?"
    "\nIt would be best not to leave that password in there:")
else:
    print("\nMight I offer thee some words with which to cleanse thy clipboard?"
    "\nIt would be best not to leave any of those passwords in there:")

print("\tNitwit Blubber Oddment Tweak\n")