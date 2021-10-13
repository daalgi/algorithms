"""
CRACKING THE CODING INTERVIEW
1.9. String rotation
Assume you have a method `isSubstring` which checks if one
word is a substring of another. Given two strings, `s1` and `s2`,
write code to check if `s2` is a rotation of `s1` using only one
call to `isSubstring`.

Examples:
Input:  "waterbottle", "erbottlewat"
Output: True
"""

def two_pointers(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    
    # If both string sizes are not equal or empty,
    # can't be a rotation
    if m != n or m == 0:
        return False

    # Two pointers, one for each string
    i, j = 0, 0
    # Loop over the characters of `s1`: O(m)
    while i < m:
        if s1[i] == s2[j]:
            # If both characters are equal,
            # check next character for both strings
            i += 1
            j += 1
        elif j == 0:
            # If characters are not equal and the pointer
            # of the second string is at the beginning,
            # check the next character in the first string
            i += 1
        elif j > 0:
            # If characters are not equal and the pointer
            # of the second string isn not at the beginning,
            # for next iteration check the current `s1` character 
            # and the first `s2`
            j = 0

    # After the first loop, if the strings are 
    # rotations of each other, the pointers must be
    # at the same characters during all iterations
    # of the next loop, so
    # continue comparing characters
    # from the beginning of `s1`: O(m) 
    i = 0
    while i < m and j < m:
        if s1[i] != s2[j]:
            # If the characters are not equal
            # they're not rotations
            return False
        
        # Update for next iteration to check
        # the following character in both strings
        i += 1
        j += 1
    
    # If the previous tests are passed,
    # both strings are rotations
    return True


def is_substring(s1: str, s2: str) -> bool:
    m = len(s1)
    if m == len(s2) and m > 0:
        # If the string `s2` is a substring
        # of two times `s1` (`s1 + s1`)
        # then is a rotation
        s1s1 = s1 + s1
        return s2 in s1s1
    
    # If not substring, is not a rotation
    return False


if __name__ == "__main__":
    print('-' * 60)
    print('String rotation')
    print('-' * 60)

    test_cases = [
        ("", "", False),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("aab", "baa", True),
        ("abab", "bbaa", False),
        ("abab", "bbaa", False),
        ("waterbottle", "erbottlewat", True),
    ]
    
    for s1, s2, solution in test_cases:

        result = two_pointers(s1, s2)
        string = f'two_pointers{s1, s2} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        result = is_substring(s1, s2)
        string = f'two_pointers{s1, s2} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()