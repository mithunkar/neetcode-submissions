class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]
        mirrored = {']':'[',
                    ')':'(',
                    '}':'{'
                    }

        for bracket in s:
            if bracket in mirrored:
                if len(stack) > 0 and stack[-1] == mirrored[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if len(stack) == 0 else False