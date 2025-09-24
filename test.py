from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n_r = 0
        n_d = 0
        q = deque(senate)

        while len(q) > 1 or (('R' in q) and ('D' in q)):
            q_new = deque()
            for c in q:
                if n_r > 0 and c == 'R':
                    n_r -= 1
                    continue
                elif n_d > 0 and c == 'D':
                    n_d -= 1
                    continue
                elif c == 'R':
                    n_d += 1
                    q_new.append(c)
                else:
                    n_r += 1
                    q_new.append(c)
            q = q_new
        if q[0] == 'R':
            return 'Radiant'
        else:
            return 'Dire'
a = Solution()
print(a.predictPartyVictory("RRR"))
