from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""

def main():
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    while beepers_present():
        pick_beeper()
        move()
        while beepers_present():
           if front_is_clear() :
               move()
        turn_around()
        move()
    put_beeper()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint.w')