# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:26:04 2021
@author: goksun
Simple Substitution Cipher
"""

msg = input("Plain text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = "qwertyuopasdfghjklizxcvbnm"

msg = msg.lower()
for char in msg:
    if char == ' ':
        continue
    index = alphabet.index(char)
    msg = msg.replace(char, letters[index])

print("Encrypted text: " + msg)
