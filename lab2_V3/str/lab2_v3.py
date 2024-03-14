def find_square(N, W, H):
    i = 1  # min square value
    j = max(W, H) * N  # and max
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

print(find_square(N, W, H))
