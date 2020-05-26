#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:30:42 2020

@author: Cindy
"""
import random
ans = random.randint(1, 5)
guess = int(input("Guess a number between int(1, 5)"))
if ans == guess:             
    print("Bingo!")
else:
    print("Wrong!") 