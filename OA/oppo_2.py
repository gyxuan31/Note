import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
n = int(sys.stdin.readline())
val = map(int, sys.stdin.readline().split())
tree = {}
ans = []

for i in range(n-1):
    e = [0, 0]
    tmp = sys.stdin.readline().split()
    e[0] = int(tmp[0])
    e[1] = int(tmp[1])
    e.sort()
    tree[e[0]].add(e[1])

for i in range(len(ans)):
    print(ans[i], end=' ')