#https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用滑动窗口。
先统计p中每个字符出现的频率，与此同时计算从0开始和p等长的s中的字符串中每个字符出现的频率。然后从第二个字符开始，每次弹出第一个元素，添加新的字符，计算当前的频率，如果当前字符串各个字符出现的频率等于p中每个字符出现的频率，则将当前字符串的起始位置加入结果。
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):#如果s的长度比p小，不可能会有p的异位词，直接返回[]
            return []
        p_cnt=[0]*26#初始化p中各个字母出现的频率
        s_cnt=[0]*26#初始化s中各个字母出现的频率
        res=[]#初始化结果
        for i in range(len(p)):#对p进行遍历
            p_cnt[ord(p[i])-ord('a')]+=1#统计p中各个字母出现的频率
            s_cnt[ord(s[i])-ord('a')]+=1#统计s中第一个和p等长的字符串的各个字母出现的频率
        if p_cnt==s_cnt:#如果当前的p_cnt和s_cnt相等，res添加0
            res.append(0)
        for i in range(1,len(s)-len(p)+1):#从第一个字符开始遍历，到len(s)-len(p)结束
            s_cnt[ord(s[i-1])-ord('a')]-=1#将s_cnt中上一个的首位字符弹出，并将其字母的频率减一
            s_cnt[ord(s[i+len(p)-1])-ord('a')]+=1#本字符串会添加一个末尾字符，并将末尾字符的字母频率加一
            if s_cnt==p_cnt:#如果当前的p_cnt和s_cnt相等，res添加i
                res.append(i)
        return res#返回结果
