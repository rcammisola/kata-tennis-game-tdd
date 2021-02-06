

POINTS_LOVE = 0
POINTS_FIFTEEN = 1
POINTS_THIRTY = 2
POINTS_FORTY = 3


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

        self.point_map = {
            POINTS_LOVE: "Love",
            POINTS_FIFTEEN: "Fifteen",
            POINTS_THIRTY: "Thirty",
            POINTS_FORTY: "Forty",
        }

    def score(self):
        if (self.player1_points > POINTS_FORTY or self.player2_points > POINTS_FORTY) and self._lead_is_at_least(2):
            game_score = f"{self._currently_leading_player()} Won"

        elif self.player1_points == self.player2_points:
            game_score = self._tied_game_score()

        elif self.player1_points > POINTS_THIRTY and self.player2_points > POINTS_THIRTY:
            game_score = f"Advantage {self._currently_leading_player()}"

        else:
            player1_score = self.point_map[self.player1_points]
            player2_score = self.point_map[self.player2_points]

            game_score = f"{player1_score}-{player2_score}"

        return game_score

    def _lead_is_at_least(self, lead):
        return abs(self.player1_points-self.player2_points) >= lead

    def _tied_game_score(self):
        if self.player1_points >= POINTS_FORTY:
            game_score = "Deuce"
        else:
            tied_score = self.point_map[self.player1_points]
            game_score = f"{tied_score}-all"
        return game_score

    def _currently_leading_player(self):
        return self.player1_name if self.player1_points > self.player2_points else self.player2_name

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1
        else:
            raise ValueError(f"Illegal player provided: '{player_name}'")
