class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        openBrackets = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                openBrackets.append(ch)
            else:
                if not openBrackets:
                    return False
                top = openBrackets.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False
        return not openBrackets