def kmp_search(needle, haystack):
    p = [0] * len(needle)
    j = 0
    i = 1
    if not needle:
        return True
    while i < len(needle):
        if needle[j] == needle[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]

    m = len(needle)
    n = len(haystack)

    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return False
