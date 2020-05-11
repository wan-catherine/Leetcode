class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(image, sr, sc, currentColor, newColor):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] == newColor or image[sr][sc] != currentColor:
                return image

            image[sr][sc] = newColor
            dfs(image, sr-1, sc, currentColor, newColor)
            dfs(image, sr+1, sc, currentColor, newColor)
            dfs(image, sr, sc-1, currentColor, newColor)
            dfs(image, sr, sc+1, currentColor, newColor)
            return image
        return dfs(image, sr, sc, image[sr][sc], newColor)