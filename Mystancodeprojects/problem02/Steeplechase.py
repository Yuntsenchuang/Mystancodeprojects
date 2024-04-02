"""
File: Steeplechase.py
Name: Sophia
---------------------------------
This file shows how to make Karel cross hurdles
in a 12x12 world with a for loop
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    # Karel is facing East
    for i in range(11):
        # Karel hasn't reach the wall
        if front_is_clear():
            move()
        # Karel is on the left side od the wall
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the right side of the wall, facing South
    """
    up()
    cross()
    down()


def up():
    """
    Karel move north along the east wall
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is at the upper left of the wall, facing North
    """
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
    Karel move east
    Pre-condition: Karel is at the upper left of the wall, facing North
    Post-condition: Karel is at the upper right of the wall, facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    Karel move south along the west wall to the ground
    Pre-condition: Karel is at the upper right, facing South
    Post-condition: Karel is on the right side of the wall, facing South
    """
    while front_is_clear():
        move()


def turn_right():
    """
    Karel will turn right
    """
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
