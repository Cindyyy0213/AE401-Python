#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:37:51 2020

@author: Cindy
"""

import os.path

while True: 
    print('1. 輸入檔案')
    print('2. 統計每個單字')
    print('3. 單字出現次數')
    print('4. 替換單字')
    print('5. 離開系統')
   
    sel=input("請輸入欲執行項目: ")
    
    if sel=="1":
        file=input("檔案名稱：")
        if os.path.isfile(file):
            print("有這個檔案")
            file=open(file, 'r')
            a=file.read()
            file.close()
        
    if sel=="4":
        o=input("輸入你想替換的舊單字: ")
        n=input("輸入想替換的新單字: ")
        a= a.replace(o,n)
        file=input("檔案名稱：")
        b=open(file, 'w')
        file.write(a)
        file.close()
    
    if sel=="5":
        break
        
        
            
            