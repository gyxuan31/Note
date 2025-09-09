from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        w1 = list(word1)
        w2 = list(word2)
        w1.sort()
        w2.sort()
        n1 = len(w1)
        n2 = len(w2)
        if n1 != n2:
            return False
        c1 = Counter(w1)
        c2 = Counter(w2)
        s1 = sorted(c1.values())
        s2 = sorted(c2.values())
        print(type(s1))
        if s1 is s2:
            return True
        return False

sol = Solution()
result = sol.closeStrings("cabbba", "aabbss")
print(result)