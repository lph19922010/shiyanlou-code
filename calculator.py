#!/usr/bin/env python3

import sys

dict1 = {}

def  do_with(str_):
    list1 = []
    list1 = str_.split(':')
    dict1[list1[0]] = list1[1]

def compute(key,value):
    try:
        salary = int(value)
    except ValueError:
        print("Parameter Error")
        exit()
    
    income = salary - salary * 0.165 - 5000

    if income <= 0:
        result = 0
    elif income <=3000:
        result = income * 0.03 - 0
    elif income <= 12000:
        result = income * 0.1 - 210
    elif income <= 25000:
        result = income * 0.2 - 1410
    elif income <= 35000:
        result = income * 0.25 - 2660
    elif income <= 55000:
        result = income * 0.3 - 4410
    elif income <= 80000:
        result = income * 0.35 - 7160
    else:
        result = income * 0.45 - 15160

    after_salary = salary * (1-0.165) - result
    dict1[key] = after_salary

def print1(**dict1):
    for key in dict1:
        print('{}:{:.2f}'.format(key,dict1[key]))
    
if __name__ == "__main__":
   
    for arg in sys.argv[1:]:
        do_with(arg)
    
for key,value in dict1.items():
    compute(key,value)

print1(**dict1)
    

