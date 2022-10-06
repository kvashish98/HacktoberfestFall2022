
'''
#  Diffie-Hellman asymmetric key exchange
# 

# define a few functions

def publickey(g,a,p):  
	astar=pow(g,a,p)  # pow(base,exp,m) is equivalent to base**exp mod m
	return astar

# compute super key x given bstar (Bob's public key), a (Alice's private key)
# and the parameter p
def superkey(bstar,a,p): 
	x=pow(bstar,a,p)
	return x

# set the global parameters known to everybody
p=103079
g=7

# here is the private key of Alice -- has to be < p
a=13  
# compute Alice's public key given the global parameters and her private key a
astar=publickey(g,a,p)  
print("the public key of Alice is= ", astar)

# private and public keys for Bob 
b=11     # it is smaller than p
bstar=publickey(g,b,p)
print("the public key of Bob is= ", bstar)

# compute super key x given bstar (Bob's public key), a (Alice's private key)
x= superkey(bstar,a,p)  
print("the superkey is = ", x)

# use the super key to encrypt a number (simple solution)
t=input("Enter the text to be encrypted")
for i in t:
    
print(l)
t=36
encrypted=(t+x) % p
print('encrypted= ', encrypted)

# and to decrypt it
decrypted=(encrypted-x)%p
print('decrypted= ', decrypted)

'''

import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
password = input("Enter encryption password: ")
 
 
def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))

