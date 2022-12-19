KEY = 22
PLAIN_TEXT = "hello world"
PLAIN_TEXT_2 = "a secret key is also known as a private key"


def caeser(mode, text, key):

    charmap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = []
    for i in text:
        if i in charmap:
            new_text = charmap[(charmap.index(i) + key) % 26] if mode == "encrypt" else charmap[
                (charmap.index(i) - key + 26) % 26]
            result.append(new_text)
        else:
            result.append(i)
    return "".join(result)


ciphertext = caeser("encrypt", PLAIN_TEXT, KEY)
print("Plaintext: ", PLAIN_TEXT)
print("Ciphertext: ", ciphertext)
#print("Decrypted text: ", caeser("decrypt", ciphertext, KEY))


def bruteforce(ct):
    for i in range(26):
        print("decrypted text: ", caeser("decrypt",ct, i), "| key: ", i)
        
bruteforce(ciphertext)