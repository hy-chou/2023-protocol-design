def perm(s, oneline):
    return [s[i] for i in oneline]


def inve(s, oneline):
    tmp = [-1 for _ in range(len(oneline))]
    for i, p in enumerate(oneline):
        tmp[p] = s[i]
    return tmp
