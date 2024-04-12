import random

def play_human_turn(n):
    while True:
        try:
            user_move = int(input("How many coins do you want to remove (1, 2, or 3)? "))
            if 1 <= user_move <= 3 and user_move <= n:
                break
            else:
                print("Invalid move. Please choose 1, 2, or 3 coins, and make sure there are enough coins in the pile.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Update the number of coins after user's move
    n -= user_move
    print(f"Coins remaining: {n}")

    # Check if the human wins
    if n == 0:
        print("Congratulations! You win!")
        return 0

    return n

def play_computer_turn(n):
    if n % 4 == 0:
        computer_move = random.randint(1, min(3, n))
    else:
        computer_move = n % 4


    # Update the number of coins after the computer's move
    n -= computer_move
    print(f"Computer removes {computer_move} coins.")
    print(f"Coins remaining: {n}")

    # Check if the computer wins
    if n == 0:
        print("Computer wins. Better luck next time!")
        return 0

    return n
