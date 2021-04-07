# Tennis Game TDD Kata

Code repository to be used as part of the testing workshop. The workshop is based on the TennisGame code kata and 
focuses on TDD to try to encourage people to write tests as well as the refactoring path to show the value of having 
tests in place.

## Desciption

Oh No! You have tripped over the power cord of the Wimbledon Scoreboard during the Men's Final and all of the numbers have reset to zeroes.

To put things right you need to re-calculate the correct scores for the match, all you have at your disposal is a
list of points that have been won in the game so far by each player 

Still, that should be enough... You start coding your solution. But hurry! It needs to be finished before anybody notices.

#### Recap of Tennis Scoring

Games (with advantage)

* Tennis scores are "Love", "Fifteen", "Thirty", "Forty", "[Player] Wins"
* If the score is tied then it is "Love-all" / "Fifteen-all" / "Thirty-all"
* The score is Deuce when both players get to "Forty" points and tied
* Player Advantage (i.e. after deuce) is denoted "Advantage [Player]"
* The score returns to Deuce if the player with Advantage loses the point
* To win the game you must be at least two points ahead of your opponent

Further details:
[https://en.wikipedia.org/wiki/Tennis_scoring_system](https://en.wikipedia.org/wiki/Tennis_scoring_system)

#### Your challenge

1. Return the scoreboard as it stands after all the points from the game so far are entered (e.g. Fifteen-Love after 1 point).
1. There are two players (P1 and P2).

### Environment setup

1. Create a virtual environment using your tool of choice (virtualenv/conda/etc) and install the requirements file with `pip install -r requirements.txt`
1. Set `pytest` as the default test runner PyCharm instructions: https://stackoverflow.com/a/6397315/47026
1. Mark `src` as Sources Root by right clicking on src > Mark Directory As... > Sources Root

### Running the tests

The tests can be setup to run in three different ways:

* Use the Makefile, run `make test` from your terminal
* Run from the terminal: `./scripts/test.sh`
* Run from inside your IDE
    * setup varies depending on editor but the most important thing is to be 
able to mark `src` as the Source Directory for the project so that it is included in the `PYTHONPATH`.

N.B. You may need to run `xcode-select --install` to get the Makefile to work

### Test Driven Development Path (TDD) ###

In the TDD Path of the workshop you start with a blank-ish slate.  

1. Create a unique branch from `master` with the initials of all people working on the branch
1. Follow the rules of TDD to implement the score functionality
    1. Red, write a test for a scenario - no production code can be written until you have a failing unit test
    1. Green, write (just enough) production code to get the test to pass - only write enough code to make it pass
    1. Refactor, take a look at your newly written code and see if you can tidy things up at all
    1. Repeat for the next scenario
1. Every few minutes you should push your changes and switch with your pair - your pair should pull the changes 
and continue where you left off

#### Consider the following while carrying out the task ####

* Run the tests after every change - only takes 1 second to run, ideally
* Commit and push often
* If your tests are not passing, getting them to pass is the top priority

### Covered Scenarios

* Score is "Love-all" at start of game
* Scores is "Fifteen-Love" when player 1 scores the first point
* Scores is "Love-Fifteen" when player 2 scores the first point
* Score is "Forty-Fifteen" when player 1 has scored 3 points and player 2 has scored 1 point
* Score is "Fifteen-all" or "Thirty-all" when scores are tied and players have scored fewer than 3 points
* Score is "Deuce" when both players have scored 3 points
* Score is "Advantage player 1" when player 1 wins the point after Deuce
* Score is "Deuce" when both players have scored 3+ points and the score is tied
* Score is "Player 2 Won" when player 2 has 4+ points and the lead is at least two points

### Details

* Maintained by Rocco Cammisola [@rcammisola](https://www.twitter.com/rcammisola)

Based on code from Emily Bache's repository
[https://github.com/emilybache/Tennis-Refactoring-Kata]()
