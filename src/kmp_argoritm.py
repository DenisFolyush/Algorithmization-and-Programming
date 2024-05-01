def kmp_search(needle, haystack):
    if not needle:
        return True

    m = len(needle)
    n = len(haystack)
    p = [0] * m
    j = 0
    i = 1
    while i < m:

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

    result = []
    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - m)
                j = p[j - 1] if j > 0 else 0
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return result
