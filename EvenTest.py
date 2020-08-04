#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:33:05 2020

@author: Cindy
"""

def EvenTest():
    num=input("Enter a number: ")
    if int(num)%2==0:
        return("This is an even number.")
    elif int(num)%2==1:
        return("This is an odd number.")

    