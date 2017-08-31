"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joshua Osborne.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 10  # Fast

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red',3)
red_turtle.speed = 20

# The first square will be 300 x 300 pixels:
blue_size = 300
red_size = 50

# Do the indented code 20 times.  Each time draws a square.
for k in range(20):
    # Blue Turtle Loop
    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(blue_size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10+k)
    blue_turtle.left(45-k)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    blue_size = blue_size - 12
    # Red Turtle Loop
    red_turtle.draw_circle(red_size)

    red_turtle.pen_up()
    red_turtle.right(k)
    red_turtle.forward(k)
    red_turtle.left(-k)

    red_turtle.pen_down()
    red_size = red_size - 12


window.close_on_mouse_click()