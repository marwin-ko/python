# Core code was taken from (https://favtutor.com/blogs/valid-parentheses) and then modified to control which brackets to search for.

def has_balanced_brackets(sequence, round_brackets=False, curly_brackets=False, square_brackets=False):
    '''
    Function to pair if sequence contains valid parenthesis
    :param sequence: Sequence of brackets
    :return: True is sequence is valid else False
    '''
    if (round_brackets is False) and (curly_brackets is False) and (square_brackets is False):
        raise Exception('Must explicitly set parenthetical (e.g. parenthesis and/or brackets) to True.')
    
    brackets = []
    # parenthesis ()
    if round_brackets:
        brackets.append(('(', ')'))
    # curly braces {}
    if curly_brackets:
        brackets.append(('{', '}'))
    # thee "bracket"
    if square_brackets:
        brackets.append(('[', ']'))
    
    opening = set()
    closing = set()
    pair = {}
    for start_bracket, end_bracket in brackets:
        opening.add(start_bracket)
        closing.add(end_bracket)
        pair[end_bracket] = start_bracket
    
    stack = []
    for i in sequence :
        if i in opening :
            stack.append(i)
        if i in closing :
            if not stack :
                return False
            elif stack.pop() != pair[i]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False
