class Player:
    def __init__(self, score):
        self.score = score
    
    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0