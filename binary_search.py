import math
def srch(seq, target, low, high):
    mid = math.floor((low + high)/2)
    if low > high:
        return [-1, 'target not found']
    else:
        if seq[mid] == target:
            return [mid, 'target found at index: {}'.format(mid)]
        elif target > seq[mid]:
            return srch(seq, target, mid+1, high)
        else:
            return srch(seq, target, low, mid-1)

def to_int_list(s):
    for i, c in enumerate(s):
        s[i] = int(c)
    return s

def main():
    l = input("Enter list: ")
    t = input("Enter target: ")
    t = int(t)
    l = l.split(',')
    l = to_int_list(l)
    l = sorted(l)
    
    print("list: ", l)

    lo = 0
    hi = len(l)-1

    fnd =  srch(l, t, lo, hi)
    print(fnd)

if __name__ == '__main__':
    main()