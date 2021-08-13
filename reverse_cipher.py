# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:50:17 2021
@author: goksun
Reverse Cipher
"""

msg = input("Plain text: ")
new_msg = ""

for index in range(0, len(msg))[::-1]:
    new_msg = new_msg + msg[index]
    
print("Encrypted text: " + new_msg)