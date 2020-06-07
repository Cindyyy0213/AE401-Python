#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:37:55 2020

@author: Cindy
"""

import turtle
sylvia = turtle.Turtle()
sylvia.shape ("turtle")
sylvia.color ("gold")
canvas = turtle.Screen()
canvas.bgcolor ("black")
for i in range (1):
    j=0    
    while j<100:
        sylvia.forward(10+j/5)
        sylvia.right(10)
        j=j+1;

    sylvia.right(170)
    sylvia.color ("red")    
    while j>0:
        sylvia.forward(10+j/5)
        sylvia.left(10)
        j=j-1;
    
    
turtle.done()
turtle.bye()
    
    