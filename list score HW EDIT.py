#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:55:55 2020

@author: Cindy
"""
num = input ("How many students are there?")
for i in range (int(num)):
    name = input("Please insert names: ")
    score = input("Scores: ")
    Classmates = []
    Classmates.append(name)
    Classmates.append(int(score))
    scores = []
    scores.append(Classmates)

high=0
for each_classmates in scores:
    if each_classmates in scores:
        if each_classmates[1]>high:
            high = each_classmates[1]
            high_name = each_classmates[0]
print("Highest", high)
print(high_name)

def printhigh():
    return'high'
            
low=100
for each_classmates in scores:
    if each_classmates in scores:
        if each_classmates[1]<low:
            low = each_classmates[1]
            low_name = each_classmates[0]
print ("Lowest: ", low)
print(low_name)
def printlow():
    return'low'
            
total = 0
for i in scores:
    total= total + i[1]
aver=total//int(num)
print("Average", aver)
def printaver():
    return'Average'




