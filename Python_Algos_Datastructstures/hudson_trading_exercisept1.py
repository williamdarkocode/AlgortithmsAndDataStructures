# plaid code signal

"""
You have been tasked with finishing this implementation of TextEditor. The TextEditor should be able to print a string based on the input passed. The various operations of the TextEditor are listed below.

Tips

Implement each operation one at a time and refactor your code as you go.
Ignore the first array element ("0", "1", "2", etc) at first. It will be used in step 5, but is passed in to all test cases for consistency.
Get as many test cases passing as you can in the 1hr time limit!
There is no penalty for running your code. Run the tests early and often!
Your final score will be the maximum of your submitted scores, so submit early and often, don't wait until the last minute! If the clock runs out and you have not submitted yet, your score will be 0, even if you have partially passing tests.
INSERT should append text:

input = [
    ["0", "INSERT", "a"],
    ["1", "INSERT", "b"],
    ["2", "INSERT", "c"]
]

// returns: "abc"
DELETE should remove the last character:

input = [
    ["0", "INSERT", "abc"],
    ["1", "DELETE"]
]

// returns: "ab"
and

input = [
    ["0", "INSERT", "abc"],
    ["1", "DELETE"],
    ["2", "DELETE"]
]

// returns: "a"
DELETE should do nothing when there are no characters to delete:

input = [
    ["0", "INSERT", "a"],
    ["1", "DELETE"],
    ["2", "DELETE"]
]

// returns: ""
UNDO should undo the previous INSERT or DELETE operation:

input = [
    ["0", "INSERT", "Hello"],
    ["1", "INSERT", " World"],
    ["2", "INSERT", "!"],
    ["3", "UNDO"],
    ["4", "UNDO"]
]

// returns: "Hello"
and should do nothing when there are more UNDOs than other input:

input = [
    ["0", "INSERT", "Hello"],
    ["1", "UNDO"],
    ["2", "UNDO"]
]

// returns: ""
REDO should redo the previous UNDO operation:

input = [
    ["0", "INSERT", "Hello"],
    ["1", "INSERT", " World"],
    ["2", "UNDO"],
    ["3", "REDO"]
]

// returns: "Hello World"
and should do nothing when there are more REDOs than UNDOs:

input = [
    ["0", "INSERT", "Hello"],
    ["1", "UNDO"],
    ["2", "REDO"],
    ["3", "REDO"]
]

// returns: "Hello"
and should only work immediately after an UNDO or REDO operation:

input = [
    ["0", "INSERT", "Hello"],
    ["1", "UNDO"],
    ["2", "INSERT", " World"],
    ["3", "REDO"]
]

// returns: " World"
input should be applied in chronological order according to the UNIX timestamp given.

input = [
    ["1548185072722", "INSERT", "ola"],
    ["1548185072721", "INSERT", "H"]
]

// returns: "Hola"
SELECT should perform the operation following it on the range from start to end. Start is inclusive and end is exclusive (equivalently, you can think of start and end as the index of a cursor rather than the index of a character). If the selection is greater than length of text, select up to the end. If a SELECT follows another SELECT, the most recent should be used. If the start of the SELECT is outside the range of the text, it should be ignored. The different uses of SELECT are further described below.
SELECT and DELETE should remove the selected characters:

input = [
    ["1548185072721", "INSERT", "Hello"],
    ["1548185072722", "SELECT", "1", "3"],
    ["1548185072723", "DELETE"],
]

// returns: "Hlo"
SELECT and INSERT should replace the selected characters with the inserted characters:

input = [
    ["1548185072721", "INSERT", "Hello"],
    ["1548185072722", "SELECT", "1", "5"],
    ["1548185072723", "INSERT", "ola"],
]

// returns: "Hola"
SELECT and BOLD should insert * characters before the first selected character and after the last selected character:

input = [
    ["1548185072721", "INSERT", "Hello"],
    ["1548185072722", "SELECT", "1", "3"],
    ["1548185072723", "BOLD"],
]

// returns: "H*el*lo"
Example

For input = [["0", "INSERT", "a"], ["1", "INSERT", "b"], ["2", "INSERT", "c"]], the output should be
solution(input) = "abc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string input

An array of operations need to be applied to the text editor. It is guaranteed that each operation is one of the one described in the description, all operation parameters are given in correct format, and that the text editor will never be in an incorrect state that is not described in the description.

[output] string

The final text in the text editor after applying all operations.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name


"""






# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_gcd(smallest, largest):
    if smallest == 0:
        return largest
    return find_gcd(largest % smallest, smallest)


def solution(X, Y):
    freqs = {}
    for i in range(len(X)):
        num = X[i]
        denom = Y[i]
        gcd = find_gcd(min(num, denom), max(num, denom))

        num//=gcd
        denom//=gcd
        frac = f'{num}/{denom}'

        if frac not in freqs:
            freqs[frac] = 0
        freqs[frac]+=1
        
    return max(freqs.values())






'''
amazon OA
'''

def find_max_profit(profits, k):
    N = len(profits)
    win_i = -N
    win_j = win_i+k

    all_sums = []
    max_sum = float('-inf')

    for i in range(len(profits)):
        if win_j >=0 and win_i < 0:
            all_sums.append(sum(profits[win_i:]+profits[:win_j]))
        else: 
            all_sums.append(sum(profits[win_i: win_j]))
            win_i+=1
            win_j+=1
    
    for i in range(len(all_sums)//2):
        l, r = all_sums[i], all_sums[i+k+1]
        max_sum = max(max_sum, l+r)
    
    return max_sum




def convert_from_booky(str_ver):
    lst = str_ver.split('\n')
    e_list = []
    for l in range(1, len(lst),1):
        e_list.append(l.split(' '))
    
    return e_list


def count_neighbours(source, graph, visited):
    if source in visited:
        return 0
    visited.add(source)
    return len(graph[source])



def degree_array(edgelist:list):
    graph = {}
    for edge in edgelist:
        p,k = edge
        if p not in graph:
            graph[p] = []
        if k not in graph:
            graph[k] = []
        graph[p].append(k)
        graph[k].append(p)

    degrees = [0]*len(graph)
    visited = set()

    for i, node in enumerate(graph.keys()):
        degrees[i] = count_neighbours(node, graph, visited)

    return degrees










def main():
   return








if __name__ == '__main__':
    main()



"""
[
  [x o x o o]
  [o x o x o]
  [x x x x x]
]

[
  [x x x x x]
  [x x o x x]
  [x o o o x]
  [x o o x x]
  [x o x x x]
]



const explore_dfs = (pos, grid, visited, changes) => {
  let pos_id = `${pos[0]},${pos[1]}`;
  
}

const visit_cells = (grid) => {
  visited = new Set()
  changes = new Set()
  for(let i = 0; i < grid.length; i++) {
    for(let j = 0; j < grid[0].length; j++) {
      explore_dfs([i,j], grid, visited, changes)
    }
  }
  
  // make changes to grid
  
  
const solution = (grid) => {
  ROWS = grid.length
  COLS = grid[0].length
  const dfs = (r, c) => {
    if(r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 'O'){
    	return
    }
    grid[r][c] = 'T'
    dfs(r+1)[c]
    dfs[r][c+1]
    dfs[r-1][c]
    dfs[r][c-1]
  }
  
  for(let i = 0; i < ROWS; i++){
    for(let j = 0; j < COLS; j++){
    	if(grid[i][j] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1])){
        dfs(i, j) // should change each bordered O -> T
      }
    }
  }
  
  for(let i = 0; i < ROWS; i++) {
    for(let j = 0; j < COLS; j++){
    	if(grid[i][j] == 'O'){
        grid[i][j] == 'X'
      }
    }
  }
  
  for(let i = 0; i < ROWS; i++) {
    for(let j = 0; j < COLS; j++){
    	if(grid[i][j] == 'T'){
        grid[i][j] == 'O'
      }
    }
  }

  return grid
}
  
  
  
  
}


"""


"""
const fbd = (prices) => {
  let min_val = Number.MAX_SAFE_INTEGER;
  let max_profit = 0;
  
  for(let i = 0; i < prices.length; i++){
    if(prices[i] < min_val){
      min_val = prices[i]
    } else if(prices[i] - min_val > max_profit){
      max_profit = prices[i] - min_val
    }
  }
  // [2, 5, 1, 200, 6, 91, 100]
  
  return max_profit
  
}

"""