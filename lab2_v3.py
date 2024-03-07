def FindSquare(N, W, H):
    i = 1
    j = max(W, H) * N
    while i < j:
        mid = i + (j - i) // 2
        if check_capacity(W, H, N, mid):
            j = mid
        else:
            i = mid + 1
    return j


def check_capacity(w, h, N, x):
    val = (x // w) * (x // h)
    if val >= N:
        return True
    else:
        return False


W = 2
H = 3
N = 10

print(FindSquare(N, W, H))
