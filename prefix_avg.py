# given a sequence S of n numbers, compute a sequence A, where A[j] is the average of elements S[0],...,S[j] for j = 0,1,...n-1

def prefix_avg(S):
    n = len(S)
    A = [0]*n
    pref_sum = 0
    for i in range(len(S)):
        pref_sum+=S[i]
        A[i] = pref_sum/(i+1)
    return A

# the time complexity for this implementation is O(n):
    # the assignment statements on lines 4-6 are O(1), and the statements in the loop body are visited n times thus requiring O(n) time
    # the return statement uses O(1) time
    # thus by Big-oh standard, we describe the worst case run time using the largest term wich is O(n)

def to_int_list(s):
    for i, c in enumerate(s):
        s[i] = int(c)
    return s


def main():
    sequence_s = input('Enter sequence of numbers: ')
    sequence_s = sequence_s.split(',')
    sequence_s = to_int_list(sequence_s)
    p_avg = prefix_avg(sequence_s)
    print(p_avg)

if __name__ == '__main__':
    main()