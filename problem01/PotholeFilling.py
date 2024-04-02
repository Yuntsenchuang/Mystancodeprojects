"""
File: PotholeFilling.py
Name: Sophia
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre_condition: Karel is at the (2, 1)
    Post-condition: Karel is at the (2, 7)
    Karel will go in, put 99 beepers and go out from the pothole for three pothole
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()


def go_in():
    """
    Pre_condition: Karel is at the upper left of the pothole, facing East
    Post-condition: Karel is in the pothole, facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    Pre_condition: Karel is in the pothole, facing South
    Post-condition: Karel is at the upper left of the pothole, facing East
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    """
    Karel will turn right
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel will turn around
    """
    turn_left()
    turn_left()


def put_99():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
