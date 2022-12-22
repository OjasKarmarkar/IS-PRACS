key = input("Enter the key : ")
pt = input("Enter the pt : ").replace(' ' , '')

pt = list(pt)
og = list(key)
s = sorted(key)

order = []
rows = len(pt)//len(key) if len(pt)%len(key)==0 else (len(pt)//len(key))+1
matrix = [ [] for _ in range(rows) ]

for i in range(len(key)):
        order.append(og.index(s[i]))
        og[og.index(s[i])]="#"

col_empty = []


def encrypt(matrix , key , order):
    k=0
    for i in range(rows):
        for j in range(len(key)):
            if k<len(pt):
                matrix[i].append(pt[k])
            else:
                matrix[i].append('')
            k+=1

    print(matrix)
    ct = []
    for i in range(len(order)):
        col_ix = order.index(i)
        for row_ix in range(rows):
            if matrix[row_ix][col_ix]=='':
                col_empty.append(col_ix)
            ct.append(matrix[row_ix][col_ix])

    ct=''.join(ct)
    print("Encrypted text is " + ct)
    return ct

def decrypt(ct):
    matrix = [ ['' for i in range(len(key))] for _ in range(rows) ]
    str_ix = 0
    for i in range(len(order)):
        k=0
        col_ix = order.index(i)
        while k<rows:
            if col_ix in col_empty and k==rows-1:
                matrix[k][col_ix] = ''
            else:
                matrix[k][col_ix] = ct[str_ix]
                str_ix+=1

            k+=1

    pt = []
    for i in range(rows):
            for j in range(len(key)):
                pt.append(matrix[i][j])

    pt=''.join(pt)
    print("Decrypted text is : " + pt)
    return pt

ct = encrypt(matrix , key , order)
pt = decrypt(ct)
print(pt)
