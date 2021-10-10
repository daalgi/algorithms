"""
CRACKING THE CODING INTERVIEW
1.5. There are three types of edits that can be performed
on strings: insert a character, remove a character, or
replace a character. Given two strings, write a function 
to check if they are one edit (or zero edits) away.

Examples:
Input:  "pale", "ple"
Output: True

Input:  "pales", "pale"
Output: True

Input:  "pale", "bale"
Output: True

Input:  "pale", "bake"
Output: False
"""

def check_replace_one_character(s1: str, s2: str, size: int):
    """
    Assumptions
    -----------
    len(s1) = len(s2) = size
    """
    # Variable to keep track of whether
    # one different character was found
    one_diff_found = False
    # Loop over the indices of the strings
    # (s1 and s2 have the same length = `size`)
    for i in range(size):
        if s1[i] != s2[i]:
            # If differnt characters, check if
            # it's the first time
            if one_diff_found:
                # If not the first time,
                # both strings are not "one away"
                return False
            one_diff_found = True
    # If passed the loop checks, both strings
    # are "one away"
    return True

def check_insert_one_character(s1: str, s2: str, size1: int, size2: int):
    """
    Assumptions
    -----------
    size1 > size2
    """
    # Variable to keep track of whether
    # one different character was found
    one_diff_found = False
    # Pointer for the short string (s2)
    j = 0
    # Loop over the indices of the long string (s1)
    for i in range(size1):
        if j == size2 or s1[i] != s2[j]:
            # If differnt characters, check if
            # it's the first time
            if one_diff_found:
                # If not the first time,
                # both strings are not "one away"
                return False
            one_diff_found = True
            # Don't update the pointer of the short string
            # to check if the next character in the
            # long string is equal to the current in the short
        else:
            # If equal characters, update the pointer
            j += 1
    # If passed the loop checks, both strings
    # are "one away"
    return True

def two_pointers(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m == n:
        return check_replace_one_character(s1, s2, m)        
    elif m == n + 1:
        return check_insert_one_character(s1, s2, m, n)
    elif n == m + 1:
        return check_insert_one_character(s2, s1, n, m)
    return False


if __name__ == "__main__":
    print('-' * 60)
    print('One away')
    print('-' * 60)

    test_cases = [
        ("ab", "a", True),
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("cactus", "cact", False),
        ("cactus", "mactu", False),
        ("mactu", "cactus", False),
        ("cactus", "cactuh", True),
        ("nactus", "cactus", True),
    ]
    
    for s1, s2, solution in test_cases:

        result = two_pointers(s1, s2)
        string = f'2pointers{s1, s2} = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')