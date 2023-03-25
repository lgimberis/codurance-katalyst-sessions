import unittest
from unittest.mock import call, patch
import battleships

BOARD_WIDTH = 7
BOARD_HEIGHT = 7

class TestAddPlayer(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def testCreateValidPlayer(self, mocked_input, mocked_print):
        """Test creating a sensible player board.

        """
        b = battleships.Battleships(board_width=BOARD_WIDTH, board_height=BOARD_HEIGHT)
        mocked_input.side_effect = ["a1 a5", "b1 b4", "c1 c4", "d1 d3", "e1 e3", "f1 f2"]
        calls = [call(" "*7), call(" "*7), call("c       "), call("cdd    "), call("cddss  "), call("cddssg "), call("cddssg ")]
        b.add_player(1)
        mocked_print.assert_has_calls(calls, any_order = False)

if __name__=="__main__":
    unittest.main()
