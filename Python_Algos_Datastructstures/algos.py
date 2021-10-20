import random

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


def guessing_game():
    def guess(l, h, num_guesses):
        if(l > h):
            print("Sorry, I couldn't guess your number. I'll try better next time :(")
            return

        mid = (l+h)//2 if num_guesses > 0 else random.randint(l,h)
        num_guesses+=1
        query = input("is {} the number you guessed? Type (y/n): ".format(mid))

        while query.strip().lower() != "y" and query.strip().lower() != "n":
            print('wrong input')
            query = input("is {} the number you guessed? Type (y/n): ".format(mid))

        if query.strip().lower() == 'y':
            print('Get in!!!! 1-0 to me. Machines are always better bruv... It only took {} {} lol.'.format(num_guesses, 'guess' if num_guesses == 1 else 'guesses'))
            return
        else:
            query2 = input('Was my guess higher (h) or lower (l) than your number? Type (h/l): ')
            while query2 != 'h' and query2 != 'l':
                query2 = input('Was my guess higher (h) or lower (l) than your number? Type (h/l): ')
            if query2 == 'h':
                guess(l,mid-1,num_guesses)
            else:
                guess(mid+1,h,num_guesses)
            
        return
    print("Pick a number from 0 to 100. I'm going to try and guess it!")
    guess(0,100, 0)



# selection sort is O(n^2) time complexit because for each iteration 0-n we must find what the smallest element is in the array
def selection_sort(unsorted_list:list):
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest = min(unsorted_list)
        sorted_list.append(smallest)
        unsorted_list.pop(unsorted_list.index(smallest))
    print(sorted_list)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = [arr[random.randint(0, len(arr)-1)]]
    left = [x for x in arr if x < pivot[0]]
    right = [y for y in arr if y > pivot[0]]
    return quick_sort(left) + pivot + quick_sort(right)



def main():
    # arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    # found = bin_search_recur(0, len(arr)-1, arr, 157)
    # print(found)
    # guessing_game()
    arr = [5,6,3,3,3,4,98,22,1,2,89,54,13,24,35,47,999,40000]
    out = quick_sort(arr)
    print(out)
    return


if __name__ == '__main__':
    main()