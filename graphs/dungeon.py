"""
SHORTEST PATH WITH BREADTH FIRST SEARCH (BFS)
"""
import queue

class ShortestPath:
    def __init__(self, grid: list, start: tuple, verbose: bool = False):
        self.verbose = verbose

        # Class scope variables
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.start = start
        
        # Empty row queue (rq) and column queue (cq)
        self.rq = queue.Queue()
        self.cq = queue.Queue()

        # Variables to track the number of steps taken        
        self.move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0

        # Variable to track whether `end` has been reached
        self.reached_end = False

        # `rows` x `columns` matrix of False values to track visited positions
        self.visited = [[False for _ in cols] for cols in grid]

        # North, south, east, west direction vectors
        self.dr = [-1, +1, 0, 0]
        self.dc = [0, 0, -1, +1]

        # Run the algorithm
        self.solve()

    def solve(self):
        self.rq.put(self.start[0])
        self.cq.put(self.start[1])
        self.visited[self.start[0]][self.start[1]] = True

        while not self.rq.empty():
            r = self.rq.get()
            c = self.cq.get()

            if self.verbose:
                string = f'Move {self.move_count:>2}\t\t'
                string += f'Node: {r, c}\t'
                queue_list = [(x,y) for x, y in zip(self.rq.queue, self.cq.queue)]
                string += f'Queue: {str(queue_list)}'
                print(string)

            # Check if we reached the exit
            if self.grid[r][c] == 'E':
                self.reached_end = True

                if self.verbose:
                    print(f'End reached: {r, c}')
                break

            self.explore_neighbours(r, c)

            # Number of steps taken to get to the dungeon exit
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
        
        if self.reached_end:
            return self.move_count
        return -1

    def explore_neighbours(self, r, c):
        # Explore neighbours using the direction vectors
        # from the current position `r` `c`
        for i in range(4):
            rr = r + self.dr[i]
            cc = c + self.dc[i]

            # Skip out of bounds locations
            if rr < 0 or cc < 0: continue
            if rr >= self.rows or cc >= self.columns: continue

            # Skip visited locations
            if self.visited[rr][cc]: continue

            # Skip obstacles (indicated as `0` in the grid)
            if self.grid[rr][cc] == 0: continue

            # If valid position, enqueue to visit later
            self.rq.put(rr)
            self.cq.put(cc)
            self.visited[rr][cc] = True
            self.nodes_in_next_layer += 1
 
    def print_solved_grid(self):
        out = ''
        for i in range(self.rows):
            out += '\n'
            for j in range(self.columns):
                if self.grid[i][j] == 'E':
                    out += ' E '
                elif (i, j) == self.start:
                    out += ' S '
                elif self.visited[i][j]:
                    out += ' . '
                elif self.grid[i][j] == 0:
                    out += ' # '
                else:
                    out += ' - '
        print(out + '\n')


if __name__ == '__main__':
    print('-' * 60)
    print('Grid shortest path (BFS)')
    print('-' * 60)

    grid = [[1 for _ in range(8)] for _ in range(8)]
    grid[7][4] = 'E'
    grid[3][3] = 0
    grid[2][2] = 0
    grid[3][4] = 0
    grid[3][3] = 0
    grid[4][3] = 0
    grid[5][2] = 0
    grid[5][3] = 0
    grid[6][3] = 0
    grid[6][1] = 0
    grid[4][5] = 0
    grid[5][6] = 0
    grid[6][6] = 0
    grid[7][1] = 0

    grids = [
        [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 'E']], 
        grid
    ]

    test_cases = [
        (grids[0], (0, 0), 7),
        (grids[1], (3, 3), 13),
    ]

    for grid, start, solution in test_cases:
        print(f'Starting point: {start}')
        p = ShortestPath(grid, start)
        print('Dungeon:', end='')
        p.print_solved_grid()
        result = p.move_count
        print(f'Number of moves: {result}')
        if solution:
            print(f'Test: {"OK" if solution == result else "NOT OK"}')
        print()


    grid, start, _ = test_cases[0]
    print(f'>>> Verbose example:')
    p = ShortestPath(grid, start, verbose=True)
    p.print_solved_grid()