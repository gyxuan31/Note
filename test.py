import numpy as np
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        tgrid = np.array(grid).T
        tgrid = tgrid.tolist()
        for column in tgrid:
            if column in grid:
                cnt += 1
        return cnt
a = Solution()
print(a.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
