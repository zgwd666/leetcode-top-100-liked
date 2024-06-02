#https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
'''利用哈希表来存储具有相同字符的字符串，然后将字符串提取出来。
解题思路：
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<2:#当数组中只存在0或1个字符串的时候，那么组合就是其本身
            return [strs]
        hmap={}#初始化哈希表
        for s in strs:#对数组中的每个字符串进行遍历
            key=str(sorted(s))#对字符串中的字符进行崇重新组合，这样异位词就会得到同一个key
            if key in hmap:#如果哈希表中已经存在当前的key
                hmap[key].append(s)#在当前的key的value中加入当前的字符
            else:
                hmap[key]=[s]#如果哈希表中不存在当前的key，则新创建key-value
        res=[lst for lst in hmap.values()]#将哈希表中的同一个key代表的value提取到同一个列表中
        return res#返回结果
