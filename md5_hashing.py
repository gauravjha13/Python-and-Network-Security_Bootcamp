# WAP in Python to generate MD5 of string data

import hashlib

text = input("Enter the text to be hashed :  ")

hashed_text = hashlib.md5(text.encode())

print("---------------OUTPUT---------------")
print("Text: ", text)
print("Hashed Text: ", hashed_text.hexdigest())
