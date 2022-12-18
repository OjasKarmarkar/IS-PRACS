def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    # add the key to the matrix
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    #Add the rest of the alphabet to the matrix
    # A=65 ... Z=90
    for letter in range(65,91):
        if letter==74: # I/J are in the same position
                continue
        if chr(letter) not in letters_added: # Do not add repeated letters
            letters_added.append(chr(letter))

    #print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index+=1
    return matrix

def indexOf(letter,matrix):
    if ord(letter)==74:
        letter = 'I'
    for row in range (5):
        try:
            col = matrix[row].index(letter)
            return (row,col)
        except:
            continue

def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            if len(message)%2!=0:
                message = message + 'X'
                index += 2
            else:
                index+=1
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=1
    return message

def encryptDecrypt(pt,matrix , isDecrypt):
    inc=1
    if isDecrypt:
        inc=-1
    ct = ''
    for  (i,j) in zip(pt[0::2], pt[1::2]):
        r1,c1 = indexOf(i,matrix)
        r2,c2 = indexOf(j , matrix)

        if c1==c2:
            ct+= matrix[(r1+inc) % 5][c1] + matrix[(r2+inc)% 5][c2]
        elif r1==r2:
            ct+= matrix[r1][(c1+inc) % 5] + matrix[r2][(c2 + inc)  % 5]
        else:
            ct+= matrix[r1][c2] + matrix[r2][c1]
    return ct

pt = input("Enter PlainText : ").upper().replace(" " , "")
key = input("Enter Key (Length 5 without I/J) : ").upper()
pt = separate_same_letters(pt)
matrix = create_matrix(key=key)

ct = encryptDecrypt(pt,matrix , isDecrypt=False)
print(ct)
pt = encryptDecrypt(ct , matrix , isDecrypt=True)
print(pt)