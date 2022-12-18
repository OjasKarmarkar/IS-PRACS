pt = input("Enter PlainText : ").replace(" " , "").upper()
key = input("Enter Key : ").replace(" " , "").upper()

def generateKey(pt , key):
    key = list(key)
    if len(key) == len(pt):
        return key
    else:
        diff = len(pt) - len(key)
        for i in range(diff):
            key.append(key[i % len(key)])
    return key

def encryption(pt, key):
  encrypt_text = []
  for i in range(len(pt)):
    x = (ord(pt[i]) +ord(key[i])) % 26
    x += ord('A')
    encrypt_text.append(chr(x))
  return("" . join(encrypt_text))

def decryption(ct, key):
    orig_text = []
    for i in range(len(ct)):
        x = (ord(ct[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

keyStream = generateKey(pt , key)
ct = encryption(pt , keyStream)
print(ct)
print(decryption(ct , keyStream))
