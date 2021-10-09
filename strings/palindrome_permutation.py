"""
CRACKING THE CODING INTERVIEW
1.4. Given a string, write a function to check if it is
a permutatio9n of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutaiton is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Example:
Input:  "Tact Coa"
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

from collections import defaultdict


def hashtable(s: str) -> bool:
    # Count the frequencies of the characters.
    # Assumption 1: ignore spaces.
    # Assumption 2: not case sensitive.
    # If the length of the string is even,
    # the frequency of all the characters must be even.
    # If the length of the string is odd,
    # the frequency of all the characters but one
    # must be even.
    
    # Keep track of the valid characters (ignoring spaces)
    n = 0

    # Frequencies hashtable
    freq = defaultdict(int)

    # Loop over the characters to find frequencies
    # O(n)
    for c in s:
        # Add non-space characters
        if c != " ":
            freq[c.lower()] += 1
            n += 1
    
    # Variable to track if there's an allowed odd
    # frequency of characters:
    # `n & 1` returns 1 if it's odd, 0 otherwise
    allowed_odd = True if n & 1 else False
    
    # Loop over the items of the frequencies hashtable
    # O(c), where c is the length of the character set
    for character, frequency in freq.items():

        if frequency & 1:
            # If the frequency is an odd number
            if not allowed_odd:
                # If odd number is not allowed
                # no possible palindrome permutations
                return False
            allowed_odd = False

    # If all frequencies passed the previous checks,
    # there are palindrome permutations
    return True

def hashtable_optimization(s: str) -> bool:
    # Same as before the `hashtable` method, 
    # but instead of saving the count in the hashtable,
    # we can save if the current count is odd (True)
    # or even (False), thus reducing the needed space
    # for the hashtable.

    n = 0
    freq = defaultdict(bool)
    for c in s:
        if c != " ":
            c_lower = c.lower()
            freq[c_lower] = not freq[c_lower]
            n += 1

    allowed_odd = True if n & 1 else False

    for character, odd_freq in freq.items():
        if odd_freq:
            if not allowed_odd:
                return False
            allowed_odd = False

    return True

def hashtable_optimization2(s: str) -> bool:
    # Same as before the `hashtable` method, 
    # but reducing the number of loops to one
    # (although it's not necessarily an optimization
    # in terms of speed, since each iteration will
    # perform more computations)
    
    count_odd = 0
    freq = defaultdict(int)
    for c in s:
        if c != " ":
            c_lower = c.lower()
            freq[c_lower] += 1

            # Current count of odds
            if freq[c_lower] & 1:
                # If it's odd, sum 1
                count_odd += 1
            else:
                # If it's even, subtract 1
                count_odd -= 1
    
    # For strings of even length, the number
    # of odd characters can be 0, 2, 4, etc.,
    # but we can only accept 0.
    # For string of odd length, the number
    # of odd characters can be 1, 3, 5, etc.,
    # but we can only accept 1.
    # Therefore, we don't even need to make a 
    # distinction between both cases for this problem.
    return count_odd <= 1


if __name__ == "__main__":
    print('-' * 60)
    print('Has a string any palindrome permutations?')
    print('-' * 60)

    test_cases = [
        ("ab", False),
        ("Tact Coa", True),
        ("tactcoapapa", True),
        ("tactcoapapac", False),
        ("abb a", True),
        ("ab b a c", True),
        ("abb acd", False),
    ]
    
    for s, solution in test_cases:

        result = hashtable(s)
        string = f'     hashtable({s}) = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = hashtable_optimization(s)
        string = f' hashtable_opt({s}) = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = hashtable_optimization2(s)
        string = f'hashtable_opt2({s}) = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()