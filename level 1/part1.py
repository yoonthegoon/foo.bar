def factors(n):
    f = []
    for i in range(n + 1, 1, -1):
        if n % i == 0:
            f.append(i)
    return f


def cut(s, f):
    return True if s[:len(s)//f]*f == s else False


def solution(s):
    for i in factors(len(s)):
        if cut(s, i):
            return i
    return
