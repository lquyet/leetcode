# Template for IO
import sys

input = sys.stdin.readline
print = sys.stdout.write

def make_dp(shape, value=0):
    if len(shape) == 1:
        return [value] * shape[0]
    return [make_dp(shape[1:], value) for _ in range(shape[0])]


dp = make_dp((1, 2, 3), 0)   # 3D
