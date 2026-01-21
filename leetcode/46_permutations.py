from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = []
        for i in permutations(nums):
            l.append(i)

        return l