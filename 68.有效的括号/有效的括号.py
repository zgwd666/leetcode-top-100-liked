#https://leetcode.cn/problems/valid-parentheses/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
本题使用栈解题。括号匹配是采用就近匹配原则，符合栈的先进后出的特点。

先用一个哈希表将左括号为key，对应的右括号为value进行存储。

初始化一个栈。

对s进行遍历，如果当前是左括号，就直接入栈；如果当前是右括号，则查看此时的栈顶是否为对应的左括号，是弹出栈顶元素，继续遍历，否就是不匹配返回。
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:#字符串中的字符为奇数个，肯定无法匹配
            return False
        hmap={'(':')','{':'}','[':']'}#创建对照哈希表
        stack=[]#初始化空栈
        for i in range(len(s)):#对字符串的每一个字符进行遍历
            if s[i] in hmap:#当前是左括号，入栈
                stack.append(s[i])
            else:#当前是右括号，需要查看栈顶元素匹配情况
                if stack and hmap[stack[-1]]==s[i]:#当栈非空且栈顶元素与当前元素想匹配时，栈顶元素弹出，继续遍历
                    stack.pop()
                else:#当栈为空或者栈顶元素与当前的元素并不匹配，断定不匹配，返回False 
                    return False 
        if stack:return False#遍历完成后，栈中还存在元素，证明没有完全匹配，返回False
        return True#当顺利遍历完成且栈为空，证明字符串中的元素均匹配，返回True
