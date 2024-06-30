<<<<<<< Updated upstream
"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.AQUA)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,599, 300, 0, arcade.csscolor.SEA_GREEN)
=======
import arcade.csscolor

arcade.open_window(600, 600, "Google 2.0")

arcade.set_background_color(arcade.csscolor.CYAN)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.GREEN)
>>>>>>> Stashed changes

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

<<<<<<< Updated upstream
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400,400,370,320,430,320, arcade.csscolor.DARK_GREEN)

arcade.draw_text("Plant a Tree, Offset your CO2", 100, 230, arcade.color.GOLD, 24)

arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()


=======
arcade.draw_rectangle_filled(200, 340, 80, 80, arcade.csscolor.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(200, 320, 20, 40, arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(300, 350, 30, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(400, 340, 80, 80, arcade.csscolor.ANTIQUE_WHITE)
arcade.draw_rectangle_filled(400, 320, 20, 40, arcade.csscolor.SIENNA)

arcade.draw_text("Plant a tree, get stung by bees.", 100, 230, arcade.color.DARK_GREEN, 24)

arcade.draw_text("What a boring village.", 100, 200, arcade.color.ASH_GREY, 24)

arcade.finish_render()

arcade.run()
>>>>>>> Stashed changes
