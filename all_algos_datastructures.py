def insertion_sort_inc(unsorted_list):
    for i in range(1,len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j > -1 and unsorted_list[j] > key:
            unsorted_list[j+1] = unsorted_list[j]
            j = j-1
        unsorted_list[j+1] = key
        print("Cur List: ", unsorted_list)
    print("Sorted List: ", unsorted_list)

def insertion_sort_dec(unsorted):
    for i in range(1, len(unsorted), 1):
        cur = unsorted[i]
        j = i - 1
        while j > -1 and unsorted[j] < cur:
            unsorted[j+1] = unsorted[j]
            j-=1
        unsorted[j+1] = cur
        print("Cur List: ", unsorted)
    print("Sorted List: ", unsorted)

def sum_nbit_binary(bin_intA, bin_intB):
    bin_sum = [0]*(len(bin_intA)+1)
    carry = 0
    for i in range(len(bin_intA)-1, -1,-1):
        sum_digit = (carry + bin_intA[i] + bin_intB[i]) % 2
        carry = 1 if (carry + bin_intA[i] + bin_intB[i]) / 2 >= 1 else 0
        print("A: ", bin_intA[i], "B: ", bin_intB[i], "CARRY: ", carry, "SUM: ", sum_digit)
        bin_sum[i+1] = sum_digit
    bin_sum[0]+=carry
    print("binary digit sum: ", bin_sum)


def cast_to_int_list(str_list):
    temp = str_list
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    return temp


def main():
    algo_name = input("Enter algorithm to run: ")
    

    if algo_name == "insertion_sort_inc" :
        algo_input = input("Enter input for algorithm: ")
        algo_input = algo_input.split(",")

        insertion_sort_inc(algo_input)
    if algo_name == "insertion_sort_dec" :
        algo_input = input("Enter input for algorithm: ")
        algo_input = algo_input.split(",")

        insertion_sort_dec(algo_input)
    if algo_name == "sum_nbit_binary" :
        bin_num1 = input("Enter binary digit 1: ")
        bin_num2 = input("Enter binary digit 2: ")

        bin_num1 = cast_to_int_list(bin_num1.split(","))
        bin_num2 = cast_to_int_list(bin_num2.split(","))

        sum_nbit_binary(bin_num1, bin_num2)


if __name__ == "__main__":
    main()