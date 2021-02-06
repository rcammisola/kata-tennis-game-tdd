import pytest

from tennis_game import TennisGame


def test_score_is_love_all_at_start_of_game():
    game = TennisGame("Federer", "Nadal")

    assert game.score() == "Love-all"


@pytest.mark.parametrize(
    "player1_score, player2_score, expected_score",
    [
        (0, 0, "Love-all"),
        (1, 1, "Fifteen-all"),
        (2, 2, "Thirty-all"),
        (3, 3, "Deuce"),
    ]
)
def test_tied_game_scenarios(player1_score, player2_score, expected_score):
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    for point in range(max(player1_score, player2_score)):
        if point < player1_score:
            game.won_point(player1_name)
        if point < player2_score:
            game.won_point(player2_name)

    assert game.score() == expected_score


@pytest.mark.parametrize(
    "player1_score, player2_score, expected_score",
    [
        (1, 0, "Fifteen-Love"),
        (0, 1, "Love-Fifteen"),
        (3, 1, "Forty-Fifteen"),
    ]
)
def test_standard_in_game_scoring_scenarios(player1_score, player2_score, expected_score):
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    for point in range(max(player1_score, player2_score)):
        if point < player1_score:
            game.won_point(player1_name)
        if point < player2_score:
            game.won_point(player2_name)

    assert game.score() == expected_score
