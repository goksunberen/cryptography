# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:28:33 2021
@author: goksun
RSA Algorithm
"""

msg = int(input("Message in numeric form: "))

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
        return x0
    else:
        print("No solution.")
        
p = int(input("First prime number: "))
q = int(input("Second prime number: "))

n = p*q
totient = (p-1)*(q-1)

e = int(input("Choose a value for e: " + "1<e<"+ str(totient) + ": " ))
d = modular_equation_solver(e, 1, totient)

new_msg = (msg)**e % n
print("Encrypted message: " + str(new_msg))