#https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题实质上是对于矩阵的一个模拟，需要关注的问题在于矩阵的四个边界点（左上、右上、右下、左下）的处理，不要重复即可。具体的算法流程为：

定义四个边界值，l,r,t,b分别代表左 右 上 下

1.从左上角进行出发，从左到右将元素加入结果中，此时添加上右上角的元素。t+1

2.从此时的t开始，从上到下将元素加入结果中，此时添加右下角的元素，r-1

3.从此时的r开始，从右到左将元素加入结果中，此时添加左下角的元素，b+1

4.从此时的b开始，从下到上将元素加入结果中，此时添加下一层的左上角元素,l+1

进行下一轮的遍历。

在上述的遍历中，发现左右边界或者上下边界的关系不存在，即跳出循环返回结果
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])#获取当前矩阵的行列值
        res=[]#创建结果数组
        l,r,b,t=0,n-1,m-1,0#初始化四个边界值
        while True:#进行遍历
            #从左上角进行出发，从左到右将元素加入结果中，此时添加上右上角的元素。t+1
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            if t>b:break
            #从此时的t开始，从上到下将元素加入结果中，此时添加右下角的元素，r-1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if l>r:break
            #从此时的r开始，从右到左将元素加入结果中，此时添加左下角的元素，b+1
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            if t>b:break
            #.从此时的b开始，从下到上将元素加入结果中，此时添加下一层的左上角元素,l+1
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
            if l>r:break
            #在上述的遍历中，发现左右边界或者上下边界的关系不存在，即跳出循环返回结果
        return res#返回结果
