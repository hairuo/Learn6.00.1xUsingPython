#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 07:30:46 2018

@author: cbg
"""

x = int(input('Enter an integer for x:'))
y = int(input('Enter an integer for y:'))
z = int(input('Enter an integer for z:'))
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')