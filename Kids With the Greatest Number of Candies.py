class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [ candies[i] + extraCandies >= maxCandies for i in range(len(candies))]