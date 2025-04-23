import random

def display_board(board):
    '''
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    '''
    
    def print_horizontal_line():
        print("+-------+-------+-------+")

    def print_row(row):
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")

    for row in board:
        print_horizontal_line()
        print_row(row)
    print_horizontal_line()


def enter_move(board):
    '''
    The function accepts the board's current status, asks the user about their move,
    checks the input, and updates the board according to the user's decision.
    '''

    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("The square is already occupied! Choose another.")
        except (ValueError, IndexError):
            print("Invalid move! Please enter a number between 1 and 9.")


def make_list_of_free_fields(board):
    '''
    The function browses the board and builds a list of all the free squares.
    The list consists of tuples, where each tuple is a pair of row and column numbers.
    '''
    free_fields = []
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell not in ['O', 'X']:
                free_fields.append((row_index, col_index))
    return free_fields


def victory_for(board, sign):
    '''
    The function analyzes the board's status to check if
    the player using 'O's or 'X's has won the game.
    '''
    # Check rows and columns
    for i in range(3):
        if all(board[i][col] == sign for col in range(3)) or all(board[row][i] == sign for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True

    return False


def draw_move(board):
    '''
    The function draws the computer's move and updates the board.
    '''
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'


def main():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)
    
    while True:
        enter_move(board)
        
        if victory_for(board, 'O'):
            print("You win!")
            break

        
        draw_move(board)
        display_board(board)

        if victory_for(board, 'X'):
            print("Computer wins!")
            break

        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()