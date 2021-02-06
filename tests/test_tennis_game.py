from tennis_game import TennisGame


def test_score_is_love_all_at_start_of_game():
    game = TennisGame("Federer", "Nadal")

    assert game.score() == "Love-all"


def test_score_fifteen_love_when_player_1_scores_first_point():
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    game.won_point(player1_name)

    assert game.score() == "Fifteen-Love"


def test_score_love_fifteen_when_player_2_scores_first_point():
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    game.won_point(player2_name)

    assert game.score() == "Love-Fifteen"


def test_score_forty_fifteen_when_players_have_scored_3_1():
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    game.won_point(player1_name)
    game.won_point(player1_name)
    game.won_point(player1_name)
    game.won_point(player2_name)

    assert game.score() == "Forty-Fifteen"
