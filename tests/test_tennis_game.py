from tennis_game import TennisGame


def test_score_is_love_all_at_start_of_game():
    game = TennisGame("Federer", "Nadal")

    assert game.score() == "Love-all"
