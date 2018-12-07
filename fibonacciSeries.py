# int fibonacci(int n) {
#     if(n > 1) { 
#         return fibonacci(n-2) + fibonacci(n-1);
#     }
#     else {
#         if(n <= 1) {
#             return 1;
#         }
#     }
# }

def fibonacci(n):
    if(n > 1):
        return fibonacci(n-2)+fibonacci(n-1)
    else:
        return 1
    

def printNext(k):
    print(str(k))
    t = fibonacci(k)
    
    return t


def main():
    start = 0
    while(start < 30):
        l = printNext(start)
        if(start == 1 and l == 1):
            start = 2
        else:
            start = l


if __name__ == "__main__":
    main()
        