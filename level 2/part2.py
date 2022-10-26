from distutils.version import LooseVersion


def solution(l):
    l.sort(key=LooseVersion)
    return l
