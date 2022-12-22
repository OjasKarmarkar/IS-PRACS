from math import gcd,sqrt

def nearestPrime(n,x):

    diff = float('inf')
    new_val = n

    def isPrime(n):
        if (n <= 1):
            return False

        # Check from 2 to sqrt(n)
        for i in range(2, int(sqrt(n))+1):
            if (n % i == 0):
                return False

        return True

    for i in range(n-1,9999):
         if isPrime(i) and i!=x:
            new_val = i
            diff = i-n
            break

    for i in range(2,n):
        if isPrime(i) and n-i < diff and i!=x:
            new_val = n-i
            break

    return new_val




def rsa(pt):
    print("Value of p is : " + str(p))
    print("Value of q is : " + str(q))
    n = p*q
    phi = (p-1)*(q-1)
    e = 0

    if pt>phi:
        pt = pt % phi

    print("final pt after mod : " + str(pt))

    for i in range(2,phi):
        if (gcd(i,phi)==1 and i!=q and i!=p):
            e = i
            break

    print("Value of e is : " + str(e))
    i=1
    while True:
        if (i*e)%phi==1 and i!=e:
            d=i
            break
        i+=1

    print("Value of d is : " + str(d))

    ct = pow(pt,e,n)
    print("Encrypted text is : " + str(ct))
    pt = pow(ct,d,n)
    print("Decrypted text is : " + str(pt))
    return ct


p = input("Enter passphrase p : ")
q = input("Enter passphrase q : ")
p = nearestPrime(len(p),0)
q = nearestPrime(len(q),p)

pt = int(input("Enter numerical input : "))
rsa(pt)