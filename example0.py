#!python3

""" the time module """

import time

"""
time is measure in 'epoch time' which is the number 
of seconds that have elapsed since Jan 1, 1970, 
kind of like the beginning of the computer age
"""

x = time.time()
'''
time.time() finds the current epoch time and returns
it as a float value
'''
print(x)

time.sleep(3.5)
'''
sleep() will pause the program for a certain number of seconds before
continuining
'''
print("I went to sleep for 3.5 seconds")
now = time.time()
print(f"elapsed time: {now - x} seconds")