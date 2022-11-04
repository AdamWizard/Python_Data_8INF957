import FiboModule as fibo
from AddingModule import *

def main():
    n = int(input("How far in the fibonacci suite should we go?"))
    print("\nHere is the array containing the fibonacci suite up to the ", n ,"th term :")

    print(fibo.fiboArray(n))

    print("\nand here is the ", n ,"th term :")
    print(fibo.fibo(n))

    print("\nHere is the ", n+1 ,"th term :")
    print(add(fibo.fibo(n),fibo.fibo(n+1)))

    print("\nHere is the ", n ,"th term minus 1:")
    print(substract(fibo.fibo(n),1))
    # errors would occur when using add and substract if we just imported addingModule
    # because we would have to write AddingModule.add() and AddingModule.substract()
    # importing modules rather than their contents can be useful if they contain functions or classes with the same names


main()