import random

def print_board(board):
    for row in board:
        print("   | ".join(row))
        print("-" * 15)
       
def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))-1
            if move<0 or move >= 9:
                raise ValueError
            return divmod(move, 3)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)
    print("\nWELCOME TO TIC-TAC-TOE !\n")
    print_board(board)

    while True:
        print(f"{current_player}'s turn.")
        row, col = get_player_move()

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue


def main():
    tic_tac_toe()

if __name__ == "__main__":
    main()