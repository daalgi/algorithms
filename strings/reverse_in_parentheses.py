"""
Write a function that reverses characters in (possibly nested) p
arentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".

Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and 
then "foobazrabblim".
"""
def reverse_in_parentheses(s: str):
    stack = []
    new_string = []
    for i in range(len(s)):
        new_string.append(s[i])
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            start = stack.pop()
            new_string[start+1:i] = new_string[start+1:i][::-1]
    return ''.join(x for x in new_string if x != '(' and x != ')')


if __name__ == '__main__':
    print('-' * 60)
    print('Reverse in parentheses')
    print('-' * 60)
    
    testcases = [
        ('(bar)', 'rab'),
        ('foo(bar)baz', 'foorabbaz'),
        ('foo(bar)baz(blim)', 'foorabbazmilb'),
        ('foo(bar)b(a)z(blim)', 'foorabbazmilb'),
        ('(b(li)m)', 'mlib'),
        ('(ba(li)m)', 'mliab'),
        ('(bak(li)m)', 'mlikab'),
        ('(b(li))m', 'libm'),
        ('foo(bar(baz))blim', 'foobazrabblim'),
        ('', '')
    ]

    for s, solution in testcases:
        res = reverse_in_parentheses(s)
        print(f'Reverse: {s} --> {res}')
        if solution is not None:
            print(f'Test: {"OK" if res == solution else "NOT OK"}\n')
        else:
            print()