def sort():
    names = ["carol", "matt", "ilana", "parakam", "ferdi"]
    num = len(names)
    print("START:  ",names)
    for i in range(num-1):
        print("")
        print("i: ",i)
        for j in range(num-1):
            print("    j: ", j)
            if (names[j] > names[j+1]):
                temp = names[j]
                names[j] = names[j+1]
                names[j+1] = temp
                print("     ", names)


def main():
    sort()



if (__name__ == "__main__"):
    main()
