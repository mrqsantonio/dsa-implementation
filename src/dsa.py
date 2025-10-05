from utils.dsa_utils.py import get_prime_dividers


def get_DSAparameters(n): 
    if(n <3): 
        raise Exception("get_DSAparameters only work with numbers above 2")
    p = randprime(pow(2,n-1), pow(2,n))
    listOfPossibleQs = get_prime_dividers(p-1)
    qIdx = random.randint(0,len(listOfPossibleQs)-1)
    q = listOfPossibleQs[qIdx]
    h = random.randint(1,p-1)
    g = pow(h,(p-1)/q) % p
    while(g ==1):
        h = random.randint(1,p-1)
        g = pow(h,(p-1)/q) % p
    return p,q,g

def  get_skeys(p, q, g):
    x = random.randint(1,q-1)
    y = pow(g,x)%p
    return x,y

def dsa_sign(message, p, q, g, x):
    k = random.randint(1,q-1)
    subR = pow(g,k)%p
    r = subR %q
    while(r==0):
        k = random.randint(1,q-1)
        subR = pow(g,k)%p
        r = subR %q
    inverseOfK = inverseOfNModP(k,q)
    xr = r*x
    s = (inverseOfK*(message+xr)) % q
    return r,s

def inverseOfNModP(n,p):
    phiOfN = p-1
    return pow(n,phiOfN-1)%p

def dsa_verify(message,signature,p,q,g,y):
    if(signature[0] > 0 and signature[0] < q and 
       signature[1] > 0 and signature[1] < q):
        print("r e s are OK")
    else:
        return False
    w = inverseOfNModP(signature[1]) % Q
    u1 = (message * w) % q
    u2 = (signature[0]*w)%q
    v= ((pow(g,u1)*pow(y,u2))%p)%q
    return v ==signature[0]

def get_private_key(y,g,p):
    x = 2 # começa com 1 porque x está entre 1 e q-1
    while(y != (pow(g,x)%p)):
        x+=1
    return x

