# Add Salting and Iteartion to your hashes.

import hashlib
import os

text = input("Enter the text to be hashed :  ")

text = text.encode()
salt = os.urandom(16)
hashed_text = hashlib.pbkdf2_hmac("sha256", text, salt, 10)

print("---------------OUTPUT---------------")
print("Text: ", text)
print("Hashed Text (Applied salt and iterated 10 times): ", hashed_text.hex())
