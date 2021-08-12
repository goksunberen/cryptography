# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:04:29 2021
@author: goksunberen
Caesar Cipher
"""

msg = input("Plain text: ")
new_msg = ""
shift = 2

msg = msg.lower()
for char in msg:
    code = ord(char)
    if code >= 97 and code <= 122:
        if code == 122:
            code = 96
        elif code == 121:
            code = 95
        character = chr(code + shift)
        new_msg = new_msg + character
    else:
        new_msg = new_msg + ' '

print("Encrypted text: " + new_msg)
