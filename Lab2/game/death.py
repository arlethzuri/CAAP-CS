# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
    #funny quips for after a death scene
    quips = ["You're not very good at this are you? ;)",
            "Oh woww, really?",
            "Boi",
            "Oh wow, did you actually die?",
            "Better luck next time."
            ]
    def enter(self):
        print (Death.quips[randint(0, len(self.quips)- 1)])#print a random quip from the list
        return 'died'