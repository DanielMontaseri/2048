import os
import sys

cols = 4
rows = 4
board = [[0]*cols]*rows
lost = False


def prepare_board():
	global board
	board = [[0]*cols]*rows


#def for random spawn, win condition, 
#hopefully it doesn't break if input doesn't change the board (detect repeat? or no)
# Process a keypress
def do_move(c):
	# Do some stuff here
	print(c)




# Run the game into you lose
def game():
	global lost
	lost = False
	
	prepare_board()
	
	while (not lost):
		# Read in keypress using os magic
		# Don't edit --------------------
		os.system("stty raw -echo")		
		c = sys.stdin.read(1)
		os.system("stty -raw echo")
		# -------------------------------


		# Do stuff with c
		do_move(c)

		if c == 'a':
			lost = True
	
	print("You lost!")


# Main game loop
while (True):	
	game() # run the game