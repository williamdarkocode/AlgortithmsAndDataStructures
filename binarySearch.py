arr = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78,82,86,90,94,98,102,106,110,114,118,122,126,130,134,138,142,146,150,154,158,162,166,170,174,178,182,186,190,194,198,200]



def binSearch(array, target, low, high):
    if(low > high):
        print("NOT FOUND!")
    else:
        mid = (low+high)//2
        if(array[mid] == target):
            print(str(mid))
        elif(array[mid] > target):
            return binSearch(array, target, low, mid-1)
        else:
            return binSearch(array, target, mid+1, high)






# makeList(2,200,4)


def main():
    count = 0
    for elem in arr:
        count+=1
    print("0th element: " + str(arr[0]))
    print("length-1 element: " + str(arr[len(arr)-1]))
    target = input("Enter an multiple of 2 to search:  ")
    binSearch(arr, int(target), 0, 50)


if __name__ == "__main__":
    main()