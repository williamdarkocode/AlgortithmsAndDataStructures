def log(base,power):
    if(power == 1):
        return 0
    else:
        return (base/base) + log(base, power/base)



def main():
    b = int(input("Enter a posititve base for logarithm:  "))
    n = int(input("Enter a positive the power:  "))
    exponent = log(b,n)
    print(str(b) + " ^ " + str(exponent) + " = " + str(n))
    

if __name__ == "__main__":
    main()
        