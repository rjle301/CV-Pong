class Player:
    def __init__(self):
        self.score = 0

    def set_score(self, score):
        self.score = score

    def increment_score(self):
        self.score += 1
    
    def get_score(self):
        return self.score
    
    def get_score_str(self):
        return str(self.score)

    def reset_score(self):
        self.score = 0