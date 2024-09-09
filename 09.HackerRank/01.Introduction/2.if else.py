import math
import os
import random
import re
import sys

def weird(n):
    if 1<=n<=100:
        if n%2 == 1:
            print("Weird")
        elif n%2 == 0 and 2<=n<=5:
            print("Not Weird")
        elif n%2 == 0 and n>=6 and n<=20:
            print("Weird")
        elif n%2 == 0 and n>20:
            print("Not Weird")

if __name__ == "__main__":
    n=int(input().strip()) #.strip() elimina los espacios de las funciones
    weird(n)
    assert weird(3)=="Weird"
    assert weird(24)=="Not Weird"
    assert weird(4)=="Not Weird"