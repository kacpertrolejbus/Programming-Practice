class TennisGame2:
    def __init__(self, player1_name: str, player2_name : str):
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
            score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
            return score_names[self.p1points] if self.p1points < 3 else "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            score_diff = self.p1points - self.p2points
            
            if score_diff == 1:
                return f"Advantage {self.player1_name}"
            elif score_diff == -1:
                return f"Advantage {self.player2_name}"
            elif score_diff >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"


        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.p1points]}-{score_names[self.p2points]}"
