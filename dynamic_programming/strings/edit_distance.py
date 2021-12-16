"""
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of 
operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.


"EDIT DISTANCE" ALGORITHM APPLICATIONS:
- Spelling correction in NLP: 
    Edit distance operations: insert, delete, substitute.
- Find similarity in DNA sequences.    
"""
from functools import lru_cache


def brute_force(word1: str, word2: str) -> int:
    # Time complexity: O(3^(m+n))
    # 3 choices (3 operations) per character.
    # Space complexity: O(min(m, n))

    def rec(i: int, j: int) -> int:
        # Recursive function that compares char by char.

        # Base cases:
        if i == m:
            # Only `word1` reached the end, so we need
            # to add characters to `word2`
            return n - j
        if j == n:
            # Only `word2` reached the end, so we need
            # to add characters to `word1`
            return m - i

        if word1[i] == word2[j]:
            # If equal characters, no need edit operations
            # for the current pointers
            return rec(i + 1, j + 1)

        # If not equal
        # Replace character operation
        replace = rec(i + 1, j + 1)
        # Remove character operation
        remove = rec(i + 1, j)
        # Insert character operation
        insert = rec(i, j + 1)
        # Minimum number of operations
        return 1 + min(replace, remove, insert)

    # Length of the words
    m, n = len(word1), len(word2)

    # Call the recursive function, starting with
    # the pointers at the first character of each string
    return rec(0, 0)


def dp_memoization(word1: str, word2: str) -> int:
    # Dynamic programming - Memoization (python built-in cache)
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)

    @lru_cache(maxsize=None)
    def rec(i: int, j: int) -> int:
        # Recursive function that compares char by char.

        # Base cases:
        if i == m:
            # Only `word1` reached the end, so we need
            # to add characters to `word2`
            return n - j
        if j == n:
            # Only `word2` reached the end, so we need
            # to add characters to `word1`
            return m - i

        if word1[i] == word2[j]:
            # If equal characters, no need edit operations
            # for the current pointers
            return rec(i + 1, j + 1)

        # If not equal
        # Replace character operation
        replace = rec(i + 1, j + 1)
        # Remove character operation
        remove = rec(i + 1, j)
        # Insert character operation
        insert = rec(i, j + 1)
        # Minimum number of operations
        return 1 + min(replace, remove, insert)

    # Length of the words
    m, n = len(word1), len(word2)

    # Call the recursive function, starting with
    # the pointers at the first character of each string
    return rec(0, 0)


def dp_tabulation(word1: str, word2: str) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    #   Can be optimized to O(m+n)

    # Size of the strings
    m, n = len(word1), len(word2)

    # Matrix to store the number of operations needed for
    # word1[:i] to become word2[:j]
    # The length of the matrix must be (m+1)x(n+1)
    dp = [[0] * (n + 1) for r in range(m + 1)]

    # Loop over the characters of `word1`
    for i in range(m + 1):
        # Loop over the characters of `word2`
        for j in range(n + 1):
            if i == 0:
                # If the first string is empty, the only option is to
                # insert all characters of the second string,
                # so for each column of row0 we'll have num_operations = num_char
                # Row = 0 --> dp = [0, 1, 2, ..., n] (word2 -> n)
                dp[i][j] = j

            elif j == 0:
                # If the second string is empty, the only option is to
                # remove all characters of the second string,
                # so for each row of col0 we'll have num_operations = num_char
                # Col = 0 --> dp = [0, 1, 2, ..., m] (word1 -> m)
                dp[i][j] = i

            elif word1[i - 1] == word2[j - 1]:
                # If equal characters, no operation needed
                # ("move" diagonally not adding 1)
                dp[i][j] = dp[i - 1][j - 1]

            else:
                # If the current characters are not equal,
                # consider all the possible operations
                # 1 (operation) + min(replace, remove, insert)
                dp[i][j] = 1 + min(
                    # Replace operation ("moving" diagonally)
                    dp[i - 1][j - 1],
                    # Remove operation ("moving" up)
                    dp[i - 1][j],
                    # Insert operation ("moving" left)
                    dp[i][j - 1],
                )

    return dp[m][n]


if __name__ == "__main__":

    print("-" * 60)
    print("Edit distance")
    print("-" * 60)

    test_cases = [
        ("sunday", "saturday", 3),
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "a", 1),
        ("asdasdnuasdfasdf", "aqwefqpowierngvqasdfasdfwervasdkllsavsi", 29),
        ("asdfasdfasdfasdfpoiu", "asdfpoiuasdfpoiu", 8),
        ("abcde", "ace", 2),
        ("abcde", "hfg", 5),
        ("abc", "abc", 0),
        ("cba", "abc", 2),
        ("abc", "abcdef", 3),
        ("aabbcc", "abc", 3),
        ("abcdaf", "acbcf", 3),
        ("sea", "eat", 2),
        ("prosperity", "properties", 4),
    ]

    for s1, s2, solution in test_cases:

        print("String 1:", s1)
        print("String 2:", s2)

        if len(s1) < 13:
            result = brute_force(s1, s2)
            string = f"   brute_force = "
            string += " " * (20 - len(string))
            string += str(result)
            string += " " * (50 - len(string))
            test_ok = solution == result
            string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(string)

        result = dp_memoization(s1, s2)
        string = f"dp_memoization = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation(s1, s2)
        string = f" dp_tabulation = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print()
