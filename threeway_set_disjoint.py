# given 3 sequences of numbers, A, B, C, determine if their intersection is empty. Namely, there does not exist an element x such that
# x is in A, B, and C
# Assume no individual sequence contains duplicates

import numpy as np

def return_smallest_to_largest(A,B,C):
    list_of_lists = [A,B,C]
    len_list = [len(A), len(B), len(C)]
    fin_list = [0]*3
    for i in range(len(len_list)):
        idx = np.argmin(len_list)
        fin_list[i] = list_of_lists[idx]
        len_list = len_list[0:idx] + len_list[idx+1:]
        list_of_lists = list_of_lists[0:idx] + list_of_lists[idx+1:]
    return fin_list

def set_disjoint1(A,B,C):
    smtlrg = return_smallest_to_largest(A,B,C)
    for a in smtlrg[0]:
        for b in smtlrg[1]:
            if a == b:
                # we only check an intersection with c if a, and b intersect
                for c in smtlrg[2]:
                    if a == c:
                        return [False, a]
    return [True, '']


def main():
    A = input('Enter sequence A: ')
    B = input('Enter sequence B: ')
    C = input('Enter sequence C: ')
    A = A.split(',')
    B = B.split(',')
    C = C.split(',')
    resp = set_disjoint1(A, B, C)
    print(resp)


if __name__ == '__main__':
    main()
