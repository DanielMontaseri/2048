import os
import sys
import random
import termcolor


#INDENTATION ------> TABS <----------
'''
TODO:
 - Implement moves
	- We have a reference implementation
	- You can also fix/write your own
 
 - Fix check_lost()

 - Add an undo button

 - Add colors for tiles above 128

 - Play the game to find bugs!

 - High scores using Repl.it Database?
	   or JSON(possibly easier(just file writing))
	   can't use JSON because we don't have access to an actual file system
	can use JSON because repl can write and save to a file(try it)
   
'''


# Global variables
cols = 4
rows = 4
board = [[0]*cols for i in range(rows)] # Initialize an array of size rows x cols with zeroes 
#[[0]*cols]*rows does not work, all rows have same pointer
lost = False
score = 0


# spawn a random tile
def spawn_random():
	done = False
	while not done:
		i = random.randint(0, rows-1)
		j = random.randint(0, cols-1)
		# check if block occupied
		if board[i][j] == 0:  	  	  
			# spawn 2 with 90% probability
			if random.randint(0, 9) < 9:
				board[i][j] = 2
			# and 4 with 10%
			else:
				board[i][j] = 4
			done = True


# get the board ready
def prepare_board():
	global board
	board = [[0]*cols for i in range(rows)]

	# spawn two random tiles for starting board
	spawn_random()
	spawn_random()


# color of each tile
def get_color(x):
	if x == 2:
		return "on_grey"
	elif x == 4:
		return "on_red"
	elif x == 8:
		return "on_green"
	elif x == 16:
		return "on_yellow"
	elif x == 32:
		return "on_blue"
	elif x == 64:
		return "on_magenta"
	else:
		return "on_cyan"


# Print the board
def print_board():
	print('''
      ___   ____  __ __  ____ 
     |__ \ / __ \/ // / ( __ )
     __/ // / / / // /_/ __  |
    / __// /_/ /__  __/ /_/ / 
   /____/\____/  /_/  \____/  
	''')
	print("BY LADUE HS CS CLUB" + ("SCORE: " + str(score) + '\n').rjust(15))
	for i in range(0, rows):
		print("-", end='')
		for j in range(0, cols):
			print("--------", end='')
		print()
		
		print("|", end='')
		for j in range(0, cols):
			if (board[i][j] > 0):
				print(termcolor.colored("       ", "white", get_color(board[i][j])), end='|')
			else:
				print("       ", end='|')
		print()
		
		print("|", end='')
		for j in range(0, cols):
			if (board[i][j] > 0):
				print(termcolor.colored(str(board[i][j]).center(7), "white", get_color(board[i][j])), end='|')
			else:
				print("       ", end='|')
		print()
		
		print("|", end='')
		for j in range(0, cols):
			if (board[i][j] > 0):
				print(termcolor.colored("       ", "white", get_color(board[i][j])), end='|')
			else:
				print("       ", end='|')
		print()

	print("-", end='')
	for j in range(0, cols):
		print("--------", end='')
	print()

	print("CONTROLS:       W  ")
	print("              A S D")



# def for random spawn, win condition, 
# hopefully it doesn't break if input doesn't change the board (detect repeat? or no)
# Process a keypress
def do_move(c):
	global lost
	global score
	# Keypress listener/handler

	#Assuming valid input
	if (c == 'w'):
		# Up 
		'''
		for i in range(0, rows):
			for j in range(0, cols):
				if board[i][j] != 0:
					current = board[i][j]
					for k in range(i - 1, -1, -1):
						if k == 0 and board[0][j] == 0:
							board[0][j] = current
							board[i][j] = 0
							break
						elif k == 0 and board[0][j] == current:
							board[0][j] = current * 2
							board[i][j] = 0
							break
						elif board[k][j] == current:
							board[k][j] = current * 2
							board[i][j] = 0
							break
						else:
							board[k + 1][j] = current
							board[i][j] = 0
							break
		# print(c)
		'''
		for i in range(0, cols):
			l = [] # list to store all nonzero tiles
			for j in range(0, rows):
				if board[j][i] > 0:
					# last tile is the same as current, then merge
					if len(l) > 0 and board[j][i] == l[-1]:
						l.pop()
						l.append(-2*board[j][i])
						score += 2*board[j][i]
					else:
						l.append(board[j][i])
					board[j][i] = 0 # clear cell
			
			# refill with list l
			for j in range(0, len(l)):
				board[j][i] = abs(l[j])
#[[board[rows-1-j][i] for j in range(rows)]for i in range(cols)] counterclockwise
#[[board[j][cols-1-i] for j in range(4)]for i in range(4)] clockwise

	elif (c == 'a'):
		# left working [2,2,2,0]=>[4,2,0,0], [2,2,2,2]=>[4,4,0,0]
		'''
		for i in range(0, rows):
			for j in range(0, cols-1):
				for k in range(j+1, cols):
					if board[i][j]==0 or board[i][k]==0:
						continue
					if board[i][j]==board[i][k]: 
						board[i][j]*=2
						board[i][k]=0
						score+=board[i][j]
					else:
						break
					#collapse left [4,0,4,0]=>[4,4,0,0]
			board[i]=[j for j in board[i] if j]+[0]*board[i].count(0)
		'''
		for i in range(0, rows):
			l = [] # list to store all nonzero tiles
			for j in range(0, cols):
				if board[i][j] > 0:
					# last tile is the same as current, then merge
					if len(l) > 0 and board[i][j] == l[-1]:
						l.pop()
						l.append(-2*board[i][j])
						score += 2*board[i][j]
					else:
						l.append(board[i][j])
					board[i][j] = 0 # clear cell
			
			# refill with list l
			for j in range(0, len(l)):
				board[i][j] = abs(l[j])

	elif (c == 's'):
		# down
		#initialize board - switch rows and columns
		
		'''
		columns = [[0]*cols for i in range(rows)]
		for i in range(0, rows):
			for j in range(0, cols):
				columns[i][cols-j] = board[j][i]
	#now you can treat as if 1 column is a 1d array in columns[][]shifting/merging to the left
		#collapse:
		for i in range(0, columns):
			if (columns[i].contains(0)):
				count = columns[i].count(0)
				columns[i].remove(0)
				for j in range(0,count):
					columns[i].append(0)

		#merge Process
		for i in range(0,cols):
			for j in range(0,cols-1):
				if(columns[i][j] == columns[i][j+1] and columns[i][j]!=0):
					columns[i][j]*=2
					columns[i].pop(j+1) 
					columns[i].append(0)
					j+=2
		#put back into board
		for i in range(0, rows):
			for j in range(0, cols):
				board[j][i] = columns[i][cols-j]
		'''
		for i in range(0, cols):
			l = [] # list to store all nonzero tiles
			for j in reversed(range(0, rows)):
				if board[j][i] > 0:
					# last tile is the same as current, then merge
					if len(l) > 0 and board[j][i] == l[-1]:
						l.pop()
						l.append(-2*board[j][i])
						score += 2*board[j][i]
					else:
						l.append(board[j][i])
					board[j][i] = 0 # clear cell
			
			# refill with list l
			for j in range(0, len(l)):
				board[rows-j-1][i] = abs(l[j])

	elif (c == 'd'):
		# right
		for i in range(0, rows):
			l = [] # list to store all nonzero tiles
			for j in reversed(range(0, cols)):
				if board[i][j] > 0:
					# last tile is the same as current, then merge
					if len(l) > 0 and board[i][j] == l[-1]:
						l.pop()
						l.append(-2*board[i][j])
						score += 2*board[i][j]
					else:
						l.append(board[i][j])
					board[i][j] = 0 # clear cell
			
			# refill with list l
			for j in range(0, len(l)):
				board[i][cols-j-1] = abs(l[j])

	else:
		return

	if check_lost():
		lost = True
	
	if not lost:
		spawn_random()


def check_lost():
	#you still need to check if anything is merge-able
	#it might be best if we have a check mergeability function. check every row and column to see if 2 consecutive elements match.
	for i in range(0, rows):
		for j in range(0, cols):
			if board[i][j] == 0:
				return False

	return True

# Run the game until you lose
def game():
	global lost, score

	# Get everything ready
	lost = False
	score = 0
	prepare_board()
	
	while (not lost):
		os.system('clear') # clear screen
		print_board()

		# Read in keypress using os magic
		# It makes Python instally read the character
		# Without having to press enter
		# Don't edit --------------------
		os.system("stty raw -echo")  	
		c = sys.stdin.read(1)
		os.system("stty -raw echo")
		# -------------------------------
		
		# Do a move
		do_move(c) 
		

		if c == 'l': # For debugging
				lost = True

	os.system('clear') # clear screen
	print_board()
	print("You lost!")

	print("Press any key to continue ...")
	# Read in keypress using os magic
	os.system("stty raw -echo")  	
	c = sys.stdin.read(1)
	os.system("stty -raw echo")

		
# Main game loop
while (True):
	game() # run the game