"""
File: BeeperRow.py
Name: Sophia
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Avoid Off-By-One Bug by adding a
    put_beeper outside the while loop
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
