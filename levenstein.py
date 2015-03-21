
def levenstein(s1, s2):
    n = range(0, len(s1) + 1)
    for y in xrange(1, len(s2) + 1):
        l, n = n, [y]
        for x in xrange(1, len(s1) + 1):
            n.append(min(l[x] + 1, n[-1] + 1, l[x - 1] +
                         ((s2[y - 1] != s1[x - 1]) and 1 or 0)))
    return n[-1]