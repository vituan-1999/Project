import random as rand
from support import *
Choices = ["Kéo", "Búa", "Bao"]
print("\tTrò chơi Kéo Búa Bao :)")
while True:
    User = None
    Computer = rand.choice(Choices)
    while User not in Choices:
        User = input("\nKéo, Búa, Bao?: ").capitalize()
    message(Computer, User)
    result = calculate(Computer, User)
    print(result)
    play_again = input("Bạn muốn chơi lại không(Yes/No)? ").capitalize()
    if play_again == "No":
        break
print("\nBye Bye! See ya!")
print("----------------------------------------")
