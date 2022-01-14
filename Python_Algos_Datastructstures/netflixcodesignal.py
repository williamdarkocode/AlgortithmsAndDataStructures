def display_grid(grid):
    s = "".join(f'{x}\n' for x in grid)
    print(s)

def display_grid_res(grid):
    s = "".join(f'{x}\n' for x in grid)
    return s

def simple_test(observed, expected):
    obs = display_grid_res(observed)
    exp = display_grid_res(expected)
    if observed == expected:
        print(f"Test passed! \n Observed:\n{obs}, Expected:\n{exp}")
    else:
        print(f"Test failed! \n Observed:\n{obs}, Expected:\n{exp}")
    return

def bubblesSolution(bubbles:list):
    coords = set()
    for i in range(len(bubbles)):
        for j in range(len(bubbles[0])):
            cur = bubbles[i][j]
            neighbours = []
            if i+1 < len(bubbles) and bubbles[i+1][j] == cur:
                neighbours.append((i+1,j))
            if i-1 >= 0 and bubbles[i-1][j] == cur:
                neighbours.append((i-1,j))
            if j+1 < len(bubbles[0]) and bubbles[i][j+1] == cur:
                neighbours.append((i,j+1))
            if j-1 >= 0 and bubbles[i][j-1] == cur:
                neighbours.append((i,j-1))

            if len(neighbours) >=2:
                neighbours.append((i,j))
                coords.update(neighbours)
    
    for pair in coords:
        bubbles[pair[0]][pair[1]] = 0


    for col in range(len(bubbles[0])):
        for row in range(len(bubbles)-1,-1,-1):
            if bubbles[row][col] == 0:
                i = row
                while i > 0 and bubbles[i][col] == 0:
                    i-=1

                bubbles[row][col] = bubbles[i][col]
                bubbles[i][col] = 0
            
    return bubbles

def ahandle(a:list,q:list):
    a[q[1]]+=q[2]
    return

def bhandle(a:list,b:list,qx:list):
    aset = {}
    for n in a:
        if n not in aset:
            aset[n] = 0
        aset[n]+=1
    
    bset = {}
    for n in b:
        if n not in bset:
            bset[n] = 0
        bset[n]+=1

    
    pairs = set()
    count = 0

    if len(b) > len(a):
        for i, n in enumerate(b):
            if (qx-n) in aset:
                count+=aset[(qx-n)]
        return count
    else:
        for i, n in enumerate(a):
            if (qx-n) in bset:
                count+=bset[(qx-n)]
        return count

def queriesSolution(a:list, b:list, queries:list):
    bres = []
    for q in queries:
        if q[0] == 0:
            ahandle(a, q)
        else:
            bres.append(bhandle(a, b, q[1]))
    return bres


def main():
    tdarr = [[3, 1, 2, 1],
             [1, 1, 1, 4],
             [3, 1, 2, 2],
             [3, 3, 3, 4]]

    exp = [[0, 0, 0, 1], [0, 0, 0, 4], [0, 0, 2, 2], [3, 0, 2, 4]]

    a = [2, 3]
    b = [1, 2, 2]
    queries = [[1, 4], [0, 0, 1], [1, 5]]

    res = queriesSolution(a,b,queries)

    simple_test(res, [3, 4])
    return

if __name__ == "__main__":
    main()