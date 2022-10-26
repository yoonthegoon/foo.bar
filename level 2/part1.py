# probably the most dumb way i've done a part

MOVES = [
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
]


def solution(src, dest):
    if src == dest:
        return 0

    pos = to_matrix(src)

    visited = [pos]
    queue = [(pos, 0)]

    while queue:
        s = queue.pop(0)
        t = s[1] + 1

        for square in knight(*s[0]):
            if square == to_matrix(dest):
                return t
            if square not in visited:
                visited.append(square)
                queue.append((square, t))


def knight(*pos):
    possible = []
    for move in MOVES:
        x, y = pos[0] + move[0], pos[1] + move[1]
        if 0 <= x < 8 and 0 <= y < 8:
            possible.append((x, y))
    return possible


def to_matrix(n):
    return n % 8, n // 8
