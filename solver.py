
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan_distance(board):
    distance = 0

    for i in range(9):
        num = board[i]

        if num != 0:
            target = num - 1
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)

    return distance


def get_neighbors(board):
    empty = board.index(0)
    row = empty // 3
    col = empty % 3
    positions = []

    if row > 0:
        positions.append(empty - 3)
    if row < 2:
        positions.append(empty + 3)
    if col > 0:
        positions.append(empty - 1)
    if col < 2:
        positions.append(empty + 1)

    neighbors = []

    for pos in positions:
        new_board = list(board)
        new_board[empty], new_board[pos] = new_board[pos], new_board[empty]
        neighbors.append(tuple(new_board))

    return neighbors


def is_solvable(board):
    numbers = [n for n in board if n != 0]
    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                count += 1

    return count % 2 == 0


def solve_puzzle(board):
    if len(board) != 9 or sorted(board) != list(range(9)):
        return []

    start = tuple(board)

    if not is_solvable(start):
        return []

    queue = [(manhattan_distance(start), 0, start)]
    costs = {start: 0}
    parents = {start: None}

    while queue:
        _, moves, current = heapq.heappop(queue)

        if moves != costs[current]:
            continue

        if current == GOAL:
            path = []

            while current is not None:
                path.append(list(current))
                current = parents[current]

            return path[::-1]

        for neighbor in get_neighbors(current):
            next_moves = moves + 1

            if neighbor not in costs or next_moves < costs[neighbor]:
                costs[neighbor] = next_moves
                parents[neighbor] = current

                score = next_moves + manhattan_distance(neighbor)
                heapq.heappush(queue, (score, next_moves, neighbor))

    return []
