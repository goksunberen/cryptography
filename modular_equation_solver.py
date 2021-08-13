# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:28:33 2021
@author: goksun
Modular Equation Solver

for example: 28x ≡ 4 (mod 12) would be a=28, b=4, n=12
"""

def extended_euclid(a,b):
    if b == 0:
        return (a,1,0)
    else:
        (d1,x1,y1) = extended_euclid(b, a%b)
        (d,x,y) = (d1,y1,x1 - (a//b) * y1)
        #print(d,x,y)     Print function to see the steps
        return (d,x,y)
    
def modular_equation_solver(a,b,n):
    (d,x1,y1) = extended_euclid(a,n)
    if b%d == 0:
        x0 = (x1*(b//d)) % n
        for i in range(0,d):
            print("x" + str(i) + " = " + str((x0 + i * (n//d)) % n))
    else:
        print("No solution.")