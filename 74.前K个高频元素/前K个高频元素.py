#https://leetcode.cn/problems/top-k-frequent-elements/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：使用哈希表存储num出现的频率，然后对其按照num出现的频率进行排序，然后返回数组前k个元素即可
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}#创建哈希表
        for num in nums:#对数组每一个元素遍历，记录num出现的频率
            if num not in hmap:
                hmap[num]=1
            else:
                hmap[num]+=1
        res=sorted(hmap,key=lambda x:hmap[x],reverse=True)#对hamp进行排序，按照num出现的频率，返回的结果时数组，降序排序
        return res[0:k]#返回前k个元素
