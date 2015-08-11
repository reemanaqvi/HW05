#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(count, userName):
    print "%s walks through the door to see a dimly lit hallway." %(userName)
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' %(userName)
        if (count >= 0) and (count < 5):
            print "but %s is not happy about it" %(userName)
        infinite_stairway_room(count + 1, userName)
    option_2 = "You're never getting out"
    if next == option_2:
        pass


def gold_room(userName):
    print "This room is full of gold.  How much do %s take?" %(userName)

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.") 

    if how_much < 50:
        print "Nice, %s is not greedy, %s win!" %(userName, userName)
        exit(0)
    else:
        dead("%s greedy bastard!") %(userName)


def bear_room(userName):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" %(userName)
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or "honey":
            dead("The bear looks at %s then slaps your face off.") %(userName)
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." %(userName)
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off.") %(userName)
        elif next == "open" or  "door" and bear_moved:
            gold_room(userName)
        elif next == "escape":
            infinite_stairway_room(0, userName)
        else:
            print "I got no idea what that means."


def cthulhu_room(userName):
    print "Here %s sees the great evil Cthulhu." %(userName)
    print "He, it, whatever stares at %s and you go insane." %(userName)
    print "Does %s flee for his/her life or eat %s's head?" %(userName, userName)

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(userName)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    userName = sys.argv[1]
    print "%s is in a dark room." %(userName)
    print "There is a door to %s's right and left." %(userName)
    print "Which one does %s take?" %(userName)

    next = raw_input("> ")

    if next == "left":
        bear_room(userName)
    elif next == "right":
        cthulhu_room(userName)
    else:
        dead("%s stumbles around the room until %s starves.") %(userName)

if __name__ == '__main__':
    main()
