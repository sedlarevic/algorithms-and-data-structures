class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        def dfs(image,sr,sc,newColor,starting_pixel):
            
            if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] == newColor or image[sr][sc] != starting_pixel:
                return

            image[sr][sc] = newColor

            dfs(image,sr+1,sc,newColor,starting_pixel)
            dfs(image,sr-1,sc,newColor,starting_pixel)
            dfs(image,sr,sc+1,newColor,starting_pixel)
            dfs(image,sr,sc-1,newColor,starting_pixel)
        
        dfs(image,sr,sc,color,image[sr][sc])

        return image
