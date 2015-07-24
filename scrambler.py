#!/usr/bin/env python
'''Returns a scramble in cube notation consiting of 
a given number of moves which in turn are randomly selected from
a given array of faces and a given array of modifiers, e.g., 
No modifier (), prime ('), and two (2).

If the last arg is true, faces are chosen such that no adjacent
moves do not involve the same or opposite sides. Opposite sides are determined from the array
of given sides, i.e., elements that are half the array's length
away from each other.

Defaults to 3x3x3.
'''

from random import randrange, choice

def scramble_cube(moves = 25, faces = 'FRUBLD', 
        modifiers = ["", "'", "2"], opposite_faces = False):
    facelen = len(faces)
    halflen = facelen >> 1
    ret_sequence = ''
    last = 0
    pot = 0
    
    for x in range(moves):
        while pot == last or (not opposite_faces and (pot == last-halflen or pot == last+halflen)):
            pot = randrange(facelen)
        last = pot
        
        ret_sequence += faces[pot] + choice(modifiers) + " "
    return ret_sequence

for s in range(10):
	print scramble_cube()
