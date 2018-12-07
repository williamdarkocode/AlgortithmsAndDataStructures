def raiseToPower(num, exponent):
    if(exponent == 0):
        return 1
    else:
        return num * raiseToPower(num, exponent-1)


def main():
    num = int(input("Enter an integer for the base:  "))
    exp = int(input("Enter a non-negative integer for the exponent:  "))
    answer = raiseToPower(num, exp)
    print(str(num) + "^" + str(exp) + " = " + str(answer))



if __name__ == "__main__":
    main()