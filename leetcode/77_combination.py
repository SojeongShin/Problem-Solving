from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = []
        num = [i+1 for i in range(n)]
        for i in combinations(num, k):
            l.append(list(i))

        return l
        