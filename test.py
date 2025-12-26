with open("whereami.in", "r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()

def check(l: int):
    seen = set()
    for i in range(n - l + 1):
        sub = s[i:i+l]
        if sub in seen:
            return True
        seen.add(sub)
    return False

left, right = 1, n
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

with open("whereami.out", "w") as out:
    out.write(str(ans + 1) + "\n")
