#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 07:27:36 2018

@author: cbg
"""

x = int(input('Enter an integer for x:'))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
else:
    print('Divisible by 3 and not by 2')
    
