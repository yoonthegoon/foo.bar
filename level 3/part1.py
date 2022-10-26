def solution(x, y):
    x, y = int(x), int(y)
    steps = 0

    while x != y:
        m, f = max(x, y), min(x, y)
        x, y = m - f, f
        steps += 1

    if x == 1:
        return str(steps)
    return 'impossible'
