# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:55:11 2023

@author: arnav
"""


n=int(input("Enter Number ="))
count=0
if n == 1 or n== 0:
    print(f"You have entered {n} which is out of scope.")
else:
    for i in range(2,n):
        if n % i == 0:
            count+=1
        else:
            pass
    if count == 0:
        print("The Given number is prime .")
    else:
        print("The Given number is not a prime numner .")
