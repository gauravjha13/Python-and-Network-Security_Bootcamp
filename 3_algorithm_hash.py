# WAP in Python to generate hashes of string data using 3 algorithms from hashlib.

import hashlib

text = input("Enter the text to be hashed :  ")

hashed_text_sha512 = hashlib.sha512(text.encode())
hashed_text_blake2b = hashlib.blake2b(text.encode())
hashed_text_shake256 = hashlib.shake_256(text.encode())

print("---------------OUTPUT---------------")
print("Text: ", text)
print("Hashed Text (sha512):   ", hashed_text_sha512.hexdigest())
print("Hashed Text (blake2b):  ", hashed_text_blake2b.hexdigest())
print("Hashed Text (shake256): ", hashed_text_shake256.hexdigest(64))