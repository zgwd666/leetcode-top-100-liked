#https://leetcode.cn/problems/merge-intervals/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：对于数对问题，一般都会对数对进行排序以简化问题。

就本题而言，要求合并区间，我们可以将区间的左边界从小到大进行排序，然后在遍历每一个区间时，我们将该位置的区间更新为该位置与之前区间能够产生交集的最大区间。
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:#当数组中仅有一个区间时，那么就不需要合并
            return intervals
        intervals=sorted(intervals,key=lambda x:x[0])#将数组按照区间的左边界进行升序排序
        res=[intervals[0]]#初始化结果数组
        for i in range(1,len(intervals)):#从1开始遍历
            if intervals[i][0]<=intervals[i-1][1]:#当当前区间与之前的区间出现交集时，将本区间更新为当前区间与之前区间的并集，并将结果中的区间进行更新
                intervals[i][0]=min(intervals[i][0],intervals[i-1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i-1][1])
                res[-1]=intervals[i]
            else:#如果没有产生交集，那么就是一个新的区间，加入到结果中
                res.append(intervals[i])
        return res#返回结果
