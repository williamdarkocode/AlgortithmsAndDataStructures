def summation(n,k):
    l = k-n
    if(l < 0):
        return 0
    else:
        return k + summation(n,k-1)



def main():
    n = int(input("Enter a starting integer: "))
    k = int(input("Enter the last interger (must be less than first):  "))
    s = summation(n,k)
    print("The sum of integers between " + str(n) + " and " + str(k) + " is:  " + str(s))



if  __name__ == "__main__":
    main()