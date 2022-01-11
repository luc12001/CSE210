'''
More in depth version of tictactoe
'''

def printTicTacToe(values):
	print("\n")
	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")

	print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
	print("\t     |     |")
	print("\n")


def printScoreboard(scoreBoard):
	print("\t--------------------------------")
	print("\t       	   SCOREBOARD       ")
	print("\t--------------------------------")

	players = list(scoreBoard.keys())
	print("\t   ", players[0], "\t    ", scoreBoard[players[0]])
	print("\t   ", players[1], "\t    ", scoreBoard[players[1]])

	print("\t--------------------------------\n")

def checkWin(playerPosition, currentPlayer):

	soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

	for x in soln:
		if all(y in playerPosition[currentPlayer] for y in x):

			return True
	return False		

def checkDraw(playerPosition):
	if len(playerPosition['X']) + len(playerPosition['O']) == 9:
		return True
	return False		

def singleGame(currentPlayer):

	values = [' ' for x in range(9)]
	
	playerPosition = {'X':[], 'O':[]}
	
	while True:
		printTicTacToe(values)
		
		try:
			print("Player ", currentPlayer, " turn. Which box? : ", end="")
			move = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again")
			continue

		if move < 1 or move > 9:
			print("Wrong Input!!! Try Again")
			continue

		if values[move-1] != ' ':
			print("Place already filled. Try again!!")
			continue

		values[move-1] = currentPlayer

		playerPosition[currentPlayer].append(move)

		if checkWin(playerPosition, currentPlayer):
			printTicTacToe(values)
			print("Player ", currentPlayer, " has won the game!!")		
			print("\n")
			return currentPlayer

		if checkDraw(playerPosition):
			printTicTacToe(values)
			print("Game Drawn")
			print("\n")
			return 'D'

		if currentPlayer == 'X':
			currentPlayer = 'O'
		else:
			currentPlayer = 'X'

def main():

	print("Player 1")
	player1 = input("Enter the name : ")
	print("\n")

	print("Player 2")
	player2 = input("Enter the name : ")
	print("\n")
	
	currentPlayer = player1

	playerchoice = {'X' : "", 'O' : ""}

	options = ['X', 'O']

	scoreBoard = {player1: 0, player2: 0}
	printScoreboard(scoreBoard)

	while True:

		print("Turn to choose for", currentPlayer)
		print("Enter 1 for X")
		print("Enter 2 for O")
		print("Enter 3 to Quit")

		try:
			choice = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again\n")
			continue

		if choice == 1:
			playerchoice['X'] = currentPlayer
			if currentPlayer == player1:
				playerchoice['O'] = player2
			else:
				playerchoice['O'] = player1

		elif choice == 2:
			playerchoice['O'] = currentPlayer
			if currentPlayer == player1:
				playerchoice['X'] = player2
			else:
				playerchoice['X'] = player1
		
		elif choice == 3:
			print("Final Scores")
			printScoreboard(scoreBoard)
			break	

		else:
			print("Wrong Choice!!!! Try Again\n")

		winner = singleGame(options[choice-1])
		
		if winner != 'D' :
			playerWon = playerchoice[winner]
			scoreBoard[playerWon] = scoreBoard[playerWon] + 1

		printScoreboard(scoreBoard)
		if currentPlayer == player1:
			currentPlayer = player2
		else:
			currentPlayer = player1

if __name__ == "__main__":
    main()