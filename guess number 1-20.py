#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:15:25 2020

@author: Cindy
"""


import random
ans = random.randint(1, 20)
gameCnt = 0;
cnt = 0;
totalCnt = 0;
while cnt < 5:
    guess = int(input("Guess a number between int(1, 20)"))
    if guess == ans:
        gameCnt = gameCnt + 1;
        totalCnt = totalCnt + cnt + 1;
        print("bingo!")
        ans2 = str(input("Continue? y/n =>"))
        if ans2 == 'y':
            cnt=0;
            continue;
        else:
            break;
    elif cnt == 4:
        gameCnt = gameCnt + 1;
        totalCnt = totalCnt + cnt + 1;
        print ("wrong!")
        ans2 = str(input("Continue? y/n =>"))
        if ans2 == 'y':
            cnt=0;
            continue;
        else:
            break;
    elif guess>ans:
        print("smaller")
    elif guess<ans:
        print("bigger")
    else:
        print ("wrong!")
    cnt = cnt + 1;  
    
print("Total played ", gameCnt, " times, average count = ", totalCnt/gameCnt)