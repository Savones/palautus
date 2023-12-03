class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def equal_score(self):
        if self.player1_score in self.scores:
            score = self.scores[self.player1_score] + "-All"
        else:
            score = "Deuce"

        return score

    def score_over_four(self):
        bigger_score = self.bigger_score()
        if abs(self.player1_score - self.player2_score) >= 2:
            score = "Win for " + bigger_score
        else:
            score = "Advantage " + bigger_score

        return score

    def bigger_score(self):
        if self.player1_score > self.player2_score:
            name = self.player1_name
        else:
            name = self.player2_name
        return name

    def unequal_score(self):
        return self.scores[self.player1_score] + "-" + self.scores[self.player2_score]

    def get_score(self):

        if self.player1_score == self.player2_score:
            return self.equal_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.score_over_four()

        else:
            return self.unequal_score()
