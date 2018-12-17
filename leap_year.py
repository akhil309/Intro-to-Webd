#https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(y):
    leap="False"
    if(y%4==0):
        if(y%100!=0):
            leap="True"
        elif(y%400==0):
            leap="True"
        
    return leap


