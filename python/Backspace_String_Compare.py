class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        stack1 = []
        stack2 = []
        for i in range(max(len(s),len(t))):
            try:
                if s[i] == '#':
                    stack1.pop()
                else:
                    stack1.append(s[i])
            except IndexError:
                pass
            try:
                if t[i] == '#':
                    stack2.pop()
                else:
                    stack2.append(t[i])
            except IndexError:
                pass
        print(stack1,stack2)
        return ''.join(stack1) == ''.join(stack2) 

print(Solution().backspaceCompare("xywrrmp","xywrrmu#p"))