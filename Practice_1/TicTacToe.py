import random

def print_board(board):
    for row in board:
        print("   | ".join(row))
        print("-" * 15)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False 
def is_full(board):
    """Checks if the board is full, leading to a tie."""
    return all(all(cell != " " for cell in row) for row in board)
       
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
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break
        
        current_player = "X" if current_player == "O" else "O"
    
    print("Game Over! Thanks for playing.")


def main():
    tic_tac_toe()

if __name__ == "__main__":
    main()