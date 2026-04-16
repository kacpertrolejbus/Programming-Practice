class TennisGame1:
    def __init__(self, player1_name : str, player2_name : str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name : str):
        """ 
        Dodaje punkt dla gracza który wygrał 
        """
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1

    def score(self):
        """
        Funkcja wylicza podczas róznych sytuacji kto wygrywa
        """
        if self.p1points == self.p2points:
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        
        if self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points

            if minus_result == 1:
                return f"Advantage {self.player1_name}"
            elif minus_result == -1:
                return f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"
            
        scores_name = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = scores_name[self.p1points]
        score2 = scores_name[self.p2points]

        return f"{score1}-{score2}"
