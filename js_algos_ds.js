/*
algos
    [] binary search
    [] selection sort
    [] quick sort
    [] insertion sort
    [] merge sort
    [] heap sort
    [] breath first search
    [] depth first search
    [] dijkstras algorithm
    [] covering stations greedy algorithm
    [] greedy algorithms
    [] dynamic programming (fib, factorial, knapsack problem)
    [] path finding in graphs
data structures
    [] Arrays
    [] Sets
    [] HashMaps / Dictionaries 
    [] Array stack
    [] Array queue
    [] DoubleEnded Queue
    [] Linked Lists (Singly, and Doubly)
    [] Linked Stack
    [] Linked Queue
    [] Graphs
    [] Binary Trees
    [] Binary Search Trees
    [] Array Binary Trees
    [] Heaps
*/


const dfs_array_stack = (source, graph) => {
    let visited = new Set();
    let stack = [ source ];

    while(stack.length > 0) {
        let top = stack.pop();
        console.log(top);
        visited.add(top);
        for(let neighbour of graph[top]) {
            if(!visited.has(neighbour)) {
                stack.push(neighbour);
            }
        }
    }
}

const dfs_call_stack = (source, graph, visited) => {
    console.log(source);
    visited.add(source);
    for(let neighbour of graph[source]) {
        if(!visited.has(neighbour)) {
            dfs_call_stack(neighbour);
        }
    }
}

const bfs_arr_queue = (source, graph) => {
    let visited = new Set();
    let queue = [ source ];

    while(queue.length > 0) {
        let front = queue.shift();
        console.log(front);
        visited.add(front);

        for(let neighbour of graph[front]) {
            if(!visited.has(neighbour)) {
                queue.push(neighbour);
            }
        }
    }
}

const has_path_dfs = (current, target, graph, visited) => {
    visited.add(current);
    if(current === target) {
        return true;
    }
    for(let neighbour of graph[current]) {
        if(!visited.has(neighbour)) {
            let found = has_path_dfs(neighbour, target, graph, visited);
            if(found) {
                return true;
            }
        }
    }
    return false;
}

const has_path_bfs = (current, target, graph) => {
    let visited = new Set();
    let queue = [ current ];

    while(queue.length > 0) {
        let front = queue.shift();
        visited.add(front);

        if(front === target) {
            return true;
        }

        for(let neighbour of graph[front]) {
            if(!visited.has(neighbour)) {
                queue.push(neighbour);
            }
        }
    }
    return false;
}

const count_connected_nodes = (graph) => {
    let visited = new Set();
    let islands = 0;
    for(let node in graph) {
        let is_island = explore_nodes(node, graph, visited);
        if(is_island) {
            islands+=1;
        }
    }
    return islands;
}

const explore_nodes_bfs = (source, graph, visited) => {
    if(visited.has(source)) {
        return false;
    }
    let queue = [ source ];
    while(queue.length > 0) {
        let front = queue.shift();
        visited.add(front);
        for(let neighbour of graph[front]) {
            if(!visited.has(neighbour)) {
                queue.push(neighbour);
            }
        }
    }
    return true;
}

const largest_island = (graph) => {
    
}


