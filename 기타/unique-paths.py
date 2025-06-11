class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list1=[[0]*n for i in range(m)]

        for j in range(n):
            list1[0][j]=1
        for i in range(m):
            list1[i][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                list1[i][j]=list1[i][j-1]+list1[i-1][j]

        return list1[m-1][n-1]
