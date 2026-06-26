class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack==[]:
                    return False
                if stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
        