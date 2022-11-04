import FiboModule as fibo

def main():
    n = int(input("How far in the fibonacci suite should we go?"))
    print("\nHere is the array containing the fibonacci suite up to the ", n ,"th term :")

    print(fibo.fiboArray(n))

    print("\nand here is the ", n ,"th term :")
    print(fibo.fibo(n))


main()