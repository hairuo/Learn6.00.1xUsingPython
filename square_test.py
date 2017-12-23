#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:42:41 2017

@author: cloudwater
"""


#def newton(x, y):
#    while not (abs(y*y -16) < 0.01):
#        y = (y + x/y)/2
#    return y
#    
#
#print newton(16, 3)

def check(x, guess):
    return (abs(guess*guess - x) < 0.001)

def newton(x, guess):
    while not check(x, guess):
        guess = (guess + (x/guess)) / 2.0
    return guess
    print(guess)

newton(16, 1)