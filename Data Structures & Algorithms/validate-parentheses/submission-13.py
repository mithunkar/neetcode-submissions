class Solution:
    def isValid(self, s: str) -> bool:
        
        close = {   ')': '(',
                    '}': '{',
                    ']': '['
                }
        
        stack = []

        for char in s:
            if char in close:
                if stack and stack[-1] == close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
