import pytest

from tennis_game import TennisGame


# @pytest.mark.parametrize(
#     "player1_score, player2_score, expected_score",
#     [
#         (0, 0, "Love-all"),
#         (1, 1, "Fifteen-all"),
#         (2, 2, "Thirty-all"),
#         (3, 3, "Deuce"),
#         (8, 8, "Deuce"),
#     ]
# )
# def test_tied_game_scenarios(player1_score, player2_score, expected_score):
#     game = play_out_game(player1_score, player2_score)
#
#     assert game.score() == expected_score
#
#
# @pytest.mark.parametrize(
#     "player1_score, player2_score, expected_score",
#     [
#         (1, 0, "Fifteen-Love"),
#         (0, 1, "Love-Fifteen"),
#         (2, 1, "Thirty-Fifteen"),
#         (1, 2, "Fifteen-Thirty"),
#         (3, 1, "Forty-Fifteen"),
#     ]
# )
# def test_standard_in_game_scoring_scenarios(player1_score, player2_score, expected_score):
#     game = play_out_game(player1_score, player2_score)
#
#     assert game.score() == expected_score
#
#
# @pytest.mark.parametrize(
#     "player1_score, player2_score, expected_score",
#     [
#         (4, 3, "Advantage Federer"),
#         (3, 4, "Advantage Nadal"),
#         (9, 8, "Advantage Federer"),
#         (7, 8, "Advantage Nadal"),
#     ]
# )
# def test_score_is_advantage_when_player_wins_point_at_deuce(player1_score, player2_score, expected_score):
#     game = play_out_game(player1_score, player2_score)
#
#     assert game.score() == expected_score
#
#
# @pytest.mark.parametrize(
#     "player1_score, player2_score, expected_score",
#     [
#         (4, 2, "Federer Won"),
#         (4, 0, "Federer Won"),
#         (9, 11, "Nadal Won"),
#     ]
# )
# def test_score_is_player_won_when_over_forty_points_and_leads_by_at_least_two_scores(player1_score,
#                                                                                      player2_score,
#                                                                                      expected_score):
#     game = play_out_game(player1_score, player2_score)
#
#     assert game.score() == expected_score

@pytest.mark.parametrize('p1Points p2Points score'.split(),
                         [
                             (0, 0, "Love-all"),
                             (1, 1, "Fifteen-all"),
                             (2, 2, "Thirty-all"),
                             (3, 3, "Deuce"),
                             (4, 4, "Deuce"),

                             (1, 0, "Fifteen-Love"),
                             (0, 1, "Love-Fifteen"),
                             (2, 0, "Thirty-Love"),
                             (0, 2, "Love-Thirty"),
                             (3, 0, "Forty-Love"),
                             (0, 3, "Love-Forty"),
                             (4, 0, "Federer Won"),
                             (0, 4, "Nadal Won"),

                             (2, 1, "Thirty-Fifteen"),
                             (1, 2, "Fifteen-Thirty"),
                             (3, 1, "Forty-Fifteen"),
                             (1, 3, "Fifteen-Forty"),
                             (4, 1, "Federer Won"),
                             (1, 4, "Nadal Won"),

                             (3, 2, "Forty-Thirty"),
                             (2, 3, "Thirty-Forty"),
                             (4, 2, "Federer Won"),
                             (2, 4, "Nadal Won"),

                             (4, 3, "Advantage Federer"),
                             (3, 4, "Advantage Nadal"),
                             (5, 4, "Advantage Federer"),
                             (4, 5, "Advantage Nadal"),
                             (15, 14, "Advantage Federer"),
                             (14, 15, "Advantage Nadal"),

                             (6, 4, 'Federer Won'),
                             (4, 6, 'Nadal Won'),
                             (16, 14, 'Federer Won'),
                             (14, 16, 'Nadal Won'),

                             (6, 4, 'Federer Won'),
                             (4, 6, 'Nadal Won'),
                             (6, 5, 'Advantage Federer'),
                             (5, 6, 'Advantage Nadal'),
                         ])
def test_get_score_game(p1Points, p2Points, score):
    game = play_out_game(p1Points, p2Points)
    assert game.score() == score


def play_out_game(player1_score, player2_score):
    player1_name = "Federer"
    player2_name = "Nadal"
    game = TennisGame(player1_name, player2_name)

    for point in range(max(player1_score, player2_score)):
        if point < player1_score:
            game.won_point(player1_name)
        if point < player2_score:
            game.won_point(player2_name)

    return game
