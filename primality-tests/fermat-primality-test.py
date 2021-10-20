#Program to check if a number is prime or not, with the Fermat primality test

n = int(input("Input a number to check if it's a prime number "))

if n==1 or n==0:
  print(n, 'is not a prime number')
  exit()

if n<0:
  n=-n

maximo = 9999
if(n<=maximo):
  maximo=n
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

primo = 1

for a in primos :  

    if a != pow(a,n,n) :
        primo = 0
        print([a,pow(a,n,n)])  
        print(n, 'is not a prime number')
        break
    
if primo==1:
    print(n,'is a prime number')


#pow(a,n,n)= a^n (mod n), if n prime, a^n ≡ a (mod n) 
  
