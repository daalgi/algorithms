"""
CRACKING THE CODING INTERVIEW
1.1. Implement an algorithm to determine if a string has all unique characters.

What if you cannot use additional data structures?

Example:
Input: "abcd"
Output: True

Example:
Input: "abcda"
Output: False
"""

def hashset(string: str) -> bool:
    # Determine if all the characters are unique
    # using an additional data structure: hashset
    # Time complexity: O(n)
    # Space complexity: O(c), 
    #   where c is the number of different characters
    s = set()
    for c in string:
        if c in s:
            # Repeated character, 
            # not unique characters
            return False
        s.add(c)
    
    # Unique characters
    return True

def brute_force(string: str) -> bool:
    # Determine if all the characters are unique
    # not using an additional data structure: hashset
    # Time complexity: O(n2)
    # Space complexity: O(1)
    n = len(string)
    for i in range(n-1):
        for j in range(i+1, n):
            if string[i] == string[j]:
                # Repeated character, 
                # not unique characters
                return False
    # Unique characters
    return True


if __name__ == "__main__":
    print('-' * 60)
    print('Loop detection in linked list')
    print('-' * 60)

    test_cases = [
        #(vals, loop_index, result)
        # `loop_index = -1` means that there's no loop
        ("abcd", True),
        ("abcda", False),
        ("qwerasdfzxcvpoiuñlkj-.,m", True),
    ]
    
    for s, solution in test_cases:

        result = hashset(s)
        string = f' hashset({s}) = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = brute_force(s)
        string = f'  bforce({s}) = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()