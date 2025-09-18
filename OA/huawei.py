import sys

def func():
    t = list(map(int, input().split()))
    h = t[0]
    w = t[1]
    k = t[2]
    image = [[0.0] * (w+2) for _ in range(h+2)]
    for i in range(1, h+1):
        image[i][1:w+1] = list(map(float, input().split()))
    kernel =[]
    for _ in range(k):
        kernel.append(list(map(float, input().split())))
    # compute energy
    energy_map = [[0.0] * w for _ in range(h)]
    for i in range(1,h+1):
        for j in range(1,w+1):
            s = 0
            for u in range(k):
                for v in range(k):
                    s += kernel[u][v] * image[i-k//2+u][j-k//2+v]
            energy_map[i-1][j-1] = s
    def dp(i, j, energy):
        if j == w:
            m[0] = max(m[0], energy)
            return 
        energy += energy_map[i][j]
        # 右上
        if i!=0:
            dp(i-1, j+1, energy)
        # 右
        dp(i, j+1, energy)
        if i < h-1:
            dp(i+1, j+1, energy)
        return 

    for i in range(h):
        dp(i,0,0)
    print(m[0])


m = [0]
func()

################################################################################
def main():
    dims = input().split()
    H, W, K = int(dims[0]), int(dims[1]), int(dims[2])
    if len(dims) == 4:
        K = int(dims[3])

    image = []
    for _ in range(H):
        line = input()
        while line.strip() == "":
            line = input()
        image.append([float(x) for x in line.strip().split()])

    kernel = []
    for _ in range(K):
        line = input()
        while line.strip() == "":
            line = input()
        kernel.append([float(x) for x in line.strip().split()])

    padding = K // 2
    energy_map = [[0.0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            energy = 0.0
            for u in range(K):
                for v in range(K):
                    ii = i + u - padding
                    jj = j + v - padding
                    if 0 <= ii < H and 0 <= jj < W:
                        energy += kernel[u][v] * image[ii][jj]
            energy_map[i][j] = energy

    NEG_INF = -1e100
    dp = [[NEG_INF] * W for _ in range(H)]
    for i in range(H):
        dp[i][0] = energy_map[i][0]

    for j in range(1, W):
        for i in range(H):
            best = dp[i][j - 1]
            if i > 0:
                best = max(best, dp[i - 1][j - 1])
            if i + 1 < H:
                best = max(best, dp[i + 1][j - 1])
            dp[i][j] = best + energy_map[i][j]

    result = max(dp[i][-1] for i in range(H))
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()