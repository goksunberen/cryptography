# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:38:18 2021
@author: goksun
ROT13
"""

msg = input("Plain text: ")
new_msg = ""
shift = 13

msg = msg.lower()
for char in msg:
    code = ord(char)
    if code >= 97 and code <= 122:
        character = chr((code + shift - 97) % 26 + 97)
        new_msg = new_msg + character
    else:
        new_msg = new_msg + ' '

print("Encrypted text: " + new_msg)