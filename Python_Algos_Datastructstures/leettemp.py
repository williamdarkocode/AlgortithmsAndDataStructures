import collections


from collections import deque

def explore_subpaths(source, parent_path, all_paths:set, sub_paths:dict, end_node):
    if source == end_node:
        final_path = f'{parent_path}-{source}'
        all_paths.add(final_path)
        return [source]
    
    if source in sub_paths:
        return sub_paths[source]
    
    i,j = int(source.split(',')[0]),int(source.split(',')[1])
    ei,ej = int(end_node.split(',')[0]),int(end_node.split(',')[1])
    
    out_bounds = (i > ei or j > ej)
    
    if out_bounds:
        return [None]
    
    sub_paths[source] = []
    
    neighbours = [f'{i},{j+1}', f'{i+1},{j}']
    
    for n in neighbours:
        res = explore_subpaths(n, f'{parent_path}-{source}', all_paths, sub_paths, end_node)
        for r in res:
            if r is not None:
                sub_paths[source].append(f'{source}-{r}')
                rspl = r.split('-')
                if rspl[-1] == end_node:
                    all_paths.add(f'{parent_path}-{source}-{r}')
                for i in range(1, len(rspl), 1):
                    sub_paths.pop(rspl[i], None)
    
    return sub_paths[source]
    
        

def uniquePaths(m: int, n: int) -> int:
    sub_paths = {}
    all_paths = set()
    
    ei = m-1
    ej = n-1
    end = f'{ei},{ej}'
    
    si,sj = 0,0
    start = f'{si},{sj}'
    
    neighbours = [f'{si},{sj+1}', f'{si+1},{sj}']
    
    sub_paths[start] = []
    
    for n in neighbours:
        res = explore_subpaths(n, ""+start, all_paths, sub_paths, end)
        for r in res:
            if r is not None:
                sub_paths[start].append(f'{start}-{r}')
                rspl = r.split('-')
                if rspl[-1] == end:
                    all_paths.add(f'{start}-{r}')
                for i in range(1, len(rspl), 1):
                    sub_paths.pop(rspl[i], None)
            
    # print(sub_paths.keys())
    # print(all_paths)
    
    return len(all_paths)



def exist(board, word: str):
    visited = set()
    used = set()
    found = ""
    cur_idx = 0
    
    queue = deque()
    queue.append([0,0])
    
    for r in board:
        print(r)
    
    while queue:
        i,j = queue.popleft()
        pos = f'{i},{j}'
        used_id = f'{i},{j}'

        
        if found == word:
            print(i,j, found, visited, used)
            return True
        if cur_idx >= len(word):
            return False
        
        out_bounds = (i >= len(board)) or (i < 0) or (j >= len(board[0])) or (j < 0)
        
        if (not out_bounds) and (pos not in visited):
            print(i,j, found)
            
            visited.add(pos)
            
            if (word[cur_idx] == board[i][j]) and (used_id not in used):
                used.add(used_id)
                found+=board[i][j]
                cur_idx+=1
                
        
            adjacents = [[i-1,j], [i+1,j], [i,j+1], [i,j-1]]
            for n in adjacents:
                n_pos = f'{n[0]},{n[1]}'
                if n_pos not in visited:
                    queue.append(n)
        
        else:
            if not out_bounds and pos in visited and pos not in used:
                adjacents = [[i-1,j], [i+1,j], [i,j+1], [i,j-1]]
                for n in adjacents:
                    n_pos = f'{n[0]},{n[1]}'
                    if n_pos not in used:
                        queue.append(n)
                
    
    print(found, cur_idx, used, visited)
    if found == word:
        return True
    
    return False
        
def main():
    inp = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    exist(inp, word)

    return

if __name__ == "__main__":
    main()