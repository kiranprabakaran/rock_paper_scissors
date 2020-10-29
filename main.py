import random

while True:

    print("rock, paper, scissors?")
    choice = input()
    choice = choice.lower()

    print("my choice is ", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = choices[random.randint(0, len(choices)-1)]
    print("computer choice is ", computer_choice)

    if choice in choices:
        if choice == 'rock':
            if computer_choice == 'rock':
                print("It is a Draw")
            elif computer_choice == 'paper':
                print("You Lost :(")
            elif computer_choice == 'scissors':
                print("Winner, Winner!!!!")

        if choice == 'paper':
            if computer_choice == 'rock':
                print("Winner, Winner!!!!")
            elif computer_choice == 'paper':
                print("It is a Draw")
            elif computer_choice == 'scissors':
                print("You Lost :(")

        if choice == 'scissors':
            if computer_choice == 'rock':
                print("You Lost :(")
            elif computer_choice == 'paper':
                print("Winner, Winner!!!!")
            elif computer_choice == 'scissors':
                print("It is a Draw")

    else:
        print("Your answer doesn't make sense. Try again")

    print()







