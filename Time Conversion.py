#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    y=len(s)
    a=s[0]+s[1]
    a=int(a)
    for i in range(y):
        if s[8]=="A" and a==12:
            newa="00"
        elif s[8]=="P" and a==12:
            newa="12"
        elif s[8]=="P":
            newa=int(a+12)
        elif s[8]=="A" and a<10:
            newa=int(a)
            newa=str(newa)
            newa="0"+newa
        elif s[8]=="A":
            newa=int(a)
    newa=str(newa)
    latest=newa
    for j in range(2,y-2):
        latest=latest+s[j]
    return latest




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
