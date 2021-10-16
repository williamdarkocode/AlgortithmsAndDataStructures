def bin_search_recur(left, right, lst, target):
    mid = (left+right)//2
    if lst[mid] == target:
        return "Found: {}, at index: {}".format(True, mid)
    elif left>right:
        return "Found: {}".format(False)
    else:
        if lst[mid] > target:
            return bin_search_recur(left, mid-1, lst, target)
        if lst[mid] < target:
            return bin_search_recur(mid+1, right, lst, target)


def main():
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    found = bin_search_recur(0, len(arr)-1, arr, 157)
    print(found)


if __name__ == '__main__':
    main()