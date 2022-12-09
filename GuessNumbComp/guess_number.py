# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

***This is a program for the computer 
to guess the number you are thingking***
"""
import random

def guess():
    low = 1
    high= 1000
    print("Think of a random number between ",low," and ",high)
    print("Now let the computer guess the number..")
    rand1 = random.randint(low,high)
    guess = 0
    
    while rand1 != guess:
        value = input(f'Is {rand1} your guess H:to high L:too low C:correct').lower()
        if value == 'h':
            high = rand1 - 1
            print (high, low)
            rand1 = random.randint(low,high)
        elif value == 'l':
            low = rand1 + 1
            print (high, low)
            rand1 = random.randint(low,high)
        elif value == 'c':
            guess = rand1
            print("yay it guessed")
        else:
            print("wrong input")
                
        
    
guess()
