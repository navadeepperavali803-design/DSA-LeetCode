class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies=candies[0]
        for candie in candies:
            if candie > max_candies:
                max_candies = candie
        result=[]
        for candie in candies:
            if candie+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
        
