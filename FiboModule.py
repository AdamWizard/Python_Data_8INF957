def fibo(n): # gives the nth term of the fibonacci suite    
    a,b = 0,1
    step = 0
    while (step<n):
        a,b = b,a+b
        step+=1
    
    return a

def fiboArray(n): # gives fibonacci suite up to the nth term
    a,b = 0,1
    step = 0
    fiboArray = []
    while (step<n):
        fiboArray.append(a)
        a,b = b,a+b
        step+=1
    
    return fiboArray

def main():
    n = 0
    for n in range(0,10):
        print(fibo(n), end=", ")
    print("\n",fiboArray(10))


