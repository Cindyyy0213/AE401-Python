#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:16:47 2020

@author: Cindy
"""


scores = []
names = []
num = input ("How many students are there? ")
for i in range (int(num)):
    name = input("What's the student's name? ")
    names.append(str(name))
    score = input("Score: ")
    scores.append(int(score))

print ("\nResults:")
high = 0
for eachScore in scores:
    if eachScore > high:
        high = eachScore
        idx = scores.index(eachScore)
print ("Highest: ", names[idx], ":", high)
       
low = 100
for eachScore in scores:
    if eachScore < low:
        low = eachScore 
        idx = scores.index(eachScore)
print ("Lowest: ", names[idx], ":", low)

total = 0       
for i in range (int(num)):
    total= total+scores[i]
aver = total/int(num)
print ("Average: ", aver)

