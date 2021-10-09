"""
CRACKING THE CODING INTERVIEW
1.2. Given two strings, write a method to decide if
one is a permutation of the other.

Example:
Input: "abcd", "dcab"
Output: True

Example:
Input: "ada", "qwer"
Output: False
"""
from collections import defaultdict

def hashtable(s1: str, s2) -> bool:
    # Count the frequency of each different character
    # in both strings and compare them.
    # If not equal frequencies, they're not permutations
    # of each other.
    # Using an additional data structure: hashtable
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(c), 
    #   where c is the number of different characters

    # If the length of both strings is not equal,
    # they can't be permutations of each other
    if len(s1) != len(s2):
        return False
    
    # Frequency hashtable
    freq = defaultdict(int)
    
    # Frequencies of the first string
    for c in s1:
        # Add frequency of the current character
        freq[c] += 1

    # Frequencies of the second string
    # to be subtracted in the `freq` table
    for c in s2:
        
        # If any frequency is equal to 0
        # before the subtraction of the current character
        # both strings are not permutations of each other
        if freq[c] == 0:
            return False

        # Subtract frequency for the current character
        freq[c] -= 1

    # Equal frequencies of characters,
    # so they are permutations of each other
    return True

def array(s1: str, s2) -> bool:
    # Count the frequency of each different character
    # in both strings and compare them.
    # If not equal frequencies, they're not permutations
    # of each other.
    # Using an additional data structure: array
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(c), 
    #   where c is the number of different characters

    # If the length of both strings is not equal,
    # they can't be permutations of each other
    if len(s1) != len(s2):
        return False
    
    # Frequency hashtable, 128 characters
    freq = [0] * 128
    
    # Frequencies of the first string
    for c in s1:
        # Add frequency of the current character
        freq[ord(c)] += 1

    # Frequencies of the second string
    # to be subtracted in the `freq` table
    for c in s2:
        
        # Current character index
        i = ord(c)

        # If any frequency is equal to 0
        # before the subtraction of the current character
        # both strings are not permutations of each other
        if freq[i] == 0:
            return False

        # Subtract frequency for the current character
        freq[i] -= 1

    # Equal frequencies of characters,
    # so they are permutations of each other
    return True

def sorting(s1: str, s2: str) -> bool:
    # Sort both arrays and compare them
    # character by character

    # If both strings length is not equal,
    # they can't be permutations of each other
    if len(s1) != len(s2):
        return False

    # Sort both arrays
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    # Return True if both sorted arrays are equal
    return s1 == s2


if __name__ == "__main__":
    print('-' * 60)
    print('Is permutation?')
    print('-' * 60)

    test_cases = [
        ("abcd", "dcba", True),
        ("abcda", "qwer", False),
        ("abcda", "dabca", True),
        ("abcda", "dabcaa", False),
        ("aaaaaaaaaaaabbb", "aabaaabaaaabaaa", True),
        ("qwerasdfzxcvpoiuñlkj-.,m", "fien", False),
    ]
    
    for s1, s2, solution in test_cases:

        result = hashtable(s1, s2)
        string = f'hashset{s1, s2} = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = array(s1, s2)
        string = f'  array{s1, s2} = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = sorting(s1, s2)
        string = f'sorting{s1, s2} = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()