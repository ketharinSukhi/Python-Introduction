import random

def print_board(board):
    for row in board:
        print("   | ".join(row))
        print("-" * 15)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("\nWELCOME TO TIC-TAC-TOE !\n")
    print_board(board)

def main():
    tic_tac_toe()

if __name__ == "__main__":
    main()