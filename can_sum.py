def can_sum_nums(target, arr):
    d = {}
    for x in arr:
        d[x] = [target-x, target % x]
    for x in d.keys():
        val = d[x][0]
        divis = d[x][1]
        if val in d or (divis == 0 and target != 0):
            print(x, d[x])
            return True
    print('False')
    return False

def main():
    test_target = 300
    arr = [7, 14]
    can_sum_nums(test_target, arr)

if __name__ == '__main__':
    main()