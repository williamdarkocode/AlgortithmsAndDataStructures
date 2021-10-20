import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# ap.add_argument("-d", "--dest", required=True, help="Destination of the final image; provide relative path.")

# args = vars(ap.parse_args())

class Team:
    def __init__(self, manager, players):
        self._manager = manager
        self._players = players

    def get_manager(self):
        return self._manager
    def get_squad(self):
        return self._players
    def sack_manager(self):
        self._manager = None
    def replace_manager(self, new_gaffer):
        self._manager = new_gaffer
        

class AcademySquad(Team):
    def __init__(self, manager, players, loanees):
        super().__init__(manager, players)
        self._loanees = loanees
    def get_loanees(self):
        return self._loanees


def bin_search(target, left, right, lst):
    mid = (left+right)//2 
    if(lst[mid] == target):
        print('found at ', mid)
        return True
    if(left > right):
        print('not found')
        return False
    bin_search(target, mid+1 if target > lst[mid] else left, mid-1 if target < lst[mid] else right, lst)


def lin_recur_sum(arr, n):
    if(n == 0):
        return 0
    return lin_recur_sum(arr, n-1) + arr[n-1]

def reverse_recur(arr, left, right):
    if(left >= right):
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    reverse_recur(arr, left+1, right-1)


def create_all_subsets(k:int,S:list,U:list,fin:list):
    return

def form_all_subsets(S:str, U:list, fin:list):
    if len(U) == 0:
        fin.append(S)
    else:
        for e in U:
            we = U.copy()
            we.pop(U.index(e))
            # fin.append(form_all_subsets(S+e, we, fin))
            form_all_subsets(S+e, we, fin)
    return fin

def main():
    studs = {
        'will': 'darko',
        'sam': 'fawcett',
        'emi': 'mora',
        'lloyd': 'chen',
        'nick': ''
    }

    studs2 = {
        'nick': 'alex',
        'nicko': 'johnson',
        'amir': 'badrudeen',
        'rami': 'baez',
        'lloyd': 'chenn'
    }

    # data = studs.keys()
    # # print(iter(data).__next__())

    # def factors(hi):
    #     for i in range(hi+1):
    #         if i % 5 == 0:
    #             yield i

    # print(list(factors(100)))

    five_aside = Team('william', studs.keys())
    # print(five_aside.get_squad())

    academys = AcademySquad('Sami', studs2.keys(), ['ivan', 'andy f', 'wilson', 'eudy'])
    # print(academys.get_loanees())

    nums = [2,4,6,8,10,12,14,16,20]
    # bin_search(16,0,len(nums)-1,nums)

    # sum_nums_recur = lin_recur_sum(nums, 5)
    # reversed_nums = reverse_recur(nums,0, len(nums)-1)


    subs = form_all_subsets("",['a','b', 'c'],[])
    print(subs)
    return


if __name__ == '__main__':
    main()


#     #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# #
# # Complete the 'groupTransactions' function below.
# #
# # The function is expected to return a STRING_ARRAY.
# # The function accepts STRING_ARRAY transactions as parameter.
# #

# def groupTransactions(transactions):
#     # Write your code here
#     item_map = {}
#     for item in transactions:
#         if item in item_map:
#             item_map[item]+=1
#         else:
#             item_map[item] = 1
    
#     sorted_keys = sorted(item_map.keys(), key = lambda x: x.lower() or item_map[x])
#     # print(sorted_keys)
#     arr = ["{} {}".format(x, item_map[x]) for x in sorted_keys]
    
#     return arr

# if __name__ == '__main__':



# def compute_gas_left(path):
#   gas = 0
#   for i, point in enumerate(path):
#     data = point.split(':')
#     given = int(data[0])
#     taken = int(data[1])
#     if (gas + given) < taken:
#       return -1
#     left = given-taken
#     gas+=left
#   return gas

# def ArrayChallenge(strArr):
#   # code goes here
#   N = int(strArr[0])
#   stations = strArr[1:]
#   possible_starts = []
#   for i, stat in enumerate(stations):
#     path = stations[i:len(stations)]+stations[0:i] if i != 0 else stations[0:len(stations)]
#     # print(path)
#     gas_left = compute_gas_left(path)
#     # print(gas_left)
#     if gas_left >= 0:
#       possible_starts.append(i)
#   return min(possible_starts)+1 if len(possible_starts) > 0 else "impossible"

# # keep this function call here 
# print(ArrayChallenge(input()))


import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

def make_camel(prev, cur):
    if prev is None or len(prev.strip()) == 0:
        return cur.lower()
    elif len(cur.strip()) == 0:
        return " "
    else:
        return cur.capitalize()

words = []
for line in sys.stdin:
    words.append(line.strip())

camel_word = "".join(make_camel(words[i-1] if i-1 >=0 else None, words[i]) for i, w in enumerate(words))
print(camel_word)