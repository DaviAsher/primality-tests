n = int(input('input a positive integer number to find all primes up to it: '))
maximo = n
nao_primo = [0] * maximo
primos = []
def sieve():
    for x in range(2,maximo):
        if(nao_primo[x]==1):
            continue
        b = x*2
        primos.append(x)
        while(b<maximo):
            nao_primo[b]=1
            b+=x
sieve()

print(primos)
