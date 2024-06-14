#https://leetcode.cn/problems/jump-game/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
根据贪心算法，依次计算每个位置能到达的最大位置。

如果当前位置的最大覆盖范围比自己的下标小，就证明该位置不可到达，就返回False。
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:#数组中只有一个元素，一定可以到达
            return True
        index=cover=0#初始化下标和最大覆盖范围都是0
        while index<=cover:#进行遍历，当最大覆盖范围可以覆盖当前下标时
            cover=max(cover,index+nums[index])#更新最大覆盖范围是最大覆盖范围和当前位置能到达的最大下标中的最大值
            if cover>=len(nums)-1:#如果最大覆盖范围能覆盖到最后一个下标，返回True
                return True
            index+=1#更新到下一个下标计算最大覆盖范围
        return False#当最大覆盖范围无法覆盖到最后一个下标，返回False
