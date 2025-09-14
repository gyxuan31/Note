import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
n = int(sys.stdin.readline())
tmp = sys.stdin.readline().split()
nums = [0]*n
ans = [0]*n
for i in range(n):
    nums[i] = int(tmp[i])
t = 0
for i in range(n-1, -1, -1):
    while (t in nums[i:n]) or t < max(nums[i:n]):
        t += 1
    ans[i] = t

for i in range(n):
    print(ans[i], end=' ')