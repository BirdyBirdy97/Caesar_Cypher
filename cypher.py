from collections import deque
from clear import clear
from art import logo

alphabet = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(orig_text, shift_amount, direc):
    newword = []
    txt = []
    pos = []
    if direc == "encode":
        alphabet.rotate(shift_amount)
        alpha2 = list(alphabet)
    else:
        alphabet.rotate(-(shift_amount * 2))
        alpha2 = list(alphabet)
    for char in orig_text:
        txt.append(char)
        pos.append(alpha.index(char))
    for num in pos:
        newchar = alpha2[num]
        newword.append(newchar)
    joined_word = "".join((x) for x in newword)
    print(f"Your {direc}d text is {joined_word}.")

print(logo)

done = ""
circle = 0
while circle < 2:
    clear()
    check = False
    while check == False:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            check = True
        else:
            print("\nInvalid selection.")
            check = False
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar(text, -shift, direction)
    
    if circle < 2:
        circle += 1
        if circle < 2:
            done = input("Would you like to go again? (Yes/No)\n").lower()     
            if done == "no":
                circle = 2
                print("Thanks for playing!")
            elif done == "yes":
                circle = circle
            else:
                print("Invalid input.")
                done = input("Would you like to go again? (Yes/No)\n").lower()
        else:
            print("Thanks for playing!")
