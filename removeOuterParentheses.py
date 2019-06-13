

def removeOuterParentheses(S):
    START_BRACKET = '('
    END_BRACKET = ')'
    bracket_stack = []
    result = ''
    bracket_nesting_counter = 0
    for index, character in enumerate(S):
        if character == START_BRACKET:
            bracket_stack.append(character)
            bracket_nesting_counter += 1
            if bracket_nesting_counter > 1:
                result += character

        elif character == END_BRACKET:
            bracket_stack.pop()
            bracket_nesting_counter -= 1
            if bracket_nesting_counter > 0:
                result += character

        
        
        


    return result

if __name__ == "__main__":
    string = "(()())(())(()(()))"
    print('{} => {}'.format(string, removeOuterParentheses(string)))

    string = "()()"
    print('{} => {}'.format(string, removeOuterParentheses(string)))


    string = ""
    print('{} => {}'.format(string, removeOuterParentheses(string)))

    string = "(()())(())"
    print('{} => {}'.format(string, removeOuterParentheses(string)))

    string = "(()())(())(()(()))"
    print('{} => {}'.format(string, removeOuterParentheses(string)))