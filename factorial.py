def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)



def main():
    num = input("Enter number to comupte factorial of:  ")
    numSorts = factorial(int(num))
    print(num+"! is: ", numSorts)


if(__name__ == "__main__"):
    main()

# factorial(n) has a total of n+1 activations
    # eg: factorial(5)
        # 