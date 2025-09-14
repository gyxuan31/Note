import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
def check(t):
    tmpl = tmpr = 0
    for i in range(len(t)):
        if i > 0:
            tmpl = abs(t[i] - t[i-1])
        if i < len(t)-1:
            tmpr = abs(t[i] - t[i+1])
    if tmpl != 1 and tmpr != 1:
        return True
    return False

res = 0 
def f(i):
    global res
    if i == len(nums):
        if check(ans):
            return res+1
        return res
    ans.append(nums[i])
    f(i+1)
    ans.pop()
    f(i+1)

n_test = int(sys.stdin.readline())
for test in range(n_test):
    n = int(sys.stdin.readline())
    nums = [0] * n
    tmp = sys.stdin.readline().split()
    for i in range(n):
        nums[i] = int(tmp[i])
    ans = []

