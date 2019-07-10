# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = raise ValueError ('todo')
	board = raise ValueError ('todo')

	def __init__(self):
		for i in range(self.size):
			self.board.append(raise ValueError ('todo'))

	# prints the leaderboard
	def print_board(self):
		raise ValueError ('todo')

	# checks if given score should be in the leaderboard
	def update(self, score):
		raise ValueError ('todo')

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		raise ValueError ('todo')