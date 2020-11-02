import os
import sys


'''
TODO:
 - Implement moves
 - Rewrite the interface to look nicer
 - High scores using Repl.it Database?
'''


# Global variables
cols = 4
rows = 4
board = [[0]*cols]*rows
lost = False


def prepare_board():
	global board
	board = [[0]*cols]*rows

	# spawn two random tiles


# Print the board
# Maybe rewrite to look nicer?
def print_board():
	for i in range(0, rows):
		for j in range(0, cols):
			b = str(board[i][j])
			b = b.ljust(5) # Pad with spaces
			print(b, end='')
		print()


#def for random spawn, win condition, 
#hopefully it doesn't break if input doesn't change the board (detect repeat? or no)
# Process a keypress
def do_move(c):
	# Do some stuff here
	
	if (c == 'w'):
		# up
		print(c)
	
	if (c == 'a'):
		# left
		print(c)

	if (c == 's'):
		# down
		print(c)

	if (c == 'd'):
		# right
		print(c)



# Run the game into you lose
def game():
	global lost
	lost = False
	
	prepare_board()
	
	while (not lost):
		
		os.system('clear') # clear screen
		print_board()


		# Read in keypress using os magic
		# Don't edit --------------------
		os.system("stty raw -echo")		
		c = sys.stdin.read(1)
		os.system("stty -raw echo")
		# -------------------------------


		# Do stuff with c
		do_move(c)

		if c == 'l': # For debugging
			lost = True
	

	os.system('clear') # clear screen
	print_board()
	print("You lost!")

	print("Press any key to continue ...")
	os.system("stty raw -echo")		
	c = sys.stdin.read(1)
	os.system("stty -raw echo")


# Main game loop
while (True):	
	game() # run the game