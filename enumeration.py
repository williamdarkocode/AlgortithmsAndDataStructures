def puzzle(k, sequence, tempset, solution):
    for elem in tempset:
        newStr = sequence + str(elem)
        sequence = newStr
        tempset[0] = []
        if(k == 1):
            if(sequence == solution):
                return "Solution found: " + sequence
        else:
            puzzle(k-1, sequence,tempset,solution)
            e = sequence[len(sequence)-1]
            sequence = sequence[:len(sequence)-1]
            # tempset[len(tempset)] = e
            tempset+=[e]



def main():
    solution = input("Enter a solution to find: ")
    k = len(solution)
    sequence = ""
    tempset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = puzzle(k, sequence, tempset, solution)
    print(answer)


if __name__ == "__main__":
    main()





        