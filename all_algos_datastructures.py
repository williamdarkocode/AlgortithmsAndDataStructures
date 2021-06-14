def insertion_sort(unsorted_list):
    for i in range(1,len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j > -1 and unsorted_list[j] > key:
            unsorted_list[j+1] = unsorted_list[j]
            j = j-1
        unsorted_list[j+1] = key
        print("Cur List: ", unsorted_list)
    print("Sorted List: ", unsorted_list)


def main():
    algo_name = input("Enter algorithm to run: ")
    algo_input = input("Enter input for algorithm: ")

    algo_input = algo_input.split(",")

    if algo_name == "insertion_sort" :
        insertion_sort(algo_input)


if __name__ == "__main__":
    main()