# Quiz game
# -------------------------------------------------
def new_game():
    correct_guess = 0  # count number of correct
    guesses = []  # list save all guess to calculate score
    question_number = 0  # print each option for each question
    for key in question:
        print("-----------------------------------")
        print(key)  # print all question element
        for i in option[question_number]:
            print(i)  # print all option element
        question_number += 1
        guess = input("Your choice (A, B, C, D): ").upper()
        guesses.append(guess)
        correct_guess += check_answer(question.get(key), guess)
    display_score(correct_guess, guesses)


# -------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT! :)")
        return 1
    else:
        print("WRONG! :(")
        return 0


# -------------------------------------------------
def display_score(correct_guess, guesses):
    print("-----------------------------------")
    print("RESULT:")
    print("-----------------------------------")
    print("Right answer: ", end=" ")
    for i in question:
        print(question.get(i), end=" ")
    print()
    print("Your guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = float(correct_guess / len(question)) * 100
    print("Your score is: " + str(score))


# -------------------------------------------------
def play_again():
    again = input("\nDo you want to try again (Yes, No)? ").capitalize()
    if again == "No":
        return False
    else:
        return True


# Data base
question = {
    "Who create Python?": "A",
    "What year was Python create?": "B",
    "How many continents in the world?": "C",
    "What is capital of Vietnam?": "D",
    "What is the shape of the Earth?": "A"
}

option = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. 5", "B. 6", "C. 7", "D. 8"],
          ["A. Beijing", "B. Washington DC", "C. Ho Chi Minh City", "D. Ha noi"],
          ["A. Round", "B. Rectangle", "C. Oval", "D. Triangle"]]

# Main function
new_game()
while play_again():
    new_game()
print("\nBye Bye! See ya :)")
