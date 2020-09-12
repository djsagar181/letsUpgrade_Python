
# prime number from 1 - 2500 using filter function

def prime(i):
    
    for j in range(2,i):
        
        if i % j == 0:
        
            break
        
    else:
        
        return i

primeNo = filter(prime, range(1, 2500))

print ('\nPrime numbers between 1-2500:\n')

print(list(primeNo))