import math

def to_binary(pt):
    ct = ''.join([format(ord(i), "08b") for i in list(pt)])
    return ct

def to_str(pt):
    result = list(map(lambda x: chr(int(x, 2)), pt))
    return ''.join(result)


def make_blocks(ct, key):
    ct_list = []
    size = len(key)
    num_iter = math.floor(len(ct)/len(key))
    for i in range(num_iter):
        ct_list.append(ct[i*size:(i+1)*size])
    return ct_list

def merge_blocks(ct_list):
    return ''.join(ct_list)

def single_xor(ct_block, key):
    result = []
    c = list(map(int, ct_block))
    k = list(map(int, key))
    for i, j in zip(c, k):
        result += [str(i^j)]
    return ''.join(result)

def check_match(ct, pt):
    if ct==pt:
        return "Plaintext and ciphertext are matching"
    else:
        return "Plaintext and ciphertext are not matching"


def xor_encrypt(ct, key):
    #Implementing ECB
    ct_list = make_blocks(ct, key)
    result_list = []
    for ct_block in ct_list:
        result_list += single_xor(ct_block, key)
    result = merge_blocks(result_list)
    return result

def xor_decrypt(ct, key):
    #Implementing ECB
    ct_list = make_blocks(ct, key)
    result_list = []
    for ct_block in ct_list:
        result_list += [single_xor(ct_block, key)]
    result = to_str(result_list)
    return result

KEY = '10101001'
PT = "hi"
MUL = 10 ** 4
PT = PT*MUL
pt = to_binary(PT)

ct = xor_encrypt(pt, KEY)

pt_d = xor_decrypt(ct, KEY)

print(check_match(PT, pt_d))