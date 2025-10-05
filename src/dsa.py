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
