def solution(n):
    m = n + 1
    arr = [[0 for _ in range(m)] for _ in range(m)]

    arr[0][0] = 1
    for i in range(1, m):
        for j in range(m):
            arr[i][j] = arr[i - 1][j]
            if j >= i:
                arr[i][j] += arr[i - 1][j - i]
    return arr[n][n] - 1


if __name__ == '__main__':
    print(solution(200))
