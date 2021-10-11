"""
CRACKING THE CODING INTERVIEW
1.6. String compression.
Implement a method to perform basic string compression using
the counts of repeated characters. If the compressed string
would not become smaller than the original string, your method
should return the original string. You can assume the string
has only uppercase and lowercase letters (a-z).

Examples:
Input:  "aabcccccaaa"
Output: "a2b1c5a3"

Input:  "abc"
Output: "abc" (a1b1c1 is longer)
"""

def string_compression(s: str) -> str:
    # Edge case
    if s == "":
        return s
    
    # Length of the current string
    n = len(s)
    # List to store the compressed string
    res = []
    # Counter for the current character repetitions
    char_count = 1
    # Loop over the original string characters: O(n)
    for i in range(1, n):
        # Compare the current character with the previous one
        if s[i] != s[i-1]:
            # If they are not equal, register the previous 
            # character and the number of repetitions
            res.append(f'{s[i-1]}{char_count}')
            # Reinitialize current character count to 1
            char_count = 1
        else:
            # If they are equal, add one to the current
            # character count
            char_count += 1

    # Last character
    last_i = n -1
    if s[n-2] == s[last_i]:
        res.append(f'{s[last_i]}{char_count}')
    else:
        res.append(f'{s[last_i]}1')

    # List to string: O(n), worst case O(2n)
    res = ''.join(res)

    # If the compressed string is smaller, return it
    if len(res) < n:
        return res
    # Otherwise, return the original string
    return s


if __name__ == "__main__":
    print('-' * 60)
    print('String compression')
    print('-' * 60)

    test_cases = [
        ("", ""),
        ("aabcccccaaa", "a2b1c5a3"),
        ("abc", "abc"),
        ("aaaab", "a4b1"),
        ("aaaabb", "a4b2"),
        ("aaaabbc", "a4b2c1"),
        ("aaaabbcc", "a4b2c2"),
        ("aaaabbccdefghijkl", "aaaabbccdefghijkl"),
    ]
    
    for s, solution in test_cases:

        result = string_compression(s)
        string = f'compr({s}) = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')