from queue import PriorityQueue

class Map:
    def __init__(self, grid, num_rows, num_cols):
        self.nodes = list()
        self.edges = dict()

        for y in range(num_rows):
            for x in range(num_cols):
                # Get create a node
                self.nodes.append((x,y))
                self.edges[(x,y)] = list()

                col = grid[y][x]
                # Get height for this node
                this = height(col)

                # Check up
                try:
                    other = height(grid[y-1][x])
                    if this - other >= -1:
                        self.edges[(x,y)].append((x,y-1))
                except KeyError:
                    pass

                # Check right
                try:
                    other = height(grid[y][x+1])
                    if this - other >= -1:
                        self.edges[(x,y)].append((x+1,y))
                except KeyError:
                    pass

                # Check down
                try:
                    other = height(grid[y+1][x])
                    if this - other >= -1:
                        self.edges[(x,y)].append((x,y+1))
                except KeyError:
                    pass
                
                # Check left
                try:
                    other = height(grid[y][x-1])
                    if this - other >= -1:
                        self.edges[(x,y)].append((x-1,y))
                except KeyError:
                    pass
        # print(self.edges)

    def djikstras(self, start):
        # Tracks which nodes have been visited
        visited = list()
        # Set initial distances for each node
        D = {n:float('inf') for n in self.nodes}
        D[start] = 0 # Initital distance of the start is 0
        # Track which nodes to visit
        pq = PriorityQueue()
        pq.put((D[start], start)) # Initial starting point

        # While there are no more nodes to visit
        while not pq.empty():
            # Deque from the pq
            (dist, current_vertex) = pq.get()
            # And note what has been visited
            visited.append(current_vertex) 
            # For each neighbor
            for neighbor in self.edges[current_vertex]:
                # If it hasn'te been visited already
                if neighbor not in visited:
                    # Update costs to get there
                    old_cost = D[neighbor]
                    # Edges are equally weighted at one
                    new_cost = D[current_vertex] + 1 
                    # Update in our distances
                    if new_cost < old_cost:
                        # Eventually visit these neighbors
                        pq.put((new_cost, neighbor)) 
                        # Update the actual cost
                        D[neighbor] = new_cost
        return D

def height(val):
    if val == "S":
        return ord("a") - ord("a")
    elif val == "E":
        return ord("z") - ord("a")
    else:
        v = ord(val) - ord("a")
        return v

def print_grid(grid, num_rows, num_cols):
    for y in range(num_rows):
        for x in range(num_cols):
            print(grid[y][x], end="")
        print()

with open("aoc-12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    num_rows = len(lines)
    num_cols = len(lines[0])

    start = None
    end   = None

    grid = dict()

    for y, row in enumerate(lines):
        grid[y] = dict()
        for x, col_value in enumerate(row):

            if col_value == "S":
                start = (x, y)

            if col_value == "E":
                end = (x, y)

            grid[y][x] = col_value

    print(f"S: {start}")
    print(f"E: {end}")
    print_grid(grid, num_rows, num_cols)

    heightmap = Map(grid, num_rows, num_cols)
    D = heightmap.djikstras(start)
    print(D[end])
