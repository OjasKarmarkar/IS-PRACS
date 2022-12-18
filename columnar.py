key = input("Enter the key : ")
pt = input("Enter the pt : ").replace(' ' , '')

pt = list(pt)
og = list(key)
s = sorted(key)

order = []
rows = len(pt)//len(key) if len(pt)%len(key)==0 else (len(pt)//len(key))+1
matrix = [ [] for _ in range(rows) ]

for char in s :
    order.append(og.index(char))



def encrypt(matrix , key , order):
    k=0
    for i in range(rows):
        for j in range(len(key)):
            if k<len(pt):
                matrix[i].append(pt[k])
            else:
                matrix[i].append('')
            k+=1


    ct = []
    for i in range(len(order)):
        col_ix = order.index(i)
        for row_ix in range(rows):
            ct.append(matrix[row_ix][col_ix])

    ct=''.join(ct)
    print("Encrypted text is " + ct)
    return ct

encrypt(matrix , key , order)
