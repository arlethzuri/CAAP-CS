# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["You died.  You kinda suck at this.",
			"Your mom would be proud...",
			"Such a loser.",
			"I have a small puppy that's better at this.",
			"Better luck next time."
			# raise ValueError ('todo')
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'