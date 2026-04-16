class TennisGame3:
    def __init__(self, player1_name : str, player2_name : str):
        """
        Inicjalizacja gry
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name : str):
        """ 
        Dodaje punkt dla gracza który wygrał 
        """
        if player_name == self.player1_name:
            self.p1_points += 1
        elif player_name == self.player2_name:
            self.p2_points += 1

    def score(self):
        """
        Funkcja wylicza podczas róźnych sytuacji kto wygrywa
        """
        if self.p1_points == self.p2_points:
            score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
            return score_names[self.p1_points] if self.p1_points < 3 else "Deuce"

        if self.p1_points >= 4 or self.p2_points >= 4:
            leading_player = self.player1_name if self.p1_points > self.p2_points else self.player2_name
            
            point_diff = abs(self.p1_points - self.p2_points)
            
            if point_diff == 1:
                return f"Advantage {leading_player}"
            else:
                return f"Win for {leading_player}"

        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = score_names[self.p1_points]
        score2 = score_names[self.p2_points]
        
        return f"{score1}-{score2}"