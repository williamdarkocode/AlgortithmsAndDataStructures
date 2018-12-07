def findMinRecur(curMin, idx, sequence):
    m = curMin
    i = idx
    if(idx > len(sequence)-1):
        return curMin
    else:
        if(sequence[i] < m):
            m = sequence[i]
            i+=1
            return findMinRecur(m,i,sequence)
        else:
            i+=1
            return findMinRecur(m,i,sequence)


def main():
    arr = [2,4,5,6,7,810,-1,5,6,9,0.5,-99.44,77]
    minnette = findMinRecur(arr[0],0,arr)
    print("Minimum in arr: " + str(arr) + " is: " + str(minnette))


if __name__ == "__main__":
    main()