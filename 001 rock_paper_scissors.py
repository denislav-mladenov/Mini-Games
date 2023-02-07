import random

result = ""
print('Rock_Paper_Scissors rules:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    player_choice = int(input("Enter your choice:"))

    while player_choice > 3 or player_choice < 1:
        player_choice = int(input("Invalid choice! Please try again.\n"
                                  + "Enter your choice: "))

    if player_choice == 1:
        game_choice = "Rock"
    elif player_choice == 2:
        game_choice = "Paper"
    else:
        game_choice = "Scissors"
    print("===================================")
    print(f"You played: {game_choice}")

    computer_choice = random.randint(1, 3)

    # while computer_choice == player_choice:
    #     computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_game_choice = "Rock"
    elif computer_choice == 2:
        computer_game_choice = "Paper"
    else:
        computer_game_choice = "Scissors"
    print(f"Computer played: {computer_game_choice}\n"
          + "===================================")
    print(f"{game_choice} Vs {computer_game_choice}")

    if player_choice == computer_choice:
        print("DRAW!")
        result = "DRAW"
    if player_choice == 1 and computer_choice == 2:
        print("Paper covers rock!")
        result = "Paper"
    elif player_choice == 2 and computer_choice == 1:
        print("Paper covers rock!")
        result = "Paper"

    if player_choice == 1 and computer_choice == 3:
        print("Rock smashes scissors!")
        result = "Rock"
    elif player_choice == 3 and computer_choice == 1:
        print("Rock smashes scissors!")
        result = "Rock"

    if player_choice == 2 and computer_choice == 3:
        print("Scissors cuts paper!")
        result = "Scissors"
    elif player_choice == 3 and computer_choice == 2:
        print("Scissors cuts paper!")
        result = "Scissors"

    if result == "DRAW":
        print("===================================")
        print("It`s a tie!")
        print("===================================")
    if result == game_choice:
        print("===================================")
        print("Player wins!")
        print("===================================")
    if result == computer_game_choice:
        print("===================================")
        print("Computer wins!")
        print("===================================")

    print("Do you want to play again? (Y/N)")

    answer = input()
    if answer == "y" or answer == "Y":
        continue
    elif answer == "n" or answer == "N":
        break
    else:
        print("Invalid answer! Let`s play one more game until you answer correctly ;)")

print("Thanks for playing. See you soon.")
