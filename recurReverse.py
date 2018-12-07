def reverse(sequence, start, stop):
    if(stop <= start):
        return sequence
    else:
        temp = sequence[start]
        sequence[start] = sequence[stop]
        sequence[stop] = temp
        return reverse(sequence, start+1, stop-1)


def main():
    arr = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78,82,86,90,94,98,102,106,110,114,118,122,126,130,134,138,142,146,150,154,158,162,166,170,174,178,182,186,190,194,198]
    print("Length of array: " + str(len(arr)))
    print("Element at index mid: " + str(arr[25]))
    reversedArr = reverse(arr,0,len(arr)-1)
    print(reversedArr)


if __name__ == "__main__":
    main()

