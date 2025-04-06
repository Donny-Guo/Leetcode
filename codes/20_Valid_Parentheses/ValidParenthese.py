class Solution:
    def isValid(self, s: str) -> bool:
        # 1. set up char lists
        open_list = ['(','[','{']
        close_list = [')',']', '}']
        dict1 = dict(zip(open_list,close_list))

        # 2. create a stack
        stack = []

        # 3. for loop
        for c in s:
            if c in open_list:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pop_char = stack.pop()
                if dict1[pop_char] != c:
                    return False
        return len(stack) == 0