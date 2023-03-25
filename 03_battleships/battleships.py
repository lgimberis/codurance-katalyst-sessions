
DEFAULT_BOARD_WIDTH = 7
DEFAULT_BOARD_HEIGHT = 7
class Ship:
    def __init__(self, name, length, quantity, icon):
        self.name = name
        self.length = length
        self.quantity = quantity
        self.icon = icon

    def get_copy(self):
        return Ship(self.name, self.length, self.quantity, self.icon)

    def set_position(self, start, end):
        self.start_x, self.start_y = start
        self.end_x, self.end_y = end

SHIPS = [
    Ship("Carrier", 5, 1, "c"),
    Ship("Destroyer", 4, 2, "d"),
    Ship("Submarine", 3, 2, "s"),
    Ship("Gunship", 2, 1, "g")
]

class Battleships:
    """Represents a self-complete state of a game of Battleships."""

    def __init__(self, board_width=DEFAULT_BOARD_WIDTH, board_height=DEFAULT_BOARD_HEIGHT):
        self.board_width = board_width
        self.board_height = board_height
        self.players = {}

    def assert_player_exists(self, player_id):
        """Raise an exception if given player is not present.
        """
        if player_id not in self.players:
            raise ValueError(f'Player with id {player_id} is not registered.')


    def print(self, player_id):
        """Prints a user-viewable image of the player's board state."""


    def pprint(self, player_id):
        """Prints a terser image of the player's board state."""
        self.assert_player_exists(player_id)
        output = list(" " * self.board_width * self.board_height)
        for ship in self.players[player_id]:
            if ship.start_x == ship.end_x:
                for y in range(ship.start_y, ship.end_y):
                    output[ship.start_x + y * self.board_width] = ship.icon
            else:
                for x in range(ship.start_x, ship.end_x):
                    output[x + ship.start_y * self.board_width] = ship.icon
        for y in range(self.board_height):
            print(''.join(output[y*self.board_width:y*self.board_width + self.board_width - 1]))



    def add_ship(self, player_id, ship, position_string):
        self.assert_player_exists(player_id)
        start, end = position_string.split(" ")
        start_x = ord(start[0].lower()) - ord('a') + 1
        start_y = int(start[1])
        end_x = ord(end[0].lower()) - ord('a') + 1
        end_y = int(end[1])
        ship = ship.get_copy()
        ship.set_position((start_x, start_y), (end_x, end_y))
        self.players[player_id].append(ship)

    def add_player(self, player_id):
        if player_id in self.players.keys():
            raise ValueError(f'Player with id {player_id} is already present')
        print('Please enter your intended placement of ships:')
        print('e.g. "a1 a5" will place a ship of length 5 starting on square a1 and ending on a5')
        self.players[player_id] = []
        for ship in SHIPS:
            for _ in range(ship.quantity):
                user_input = input(f'{ship.name} (Length: {ship.length})')
                print(user_input)
                self.add_ship(player_id, ship, user_input)
