# WAP in Python to generate MD5 of string data
import hashlib
result = hashlib.md5(b'ShapeAI')
print("The byte equivalent of hash is : ", end = " ")
print (result.digest())

# WAP in Python to generate hashes of string data using 3 algorithms from hashlib.
int_val = 13
str_val = 'ShapeAI'
flt_val = 13.56

print ("The integer hash value is : " + str(hash(int_val)))
print ("The string hash value is : " + str(hash(str_val)))
print ("The float hash value is : " + str(hash(flt_val)))

# Add Salting and Iteartion to your hashes.