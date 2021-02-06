from tennis_game import TennisGame


def test_using_tennis_game_in_project():
    game = TennisGame("Federer", "Nadal")

    assert game.score() is None
