# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:26:04 2021
@author: goksun
Simple Substitution Cipher
"""

msg = input("Plain text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
letters =  "qwertyuopasdfghjklizxcvbnm"
new_msg = ""


msg = msg.lower()
for char in msg:
    if char == ' ':
        new_msg = new_msg + ' '
        continue
    index = alphabet.index(char)
    new_msg = new_msg + letters[index]

print("Encrypted text: " + new_msg)
