<<<<<<< Updated upstream
"""
Sprite Collect Coins with Background

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins_background
"""
import random
import arcade
import os

PLAYER_SCALING = 0.5
COIN_SCALING = 0.25

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins with Background Example"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Background image will be stored in this variable
        self.background = None

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.score_text = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        # Image from:
        # https://wallpaper-gallery.net/single/free-background-images/free-background-images-22.html
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite(":resources:fonts/ttf/playerShip1_green.png",
                                           PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(100):

            # Create the coin instance
            coin = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk2.png", COIN_SCALING)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on the coin sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
=======
class Room:
    """
    this class represents the room in the playing area
    """

    def __init__(self, name, descr, north, east, south, west, go_up, go_down):
        """ This is a method that sets up the variables in the object. """
        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = go_up
        self.down = go_down

def main():
    """ This is my main program function:
    """
    room_list = []
    names = ['Bedroom', 'Living Room','Kitchen', 'Dining Room', 'Attic', 'Play room']
    descriptions = [
        'You are in the Bedroom. Be careful not to wake the sleeping child. The door leading to the'
        'You are standing on a wooden floor with toys laid out across the room. Play Room has been '
        'blocked. To the north, there are stairs leading to the Living Room. You walk down the stairs.'
        'You are in the Living room. With chairs and sofas made of stone and a fireplace built into the wall.'
        'North from the Living Room is a door leading to the Kitchen. You walk through the door. '
        'You are in the Kitchen. It is filled with cabinets and a sink in the far corner. There is a fridge on '
        'the wall. A slanted one. To the east is the Dining Room. You enter the door. You are in the Dining Room.'
        'The dining table is made of stone and has many cracks on the surface. The marble floor never shines.'
        'Then, you walk up the spiral staircase. You are in the Attic. At the top floor, there are many unopened'
        'boxes. No one knows what is inside of them. Old furniture is stored here. You move south, down the stairs'
        'You are in the Play Room. There are several draws with paint and toys. To the west is the blocked'
        'door leading to the Bedroom.'
    ]
    norths = [3, 2, None, 3, 2, None]
    easts = [None, None, None, 2, 2, 2]
    souths = [None, 2, 3, None, 2, 3]
    wests = [2, 2, 2, None, None, None]
    ups = [None, None, 2, None, 3, 2]
    downs = [3, 3, 2, 3, None, 2]
    for i in range(len(names)):
        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    current_room = 1
    done = False
    while not done:
        print(room_list[current_room].description)
        answer = input('What do you want to do? Enter n for north, e for east, s for south, w for west, u for up, '
                       'd for down, q to quit: ')
        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == 'n':
            new_room = room_list[current_room].north
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'e':
            new_room = room_list[current_room].east
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'w':
            new_room = room_list[current_room].west
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 's':
            new_room = room_list[current_room].south
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'u':
            new_room = room_list[current_room].up
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'd':
            new_room = room_list[current_room].down
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'q':
            print('Goodbye. I hope you liked exploring the dungeon.')
            done = True
        else:
            print('Sorry, I did not understand your answer')


main()
>>>>>>> Stashed changes
