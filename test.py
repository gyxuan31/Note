import numpy as np
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tgrid = np.array(grid).T
        tgrid = tgrid.tolist()
        for i, column in enumerate(tgrid):
            if column == grid[i]:
                return i
        return 0
a = Solution()
print(a.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
