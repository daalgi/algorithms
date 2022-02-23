"""
https://leetcode.com/problems/repeated-substring-pattern/

Given a string s, check if it can be constructed by 
taking a substring of it and appending multiple copies 
of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or 
the substring "abcabc" twice.

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""


def brute_force(s: str) -> int:
    # Time complexity: O(n sqrt(n))
    # Space complexity: O(sqrt(n))
    # Check all posible divisors of length of `s`,
    # replicate them and compare them with the
    # original string.
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return True
    return False


def rotated(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: if we have a periodic string,
    # then we can ccheck if the string is equal to
    # some rotation of itself, and if it is,
    # we know that the string is periodic.
    # Checking `s in (s + s)[1:-1]` basically checks
    # if the string is present in a rotation of itself
    # for all values of R such that 0 < R < len(s)
    """
    Example 2 (True)
                  s = xyxy
    dup = (s+s)[1:] =  yxyxyxy
    s in dup = xyxy in yxyxyxy
                        ----      --> TRUE
    Example 2 (False)
                  s =  xyxyz
    dup = (s+s)[1:] =   yxyzxyxyz
    s in dup = xyxyz in yxyzxyxyz
                         --F--F   --> FALSE
    """
    return s in (s + s)[1:-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Repeated substring pattern")
    print("-" * 60)

    test_cases = [
        # (s, solution)
        ("a", False),
        ("aa", True),
        ("aabab", False),
        ("aabaab", True),
        ("aabcaaaabcaaaabcaa", True),
        ("aabcaaaabcaaaabca", False),
    ]

    for s, solution in test_cases:

        print("String", s)

        result = brute_force(s)
        output = f"   brute_force = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = rotated(s)
        output = f"       rotated = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
