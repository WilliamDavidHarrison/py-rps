import random

play_again = 'y'
while play_again == 'y':
    ai_move = random.randint(0, 2)
    ai_move_string = ""
    if ai_move == 0:
        ai_move_string = "rock"
    elif ai_move == 1:
        ai_move_string = "paper"
    else:
        ai_move_string = "scissors"
    player_move = input("Rock, paper, or scissors? (r/p/s): ")
    print(f"AI plays {ai_move_string}.")
    result = ""
    if player_move == 'r':
        if ai_move == 0:
            result = "It's a tie!"
        elif ai_move == 1:
            result = "You lose!"
        else:
            result = "You win!"
    elif player_move == 'p':
        if ai_move == 0:
            result = "You win!"
        elif ai_move == 1:
            result = "It's a tie!"
        else:
            result = "You lose!"
    elif player_move == 's':
        if ai_move == 0:
            result = "You lose!"
        elif ai_move == 1:
            result = "You win!"
        else:
            result = "It's a tie!"
    else:
        result = "Invalid move. Please enter r, p, or s."
    print(result)
    play_again = input("Do you want to play again? (y/n): ")
