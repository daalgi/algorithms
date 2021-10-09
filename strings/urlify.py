"""
CRACKING THE CODING INTERVIEW
1.3. Write a method to replace all spaces in a string
with "%20". You may assume that the string has sufficient
space at the end to hold the additional characters, and that
you are given the "true" length of the string.

Example:
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

"""

def two_pointers(s: str, true_length: int) -> bool:
    # Since the string has the needed additional space
    # at the end, we can move the characters starting
    # from the end of the string without worrying
    # about what  we're overwriting.
    # Time complexity: O(3n) = O(n)

    # Two pointers
    # Slow pointer at the end of the string
    slow = len(s) - 1
    # Fast pointer at the end of the true_length of the string
    fast = true_length - 1
    # Strings in python are immutable, so we can
    # convert the string into a list
    # O(n)
    s = list(s)
    # Loop over the characters
    # O(n)
    while fast > -1:
        if s[fast] != " ":
            s[slow] = s[fast]
            fast -= 1
            slow -= 1
        else:
            s[slow] = "0"
            s[slow - 1] = "2"
            s[slow - 2] = "%"
            fast -= 1
            slow -= 3
    # Join the elements of the list
    # to form a string again
    # O(n)
    return ''.join(s)


if __name__ == "__main__":
    print('-' * 60)
    print('URLify string (substitute space for "%20")')
    print('-' * 60)

    test_cases = [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        (" qwer qwer qwer      ", 15, "%20qwer%20qwer%20qwer"),
    ]
    
    for s, true_length, solution in test_cases:

        result = two_pointers(s, true_length)
        string = f'2pointers{s, true_length} = '
        string += ' ' * (55 - len(string))
        string += str(result)
        string += ' ' * (40 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')