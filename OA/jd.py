
# 题目内容
# 小明有一个长度为n的数组a。
# 小明可以对数组执行最多k次如下操作：
# 指定数组中的某个元素a_i，令a_i = a_i+1。对于同一个位置的元素可以多次进行操作。
# 小明想要最小化数组中相邻元素差的绝对值的最大值，请你帮助他计算。

# 输入描述
# 输入包括多组测试数据。
# 输入第一行有一个正整数T，表示测试数据的组数。

# 对于每组测试数据：
# 第一行有两个正整数n(1<=n<=10^5)，k(0<=k<=10^9) 分别表示数组的长度、操作最多可以执行多少次。
# 接下来的一行有n个整数a_1, ...，a_n, 表示题目给定的数组。

# 输出描述
# 对于每组测试数据，输出一个正整数，表示经过操作后数组中相邻元素差的绝对值的最大值最小是多少。

# 输入样例
# 1
# 5 3
# 3 1 5 4 1
# 输出

# 2

'''
import sys
n_test = int(input())
def f(i, n, k, nums):
    if i == n or k == 0:
        ab = [0]*n
        for t in range(n):
            tmpl = tmpr = 0
            if t > 0:
                tmpl = abs(nums[t]-nums[t-1])
            if t < n-1:
                tmpr = abs(nums[t]-nums[t+1])
            ab[t] = max(tmpl, tmpr)
        return max(ab)
    nums[i] += 1
    a = f(i, n, k-1, nums)
    nums[i] -= 1
    b = f(i+1, n, k, nums)
    return min(a, b)
for i in range(n_test):
    n, k = map(int, sys.stdin.readline().split())
    num = sys.stdin.readline().split()
    nums = [0]*n
    for t in range(n):
        nums[t] = int(num[t])
    print(f(0, n, k, nums))
'''

import sys
def need_ops(a, X):
    """给定X，返回把数组抬到|相邻差|<=X所需的最小加法次数"""
    n = len(a)
    b = a[:]  # 复制一份作为工作数组
    # 正向：右侧至少为 左侧-X
    for i in range(1, n):
        if b[i] < b[i-1] - X:
            b[i] = b[i-1] - X
    # 反向：左侧至少为 右侧-X
    for i in range(n-2, -1, -1):
        if b[i] < b[i+1] - X:
            b[i] = b[i+1] - X
    # 计算总加法次数（可能很大，用Python int即可）
    s = 0
    for i in range(n):
        s += b[i] - a[i]
    return s

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it)); k = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        # 设二分区间
        R = 0
        for i in range(n-1):
            d = abs(a[i] - a[i+1])
            if d > R: R = d
        L = 0
        # 二分最小可行X
        while L < R:
            mid = (L + R) // 2
            if need_ops(a, mid) <= k:
                R = mid
            else:
                L = mid + 1
        out.append(str(L))
    sys.stdout.write("\n".join(out))

solve()