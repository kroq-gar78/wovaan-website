#!/usr/bin/env python3
from random import randrange, choice
from time import time
from threading import Thread

'''Returns a scramble consisting of a given number of moves which are
randomly selected from a given array of faces and a given array of
modifiers, e.g., no modifier (), prime ('), and two (2).

If the opposite_faces is true, faces are chosen such that no adjacent
moves involve the same or opposite sides.
Opposite sides are determined from the array of given sides,
i.e., elements that are half the array's length away from each other.

Defaults to 3x3x3 with no opposite faces.
'''
def scramble_cube(moves = 25, faces = 'FRUBLD',
        modifiers = ["", "'", "2"], opposite_faces = False):
    facelen = len(faces)
    halflen = facelen >> 1
    ret_sequence = ''
    last = 0
    pot = 0

    for x in range(moves):
        while pot == last or (not opposite_faces and
                (pot == last-halflen or pot == last+halflen)):
            pot = randrange(facelen)
        last = pot

        ret_sequence += faces[pot] + choice(modifiers) + " "
    return ret_sequence

'''Prints a given prompt string and returns the user's input as a float.
If invalid or no input, returns a given default.
'''
def prompt_inspection(default = 15, prompt = 'Session inspection time (default 15s): '):
    print(prompt, end = '')
    try:
        return float(input())
    except:
        return float(default)

'''Counts down a given inspection time which must be interrupted with
the enter key to start the timer, then counts up until interrupted
with enter key again.
Returns the time spent solving, i.e., after inspection.
'''
def prompt_solve(inspection_time):
    penalty = 0 #0 if none, 1 if +2, -1 if DNF
    stop = []
    Thread(target=(lambda stop:stop.append(input())), args=(stop,)).start()
    start = time()
    while not stop:
        if inspection_time > time()-start:
            print('%-3.2f  ' % (inspection_time-time()+start), end='\r')
        elif inspection_time+2 > time()-start:
            penalty = 1
            print('%-5s' % '+2', end='\r')
        else:
            penalty = -1
            print('%-5s' % 'DNF', end='\r')

    stop = []
    Thread(target=(lambda stop:stop.append(input())), args=(stop,)).start()
    start = time()
    ret = 0
    while not stop:
        ret = time()-start
        if penalty <= 0:
            print('%.2f    ' % ret, end='\r')
        else:
            print('%.2f  +2' % ret, end='\r')
    print('%-10s' % '\r')

    if penalty == 0: return ret
    elif penality > 0: return ret+2
    else: return None

'''Prompts for an inspection time to use over the whole session once,
then provides a scramble, waits for the enter key, and calls
prompt_solve n times.

After a given number n solves, prints and returns the session average.
If n is <= 0, iterates until stopped (this is default behaviour).
Regardless of the value of n, the average can be calculated and exited
by typing 'end' insead of a black line after a scramble.
'''
def avg(n = 0):
    arr = []
    dnfs = 0
    inspection_time = prompt_inspection()
    x = 0
    while x <= n if n > 0 else True:
        if x-dnfs > 0:
            print('Solve %d - Current average: %.2f' % (x+1, sum(arr)/(x-dnfs)))
        else:
            print('Solve %d' % (x+1))

        print(scramble_cube(), end='')
        if input() == 'end':
            break

        current_solve = prompt_solve(inspection_time)
        if current_solve != None:
            arr.append(current_solve)
        else:
            dnfs+=1
        x+=1

    ret_avg = sum(arr)/(x-dnfs)
    print('Average of %d: %.2f' % (x, ret_avg))
    return ret_avg

if __name__=="__main__":
    avg()
