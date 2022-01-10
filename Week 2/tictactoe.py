playBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in playBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def ticTacToe():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(playBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if playBoard[move] == ' ':
            playBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count >= 5:
            if playBoard['7'] == playBoard['8'] == playBoard['9'] != ' ':
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif playBoard['4'] == playBoard['5'] == playBoard['6'] != ' ':
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif playBoard['1'] == playBoard['2'] == playBoard['3'] != ' ': 
                printBoard(playBoard)
                print("\nGame Over.\n")            
                print(" **** " +turn + " won. ****")
                break
            elif playBoard['1'] == playBoard['4'] == playBoard['7'] != ' ': 
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif playBoard['2'] == playBoard['5'] == playBoard['8'] != ' ':
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif playBoard['3'] == playBoard['6'] == playBoard['9'] != ' ':
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif playBoard['7'] == playBoard['5'] == playBoard['3'] != ' ': 
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif playBoard['1'] == playBoard['5'] == playBoard['9'] != ' ': 
                printBoard(playBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 


        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")


        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            playBoard[key] = " "

        ticTacToe()

if __name__ == "__main__":
    ticTacToe()