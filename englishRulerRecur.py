def line(len, label):
    line = "-"*len 
    if(label):
        line = line + " " + label
    print(line)


def interval(centreLen):
    if(centreLen > 0):
        interval(centreLen-1)
        line(centreLen,"")
        interval(centreLen-1)


def ruler(inches, totalLen):
    line(inches,"0")
    for i in range(1,1+inches):
        interval(totalLen-1)
        line(totalLen-1, str(i))




def main():
    ruler(7, 4)


if __name__ == "__main__":
    main()