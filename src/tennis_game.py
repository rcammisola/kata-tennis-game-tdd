

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

        self.point_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

    def score(self):
        if self.player1_points == self.player2_points:
            tied_score = self.point_map[self.player1_points]
            game_score = f"{tied_score}-all"
        else:
            player1_score = self.point_map[self.player1_points]
            player2_score = self.point_map[self.player2_points]

            game_score = f"{player1_score}-{player2_score}"

        return game_score

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1
        else:
            raise ValueError(f"Illegal player provided: '{player_name}'")
