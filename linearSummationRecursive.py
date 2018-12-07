def summation(sequence, n):
    if(n == 0 or len(sequence) == 0):
        return 0
    else:
        return sequence[n-1] + summation(sequence, n-1)
    


def main():
    ls = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        inp = int(input("Enter element at index "+str(i)+":  " ))
        ls[i] = inp

    print(ls)
    numElems = len(ls)
    print("SUM of all elements in list is: " + str(summation(ls, numElems)))



if __name__ == "__main__":
    main()