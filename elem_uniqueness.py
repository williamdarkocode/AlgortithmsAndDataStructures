def unique(S):
    S = sorted(S)
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            return [False, 'duplicate: '+S[i]]
    return [False, 'no duplicates']

def main():
    lst = input('Enter list: ')
    lst = lst.split(',')
    is_unique = unique(lst)
    print(is_unique)


if __name__ == '__main__':
    main()