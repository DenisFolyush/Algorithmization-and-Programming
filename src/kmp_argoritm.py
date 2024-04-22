def prefix_func(needle):
    if not needle:
        return "no needle"

    needle_len = len(needle)
    prefix = [0] * needle_len
    j = 0
    i = 1
    while i < needle_len:
        if needle[j] == needle[i]:
            prefix[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                prefix[i] = 0
                i += 1
            else:
                j = prefix[j - 1]
    return prefix


def kmp_search(needle, haystack):
    result = []
    haystack_len = len(haystack)
    needle_len = len(needle)
    prefix = prefix_func(needle)
    i = 0
    j = 0
    while i < haystack_len:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == needle_len:
                result.append(i - needle_len)
                j = prefix[j - 1] if j > 0 else 0
        else:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    return result
