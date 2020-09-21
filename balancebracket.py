# Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
# Examples:
# Input : {[]{()}}
# Output : Balanced

# Input : [{}{}(]
# Output : Unbalanced

def check_balance(s):
    stack = [];
    for char in s:
        if(char in ['{','(','[']):
            stack.append(char)
        else:
            if(not stack):
                return 'Unbalanced';
            if((char == ']' and stack[-1] != '[' )or(char == '}' and stack[-1] != '{' )or (char == ')' and stack[-1] != '(' )):
                return 'Unbalanced';
            stack.pop()

    return len(stack) == 0

if(check_balance("([]){}[]")):
    print('balance')
print(check_balance("[{}{}(]"));