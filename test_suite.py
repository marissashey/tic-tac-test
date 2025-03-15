import pytest
from tictactoe import TicTacToe

@pytest.fixture 
def game(): # for directly modifying instance attributes 
    new_game_instance = TicTacToe()
    yield new_game_instance  

@pytest.fixture
def game_factory(monkeypatch): # for passing inputs with full playthroughs

    def game_instance(inputs):
        preloaded_game_instance = TicTacToe()
        input_iter = iter(inputs)

        def mock_input(prompt):
            return next(input_iter)
        
        monkeypatch.setattr('builtins.input', mock_input)
        return preloaded_game_instance
    
    return game_instance

def test_initial_state(game):
    expected_ledger = {str(val): None for val in range(1,10)}
    assert game.ledger == expected_ledger

    expected_display = [[1,2,3],[4,5,6],[7,8,9]]
    assert game.display == expected_display
    assert game.token == "x"
    assert not game.game_over


def test_taking_turns(game):

    game.update_turn()
    assert game.token == "o"
    
    game.update_turn()
    assert game.token == "x"




def test_x_wins(game_factory):
    """
    |x|o|x|
    |x|o|o|
    |x|8|9|
    """
    inputs = ["1", "2", "3", "5", "4", "6", "7"]
    game = game_factory(inputs)
    game.play()

    assert game.game_over
    assert game.outcome["x"] is True
    assert game.outcome["o"] is False
    assert game.outcome["tie"] is False


def test_initially_invalid_input(game_factory):
    # this is just the `test_x_wins` inputs with some faulty inputs in front, so it should yield an x win. 
    faulty_inputs = ["asdf", "0", 10, "10", 1, 
              "1", "2", "3", "5", "4", "6", "7"]

    game = game_factory(faulty_inputs)
    game.play()
    
    assert game.game_over
    assert game.outcome["x"] is True
    assert game.outcome["o"] is False
    assert game.outcome["tie"] is False


def test_tie(game_factory):
    """
    |x|o|x|
    |x|o|o|
    |o|x|x|
    """
    inputs = ["1", "2", "3", "5", "4", "6", "8", "7", "9"]
    game = game_factory(inputs)
    game.play()

    assert game.game_over
    assert game.outcome["x"] is False
    assert game.outcome["o"] is False
    assert game.outcome["tie"] is True