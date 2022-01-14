import random
from collections import deque

def bin_search_recur(left, right, lst, target):
    mid = (left+right)//2
    if lst[mid] == target:
        return "Found: {}, at index: {}".format(True, mid)
    elif left>right:
        return "Found: {}".format(False)
    else:
        if lst[mid] > target:
            return bin_search_recur(left, mid-1, lst, target)
        if lst[mid] < target:
            return bin_search_recur(mid+1, right, lst, target)


def guessing_game():
    def guess(l, h, num_guesses):
        if(l > h):
            print("Sorry, I couldn't guess your number. I'll try better next time :(")
            return

        mid = (l+h)//2 if num_guesses > 0 else random.randint(l,h)
        num_guesses+=1
        query = input("is {} the number you guessed? Type (y/n): ".format(mid))

        while query.strip().lower() != "y" and query.strip().lower() != "n":
            print('wrong input')
            query = input("is {} the number you guessed? Type (y/n): ".format(mid))

        if query.strip().lower() == 'y':
            print('Get in!!!! 1-0 to me. Machines are always better bruv... It only took {} {} lol.'.format(num_guesses, 'guess' if num_guesses == 1 else 'guesses'))
            return
        else:
            query2 = input('Was my guess higher (h) or lower (l) than your number? Type (h/l): ')
            while query2 != 'h' and query2 != 'l':
                query2 = input('Was my guess higher (h) or lower (l) than your number? Type (h/l): ')
            if query2 == 'h':
                guess(l,mid-1,num_guesses)
            else:
                guess(mid+1,h,num_guesses)
            
        return
    print("Pick a number from 0 to 100. I'm going to try and guess it!")
    guess(0,100, 0)

# selection sort is O(n^2) time complexit because for each iteration 0-n we must find what the smallest element is in the array
def selection_sort(unsorted_list:list):
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest = min(unsorted_list)
        sorted_list.append(smallest)
        unsorted_list.pop(unsorted_list.index(smallest))
    print(sorted_list)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = [arr[random.randint(0, len(arr)-1)]]
    left = [x for x in arr if x < pivot[0]]
    right = [y for y in arr if y > pivot[0]]
    return quick_sort(left) + pivot + quick_sort(right)


#we use bfs to ask and answer two questions: is there a path from A to B? If so, what is the shortest path.
def find_mango_seller(person):
    people = {}
    people['william'] = ['steph', 'vicky', 'aaron']
    people['vicky'] = ['steph', 'aaron', 'william']
    people['steph'] = ['quinn', 'shore', 'william', 'hailey']
    people['aaron'] = ['vicky', 'steph', 'william']
    people['shore'] = ['william', 'quinn', 'steph']
    people['hailey'] = ['steph']
    people['quinn'] = ['william', 'steph', 'shore', 'simgbi', 'billy']
    people['simgbi'] = ['shore', 'quinn', 'steph', 'millionz']
    people['billy'] = ['quinn']
    people['millionz'] = ['lagga lagga']
    people['bryan'] = ['hailey', 'steph']

    mango_sellers = ['billy', 'millionz', 'bryan']

    search_queue = deque()

    searched = []
    if person in people:
        search_queue = deque(people[person])
    else:
        print(f'Person {person} is not in the network')
        return False
    
    levels = 1
    while search_queue:
        conn = search_queue.popleft()
        if conn in mango_sellers and conn != person:
            searched.append(conn)
            print(f"You've found a mango seller {conn} in your network")
            print(searched)
            return True
        else:
            if conn not in searched and conn != person:
                search_queue+=people[conn]
                searched.append(conn)
    print('No mango sellers found in your entire network')
    return False


def find_mango_sellers_recur(root_person, parent, level, searched:list):
    people = {}
    people['william'] = ['steph', 'vicky', 'aaron']
    people['vicky'] = ['steph', 'aaron', 'william']
    people['steph'] = ['quinn', 'shore', 'william', 'hailey']
    people['aaron'] = ['vicky', 'steph', 'william']
    people['shore'] = ['william', 'quinn', 'steph']
    people['hailey'] = ['steph']
    people['quinn'] = ['william', 'steph', 'shore', 'simgbi', 'billy']
    people['simgbi'] = ['shore', 'quinn', 'steph', 'millionz']
    people['billy'] = ['quinn', 'lagga lagga', 'nvidia']
    people['lagga lagga'] = []
    people['nvidia'] = []
    people['millionz'] = ['lagga lagga', 'batty boi', 'ypree', 'SL', 'badnis', 'funny youtes']
    people['funny youtes'] = ['boris johnson', 'lizzy', 'teresa may', 'pretty priti']
    people['boris johnson'] = ['handsy hancock']
    people['lizzy'] = ['charles', 'william', 'harry', 'kate']
    people['harry'] = ['megs']
    people['charles'] = ['phillip']
    people['phillip'] = ['andrew']
    people['bryan'] = ['hailey', 'steph']

    people['andrew'] = ['epstien']

    mango_sellers = ['handsy hancock', 'epstien', 'bryan']

    # if parent in mango_sellers and parent != root_person:
    #     searched.append(parent)
    #     print(f"{'    '*level}|__ |{parent}|")
    #     return parent

    if parent not in searched:
        if len(searched) == 0:
            print(f"|__ {parent}")
        searched.append(parent)

        if any((children in mango_sellers and children != root_person) for children in people[parent]):
            m_seller = ""
            for child in people[parent]:
                searched.append(child)
                if child in mango_sellers and child != root_person:
                    m_seller+= child
                    print(f"{'    '*(level+1)}|__ ***|{child}|***  FOUND {level} levels deep")
                elif child not in searched:
                    print(f"{'    '*(level+1)}|__ {child}")
            return True

        else:
            for child in people[parent]:
                if child not in searched and child in people:
                    print(f"{'    '*level}|__ {child}")
                    find_mango_sellers_recur(root_person,child,level+1,searched+[x for x in people[parent] if x != child])
    return False


# dijkstra's algorithm
# while bfs gives us shortest path, dijkstra's gives us fastest path
# fastest doesn't necesarily mean time, or smallest number of edges to get to a node. it has to do with minimising the metric of weights on the edges, like minimising cost, minimising time, etc
# dijkstra's works with DAGs (Directed Acyclic Graphs) meaning edges are directed in one direction. No bi-directional relationships between nodes
# dijkstra's does not do well with negative weights; for that we use Bellman-Ford algorithm

# note to self: try dijkstras from any starting position. Implement Bellman-Ford algorithm
def find_cheapest_trade(start, end):
    trade_net = {}
    trade_net['Book'] = {'LP': 5, 'Poster': 0}
    trade_net['LP'] = {'Guitar': 15, 'Drum Set': 20, 'Poster': -7}
    trade_net['Poster'] = {'Guitar': 30, 'Drum Set': 35}
    trade_net['Guitar'] = {'Piano': 20}
    trade_net['Drum Set'] = {'Piano': 10}
    trade_net['Piano'] = {}

    trade_parents = {'LP': 'Book', 'Poster': 'Book', 'Guitar': None, 'Drum Set': None, 'Piano': None}

    inf = float('inf')
    trade_costs = {'Book': 0, 'LP': 5, 'Poster': 0, 'Guitar': inf, 'Drum Set': inf, 'Piano': inf}
    visited = []

    def find_cheapest():
        m = inf
        cheapest = None
        for x in trade_costs.keys():
            if x not in visited and trade_costs[x] < m:
                m = trade_costs[x]
                cheapest = x
        return cheapest
    


    cheapest_node = find_cheapest()

    while cheapest_node is not None:
        cost = trade_costs[cheapest_node]
        neighbours = trade_net[cheapest_node]
        for n in neighbours:
            accum_cost = cost + neighbours[n]
            if trade_costs[n] > accum_cost:
                trade_costs[n] = accum_cost
                trade_parents[n] = cheapest_node
        visited.append(cheapest_node)
        cheapest_node = find_cheapest()

    cheapest_path = []
    cur_parent = end
    while cur_parent != start:
        cheapest_path.append(cur_parent)
        cur_parent = trade_parents[cur_parent]
    cheapest_path.append(cur_parent)

    pth = ""
    cheapest_path.reverse()
    for i, item in enumerate(cheapest_path):
        pth+='{}{}'.format(item, ("--"+str(trade_costs[cheapest_path[i+1]]-trade_costs[cheapest_path[i]])+"--> " if i+1 <= len(cheapest_path)-1 else "") )
    print(pth)
    
    return cheapest_path




# covering stations greedy algorithm
def cover_stations():
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])

    stations_to_use = set()

    while states_needed:
        best_station = None
        most_states_covered = set()

        for station, states_in_station in stations.items(): #loop through each station, and each state in station in the stations dict
            covered_by_cur_station = states_needed & states_in_station #the states this current station covers that also are stations that we need to cover

            if len(covered_by_cur_station) > len(most_states_covered): # if this station covers more stations we need than a previous one, make it the current best
                best_station = station
                most_states_covered = covered_by_cur_station
            
        states_needed-=most_states_covered
        stations_to_use.add(best_station)

        print(f'best stations: {stations_to_use} states needed: {states_needed}')

    return stations_to_use


def fib_dp(i:int, computed={}):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i in computed:
        return computed[i]
    else:
        fibi = fib_dp(i-1) + fib_dp(i-2)
        computed[i] = fibi
        return fibi

def factorial_dp(i:int, computed={}):
    if i <= 1:
        return 1
    elif i in computed:
        return computed[i]
    else:
        prod = i * factorial_dp(i-1)
        computed[i] = prod
        return prod 


def display_grid(grid):
    s = "".join(f'{x}\n' for x in grid)
    print(s)

def classic_knapsack():
    items = {
        'guitar': [1500, 1],
        'stereo': [3000, 4],
        'laptop': [2000, 3],
        'phone': [2000, 1]
    }
    grid = [[0,0,0,0] for i in range(len(items))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            itmkeys = list(items.keys())
            itm_lbs = items[itmkeys[i]][1]
            cell_cap = j+1
            itm_val = items[itmkeys[i]][0]


            if itm_lbs > cell_cap:
                grid[i][j] = grid[i-1][j] # use the previous column max if the item weight exceeds cell capacity
            elif itm_lbs == cell_cap:
                grid[i][j] = itm_val
            else:
                new_cell_val = itm_val + grid[i-1][j-itm_lbs] # j - itm_lbs is the remaining capacity in this cell. Thus grid[i-1][j-itm_lbs] is the corresponding item and item value of that remaining capacity
                prev_max = grid[i-1][j]
                grid[i][j] = max(new_cell_val, prev_max)
            display_grid(grid)

    return


def classic_knapsack_with_non_interger_sacs():
    items_val = {
        'guitar': 1500,
        'stereo': 3000,
        'laptop': 2000,
        'phone': 2000,
        'diamond': 10000
    }
    
    items_lbs = {
        'guitar': 1,
        'stereo': 4,
        'laptop': 3,
        'phone': 1,
        'diamond': .6
    }

    idx_to_lbs = {}

    for i, itm in enumerate(items_lbs.keys()):
        idx_to_lbs[i] = items_lbs[itm]

    hitm, litm = max(items_lbs.values()), min(items_lbs.values())

    weights = []
    c = litm
    while c < hitm:
        weights.append(c)
        c+=litm
    weights.append(hitm)

    grid = [[0]*len(weights) for i in range(len(items_lbs))]

    display_grid(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            itmkeys = list(items_val.keys())
            itm_lbs = idx_to_lbs[i]
            cell_cap = weights[j]
            itm_val = items_val[itmkeys[i]]

            if itm_lbs > cell_cap:
                grid[i][j] = grid[i-1][j] # use the previous column max if the item weight exceeds cell capacity
            elif itm_lbs == cell_cap:
                grid[i][j] = itm_val
            else:
                rem_space = cell_cap - itm_lbs
                new_cell_val = itm_val + grid[i-1][j-itm_lbs] # j - itm_lbs is the remaining capacity in this cell. Thus grid[i-1][j-itm_lbs] is the corresponding item and item value of that remaining capacity
                prev_max = grid[i-1][j]
                grid[i][j] = max(new_cell_val, prev_max)
            display_grid(grid)

    return


def edge_list_to_graph(edge_list:list):
    graph = {}
    for edge in edge_list:
        l,r = edge
        if l not in graph:
            graph[l] = []
        if r not in graph:
            graph[r] = []      
        graph[l].append(r)
        graph[r].append(l)
    return graph

def dfs_using_array_stack(edge_list:list, source_node):
    graph = edge_list_to_graph(edge_list)
    
    visited = set()
    stack = [source_node]
    print(graph)
    while len(stack) > 0:
        top = stack.pop()
        print(top)
        visited.add(top)
        for neighbour in graph[top]:
            if neighbour not in visited:
                stack.append(neighbour)

    return

def dfs_using_call_stack(graph:dict, visited:set, source_node):
    print(source_node)
    visited.add(source_node)
    for neighbour in graph[source_node]:
        if neighbour not in visited:
            dfs_using_call_stack(graph, visited, neighbour)
    return

def bfs_arr_queue(edge_list:list, source_node):
    graph = edge_list_to_graph(edge_list)
    visited = set()
    queue = [ source_node ]
    print(graph)
    while len(queue) > 0:
        top = queue.pop(0)
        print(top)
        visited.add(top)
        for neighbour in graph[top]:
            if neighbour not in visited:
                queue.append(neighbour)
    return

def has_path_dfs(graph, current, target, visited, path):
    path.append(current)
    visited.add(current)
    if current == target:
        return True,path
    for neighbour in graph[current]:
        if neighbour not in visited:
            is_target, full_path = has_path_dfs(graph, neighbour, target, visited, path[0:])
            if is_target:
                return True, full_path
    return False, []

def has_path_bfs(graph, source, target):
    visited = set()
    queue = [ source ]
    while queue:
        front = queue.pop(0)
        print(front)
        visited.add(front)
        if front ==  target:
            return True
        for neighbour in graph[front]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False

def count_connected_nodes(graph): #similar to count number islands
    visited = set()
    num_node_groups = 0

    for node in graph.keys():
        is_connected = explore_nodes_bfs(node, graph, visited)
        if is_connected:
            num_node_groups+=1
    print(num_node_groups)
    return num_node_groups

def explore_nodes_bfs(source, graph, visited):
    if source in visited:
        return False
    
    queue = [ source ]
    while len(queue) > 0:
        front  = queue.pop(0)
        visited.add(front)
        for neighbour in graph[front]:
            if neighbour not in visited:
                queue.append(neighbour)

    return True # can return true here because we know the nodes have been traversed to their fullest


def largest_island(graph):
    visited = set()
    largest = 0
    for node in graph.keys():
        node_count = count_nodes_dfs(node, graph, visited)
        largest = max(largest, node_count)

    return largest

def count_nodes_bfs(source, graph:dict, visited:set):
    if source in visited:
        return 0
    queue = [ source ]
    count  = 0
    while len(queue) > 0:
        front = queue.pop(0)
        if front not in visited:
            count+=1
        visited.add(front)
        for neighbour in graph[front]:
            if neighbour not in visited:
                queue.append(neighbour)

    return count

def count_nodes_dfs(source, graph:dict, visited:set):
    if source in visited:
        return 0
    
    count = 1
    visited.add(source)

    for neighbour in graph[source]:
        if neighbour not in visited:
            count += count_nodes_dfs(neighbour, graph, visited)

    return count


# shortest path algorithm is always BFS unless in the case of minimising weighted edges
# then use Dijkstras 

def length_of_shortest_path(graph, start, end):
    visted = set()
    queue = [ [start, 0] ]

    while len(queue) > 0:
        node, distance = queue.pop(0)
        visted.add(node)
        if node == end:
            return distance
        
        for neighbour in graph[node]:
            if neighbour not in visted:
                queue.append([neighbour, distance+1])  


    return -1


def count_island(grid_graph):
    visited = set()
    num_islands = 0
    for i in range(len(grid_graph)):
        for j in range(len(grid_graph[0])):
            cell = f'{i},{j}'
            is_island = search_islands(cell, grid_graph, visited)
            if is_island:
                num_islands+=1
    return num_islands

def search_islands(cell, grid:list, visited:set):
    if cell in visited:
        return False
    
    row, col = int(cell.split(',')[0]), int(cell.split(',')[1])
    row_in_range = 0 <= row and row < len(grid)
    col_in_range = 0 <= col and col < len(grid[0])

    if not row_in_range or not col_in_range:
        return False

    if grid[row][col] == 'W':
        return False
    
    visited.add(cell)

    for neighbour in [f'{row-1},{col}', f'{row+1},{col}', f'{row},{col-1}', f'{row},{col+1}']:
        if neighbour not in visited:
            search_islands(neighbour, grid, visited)

    return True



def find_smallest_island(grid:list):
    return


def main():
    edge_list = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"]
    ]
    test_graph = {
        "a": ["b", "c"],
        "b": ["d", "c"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    acyc_graph = {
        "f": ["g", "i"],
        "g": ["h"],
        "h": [],
        "i": ["g", "k"],
        "j": ["i"],
        "k": []
    }

    structy_graph = {
        '0': ['8', '1', '5'],
        '1': ['0'],
        '5': ['0', '8'],
        '8': ['0', '5'],
        '2': ['3', '4'],
        '3': ['2', '4'],
        '4': ['3', '2']
    }

    shrtestpth_elist = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'z']
    ]

    # island_grid = [
    #     ['W', 'L', 'W', 'W', 'W'],
    #     ['W', 'L', 'W', 'W', 'W'],
    #     ['W', 'W', 'W', 'L', 'W'],
    #     ['W', 'W', 'L', 'L', 'W'],
    #     ['L', 'W', 'W', 'L', 'L'],
    #     ['L', 'L', 'W', 'W', 'W'],
    # ]

    # island_grid = [
    #     ['W', 'W'],
    #     ['W', 'W'],
    #     ['W', 'W'],
    # ]

    # island_count = count_island(island_grid)

    # print(island_count)

    print(fib_dp(23, {}))

    return


if __name__ == '__main__':
    main()



# problems to work on:
# steps counting to step i
# number ways to get to step i with max k jumps
# getting from top left to bottom right of grid moving only right or down, and minimising sum of path