import math


def operations(n):
    if math.log(n, 2).is_integer():
        return [n // 2]

    result = [n + 1, n - 1]
    if n % 2 == 0:
        result.append(n // 2)
    return result


def solution(n):
    n = int(n)

    if n == 1:
        return 0

    visited = {n}
    queue = [(n, 0)]

    while queue:
        i = queue.pop(0)
        j, k = i

        for operation in operations(j):
            if operation == 1:
                return k + 1
            if operation not in visited:
                visited.add(operation)
                queue.append((operation, k + 1))
