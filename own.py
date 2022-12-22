def encrypt(plaintext, key):
  ciphertext = ""
  for ch in plaintext:
    if ch.isalpha():
      stayInAlphabet = ord(ch)
      if ch.isupper():
        start = ord('A')
      else:
        start = ord('a')
      stayInAlphabet -= start
      newChar = key[stayInAlphabet]
      ciphertext += newChar
    else:
      ciphertext += ch
  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ""
  for ch in ciphertext:
    if ch.isalpha():
      idx = key.index(ch)
      if ch.isupper():
        start = ord('A')
      else:
        start = ord('a')
      idx += start
      newChar = chr(idx)
      plaintext += newChar
    else:
      plaintext += ch
  return plaintext

encrypted_message = encrypt("hello", "zyxwvutsrqponmlkjihgfedcba")
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, "zyxwvutsrqponmlkjihgfedcba")
print(decrypted_message)
