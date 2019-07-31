# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
    size = 10
    board = []

    def __init__(self):
        for i in range(self.size):
            defaultName = 'player'
            defaultMoves = 999
            score = Score(defaultName, defaultMoves)
            self.board.append(score)
            
    # prints the leaderboard, pretty intuitive
    def print_board(self):
        print("*** CTA Adventure Leaderboard ***")        
        for pos in range(0, self.size-1):
            score = self.board[pos]
            print("| Name: ", score.get_name()," | " + "Moves: ", score.get_score(), " |")
        print("\n")   
        
    # checks if given score should be in the leaderboard
    def update(self, score):
        playerMoves = score.get_score()
        
        for i in range(self.size):
            if playerMoves < self.board[-1].get_score():
                self.insert_score(score)
                self.board.pop(-1)
                return
        
    # inserts the score in the given position (assuming it's better or equal to the one in the given rank)
    # moving everything below down a rank
    def insert_score(self, score):
        for i in range(self.size - 1):
            if score.get_score() < self.board[i].get_score():
                self.board.insert(i, score)
                return