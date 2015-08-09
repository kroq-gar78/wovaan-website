#!/usr/bin/env python3
from random import randrange, choice
from math import ceil
'''For any cube of dimensions NxNxN, returns a scramble consisting of a 
given number of moves in WCA notation for 2x2x2-4x4x4 and prefix 
notation for 4x4x4 and bigger.

The same face will not be moved twice in a row and no two adjacent turns
will result in the equivalent of a cube rotation.

Defaults to 3x3x3.
'''
def scramble_cube(n = 3, moves = 25):
    assert n > 1
    half = n >> 1
    ret = ''
    last = (0, 0, 0) #Turns are of form [face, depth, direction]
    opposite_last = (0, 0, 0)
    turn = (0, 0, 0)
    
    for x in range(moves):
        while turn[0] == last[0] or (turn[0] == opposite_last[0] and 
                 turn[1] == opposite_last[1] == half and (n&1) == 0):
            turn = (randrange(6), randrange(half)+1, randrange(3))
        
        last = turn
        opposite_last = (turn[0]-3 if turn[0]-3 > 0 else turn[0]+3,
                        n-turn[1],
                        0 if turn[2] == 1 else 1 if turn[2] == 0 else 2)
        
        if turn[1] >= 2 and n != 4: 
            ret += str(turn[1]) 
        ret += 'FRUBLD'[turn[0]]
        if turn[1] == 2 and n == 4: 
            ret += 'w'
        ret += ('', '\'', '2')[turn[2]]
        ret += ' '
    
    return ret


'''Returns a scramble consisting of a given number of moves which are
randomly selected from a given array of faces and a given array of 
modifiers, e.g., no modifier (), prime ('), and two (2).

The same face will not be moved twice in a row.

Defaults to megaminx.
'''
def scramble_non_cube(
        moves = 25, 
        faces = ('U', 'U\'', 'R++', 'R--', 'D++', 'D--'),
        modifiers = []):
    facelen = len(faces)
    half = facelen >> 1
    ret = ''
    last = 0
    turn = 0
    
    for x in range(moves):
        while turn == last:
            pot = randrange(facelen)
        last = pot
        
        ret += faces[pot] + choice(modifiers) + " "
    return ret

if __name__=='__main__':
    import sys
    l = len(sys.argv)
    if l >= 2 and sys.argv[1] == 'noncube':
        for x in range(10):
            print(scramble_non_cube())
    for x in range(10 if l <= 2 else int(sys.argv[2])):
        print(scramble_cube(3 if l <= 1 else int(sys.argv[1]), 25 if l <= 3 else int(sys.argv[3])))
