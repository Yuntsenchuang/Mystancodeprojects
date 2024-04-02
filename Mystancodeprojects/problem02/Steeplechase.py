"""
File: Steeplechase.py
Name: Sophia
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        # Karel is facing East
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()
            # Karel is facing East


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
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is at the upper left, facing North
    """
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
    Pre-condition: Karel is at the upper left, facing North
    Post-condition: Karel is at the upper right, facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    Pre-condition: Karel is at the upper right, facing South
    Post-condition: Karel is on the right side of the wall, facing South
    """
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
