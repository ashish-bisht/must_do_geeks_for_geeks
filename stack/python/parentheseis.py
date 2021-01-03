def valid_parentheses(string):
    stack = []

    brackets = {"(": ")", "{": "}", "[": "]"}

    for ch in string:
        if ch not in brackets:
            if not stack:
                return False
            cur_bracket = stack.pop()
            if not brackets[cur_bracket] == ch:
                return False
        else:
            stack.append(ch)
    return not stack


print(valid_parentheses("()[]{}"))

print(valid_parentheses("()[]{"))

print(valid_parentheses("})"))
