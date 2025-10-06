#https://www.codewars.com/kata/5270f22f862516c686000161/train/python
'''
Base64 Encoding 5kyu

Base64 encoding lets you represent arbitrary binary data as ASCII-safe text. Your task is to provide both the encoder and decoder to convert to and from Base64.

Create two functions that can convert from binary data to a Base64 encoded string, and vice versa:

def to_base_64(data: bytes) -> str: ...
def from_base_64(encoded: str) -> bytes: ...

While many Base64 implementations use = padding characters, your functions should not use padding.

Can you come up with your own encoder and decoder rather than use your language's base64 implementation?

Example (input -> output):
b'this is a bytestring!' -> "dGhpcyBpcyBhIGJ5dGVzdHJpbmch"
b'\x00' -> "AA"  RM:  \x00 is ASCII, not a base64 string.
'''
import base64
#Encode strings
message = "this is a bytestring!"
message = "\x00"
message = "Python is fun"
messagebytes = message.encode("ascii") #Convert to bytes
print(messagebytes) #print b'Python is fun'
base64bytes = base64.b64encode(messagebytes) #Encode to Base64
print(base64bytes) #print b'UHl0aG9uIGlzIGZ1bg=='
base64message = base64bytes.decode("ascii") #String representation of the Base64 conversion.  Decode as ASCII.
base64messagenopadding = base64message.rstrip('=') #remove padding or equal signs
print(base64messagenopadding) #print UHl0aG9uIGlzIGZ1bg
#Decode strings
base64message = "dGhpcyBpcyBhIGJ5dGVzdHJpbmch"
base64message = "AA=="
base64message = "UHl0aG9uIGlzIGZ1bg=="
base64bytes = base64message.encode("utf-8") #Encode message to bytes
print(base64bytes) #print b'UHl0aG9uIGlzIGZ1bg=='
messagebytes = base64.b64decode(base64bytes) #Decode
print(messagebytes) #print b'Python is fun'
message = messagebytes.decode("utf-8") #Decode to a string
print(message) #print Python is fun
#Decode strings without decoding to string
base64message = "AA"
print(base64message)
print(type(base64message))
base64message += '=' * (-len(base64message) % 4) #Add padding if necessary
print(base64message)
print(type(base64message))
base64bytes = base64message.encode("utf-8") #Encode message to bytes
print(base64bytes) #print b'AA=='
print(type(base64bytes))
messagebytes = base64.b64decode(base64bytes) #Decode.  Not decoding to a string.
print(messagebytes) #print b'\x00'

def to_base64(data: bytes) -> str:
    encoded_bytes = base64.b64encode(data)
    encoded_no_padding_bytes = encoded_bytes.rstrip(b'=')
    base64_string_no_padding = encoded_no_padding_bytes.decode('ascii')
    return base64_string_no_padding


print(to_base64(b"this is a bytestring!")) #print dGhpcyBpcyBhIGJ5dGVzdHJpbmch
print(to_base64(b"Hello World")) #print dGhpcyBpcyBhIGJ5dGVzdHJpbmch
print(to_base64(b"\x00")) #print AA
print(to_base64(b"Python is fun")) #print UHl0aG9uIGlzIGZ1bg
print(to_base64(b"the quick brown fox jumps over the white fence. ")) #print dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g


def from_base64(encoded: str) -> bytes:
    missingpadding = len(encoded) % 4
    addmissingpadding = "=" * (4 - missingpadding)
    encoded += addmissingpadding
    encoded_bytes = encoded.encode('ascii')
    decoded_bytes = base64.b64decode(encoded_bytes)
    return decoded_bytes


print(from_base64("dGhpcyBpcyBhIGJ5dGVzdHJpbmch")) #print b'this is a bytestring!'
print(from_base64("SGVsbG8gV29ybGQ")) #print b'Hello World'
print(from_base64("AA")) #print b'\x00'
print(from_base64("AA==")) #print b'\x00'
print(from_base64("dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g")) #print b'the quick brown fox jumps over the white fence. '

#User solution
import base64
def to_base_64(data: bytes) -> str:
    return base64.b64encode(data).rstrip(b'=').decode('latin1')


def from_base_64(encoded: str) -> bytes:
    encoded = ''.join(encoded)
    encoded += '=' * (-len(encoded) % 4)
    return base64.b64decode(encoded.encode('utf-8'))
