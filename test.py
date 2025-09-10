import sys
for line in sys.stdin:
    # 先读每组第一个数（每组的数据个数）
    cnt = int(line)
    print(cnt)
    # 读下一行作为该组的具体内容
    data_line = sys.stdin.readline().strip()
    data = list(map(int, data_line.split()))
    print(data_line)
    print(data)