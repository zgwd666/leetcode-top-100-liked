#https://leetcode.cn/problems/number-of-islands/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用双层循环，对数组中每一个点进行遍历，在遍历过程中采用BFS进行遍历，对访问过的地方进行标识。

当当前点的值为1且之前未被遍历过，则代表找到一个新的岛屿，结果加一，否则直接跳过当前点 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])#获取数组的行列数
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向
        Visited=[[False for i in range(n)]for i in range(m)]#创建表示函数
        def bfs(grid,Visited,x,y):#BFS函数
            queue=[(x,y)]#将当前点加入到队列中
            Visited[x][y]=True#该点的位置被标识已经访问
            while queue:#对队列进行遍历
                curx,cury=queue.pop(0)#点位出队
                for dx,dy in dir:#获取该店的四个方向
                    nextx,nexty=curx+dx,cury+dy#计算下一个点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or grid[curx][cury]=='0' or Visited[nextx][nexty]:#如果下一个点超过范围或者值等于0或者已经访问过，直接跳过
                        continue
                    Visited[nextx][nexty]=True#否则将下一个点进行标记
                    queue.append((nextx,nexty))#将下一个点加入队列
        res=0#初始化res
        #对数组进行遍历
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not Visited[i][j]:#当点的值为1且未被标记
                    res+=1#结果加一
                    bfs(grid,Visited,i,j)#将与该点一起构成同一个岛屿的点标记
        return res#返回结果
