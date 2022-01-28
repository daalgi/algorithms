"""
https://leetcode.com/problems/minimum-window-subsequence/

Given strings s1 and s2, return the minimum contiguous 
substring part of s1, so that s2 is a subsequence 
of the part.

If there is no such window in s1 that covers all 
characters in s2, return the empty string "". 
If there are multiple such minimum-length windows, 
return the one with the left-most starting index.

Example 1:
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" 
which has the same length.
"deb" is not a smaller window because the elements 
of s2 in the window must occur in order.

Example 2:
Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""

Constraints:
1 <= s1.length <= 2 * 10^4
1 <= s2.length <= 100
s1 and s2 consist of lowercase English letters.
"""


def two_pointers(s1: str, s2: str) -> str:
    # Time complexity: O(mn)
    # Space complexity: O(1)

    m, n = len(s1), len(s2)
    if m < n or not m or not n:
        return ""

    # Minimum contiguous subsequence (mcs)
    mcs_len, mcs_start = float("inf"), None
    # Loop over the chars of `s1`
    for i in range(m):

        # If the current char at `s1` doesn't match the first
        # char at `s2`, check next char
        if s1[i] != s2[0]:
            continue

        # Use two pointers to scan the rest of the chars
        index_s1, index_s2 = i, 0
        while index_s1 < m and index_s2 < n:
            if s1[index_s1] == s2[index_s2]:
                index_s2 += 1
            index_s1 += 1

        # If `index_s2` reached the end of the string `s2`
        if index_s2 == n:
            curr_len = index_s1 - i
            if curr_len < mcs_len:
                mcs_len = curr_len
                mcs_start = i

    if mcs_start is not None:
        return s1[mcs_start : mcs_start + mcs_len]
    return ""


def two_pointers_opt(s1: str, s2: str) -> str:
    # Time complexity: O(mn)
    # Space complexity: O(1)
    # Strategy:
    # Scan both strings until the first subsequence match.
    # Move the pointer backwards to find the minimum window.
    # Repeat until reaching the end of the string `s1`

    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 < len_s2 or not len_s1 or not len_s2:
        return ""

    mcs_len, mcs_start = float("inf"), None
    index_s1 = index_s2 = 0
    while index_s1 < len_s1:
        if s1[index_s1] == s2[index_s2]:
            # If the current chars of both strings match,
            # move the pointer of `s2`
            index_s2 += 1

            if index_s2 == len_s2:
                # If reached the end of `s2`,
                # save the `end` index of the substring
                end = index_s1

                # find the MCS, from right to left
                index_s2 -= 1
                while index_s2 >= 0:
                    if s1[index_s1] == s2[index_s2]:
                        index_s2 -= 1
                    index_s1 -= 1

                # Lenght of the current window
                curr_len = end - index_s1
                if curr_len < mcs_len:
                    mcs_len = curr_len
                    mcs_start = index_s1 + 1

        index_s1 += 1

    if mcs_start is not None:
        return s1[mcs_start : mcs_start + mcs_len]
    return ""


def dp_iter(s1: str, s2: str) -> str:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    len_s1, len_s2 = len(s1), len(s2)

    # Table that stores the starting index `k` in `s1`
    # that contains the subsequence s2[0:j] for each
    # substring s1[0:i], i.e.:
    #         b b a c b a d c
    #       0 1 2 3 4 5 6 7 8
    #     a 0 0 0 2 2 2 5 5 5
    #     b 0 0 0 0 0 2 2 2 2
    #     c 0 0 0 0 0 0 0 0 2
    #     Checking the last row, at index `j = 8`
    #     we find the shortest (unique in this case)
    #     substring in `s1` that contains the
    #     subsequence `s2`, which starts at index `2`
    #     --> return s1[2:8] = "acbadc"
    dp = [[-1] * (len_s1 + 1) for _ in range(len_s2 + 1)]

    # Initialize the first row (empty string)
    for j in range(len_s1 + 1):
        dp[0][j] = j

    # Loop over the rows (chars of `s2`)
    for i in range(1, len_s2 + 1):
        # Loop over the columns (chars of `s1`)
        for j in range(1, len_s1 + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    # Find the minimum window looping over the
    # cols of the last row of `dp`
    # print(dp[-1])
    mcs_len, mcs_start = float("inf"), None
    for j in range(len_s1 + 1):
        if dp[-1][j] > -1:
            curr_len = j - dp[-1][j]
            if 0 < curr_len < mcs_len:
                mcs_len = curr_len
                mcs_start = dp[-1][j]

    if mcs_start is None:
        return ""
    return s1[mcs_start : mcs_start + mcs_len]


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum window subsequence")
    print("-" * 60)

    test_cases = [
        # (s1, s2, solution)
        ("abc", "hk", ""),
        ("abc", "abcd", ""),
        ("a", "a", "a"),
        ("bbacbdc", "abc", "acbdc"),
        ("abcdefghijk", "dg", "defg"),
        ("abcdefghijk", "hk", "hijk"),
        ("abcdefghijk", "hkj", ""),
        ("asdlkfjhdsfmnbzxcvkljhqwerhgqweripo", "u", ""),
        (
            "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeesssaaaa",
            "fffessa",
            "fffeeeeeeesssa",
        ),
        (
            "pcaimomtmveadexvauerxryuisraxixqbgnbwrjqidfdcnrlljirsioxlholkytimqtzubqommizbdxaunnydfylyerxmzatcedymqxgaochxnfeplecowiuwrqsaxjhqjfxpotrnytfteghimxlalhjclvnszzudxigaiozwduuudufxiupehkbumnlcempydugrsnqwfutycpfctlshyjlelszhtkaowhiweisjejisslhwcbwjdabmfnievmufkuvalpdufglzzwtvgqthbgzqqqxxzklhxvwygmrpoqlbwgopjnfymtcgxvtfqhztffdch",
            "olbmyncpiu",
            "olkytimqtzubqommizbdxaunnydfylyerxmzatcedymqxgaochxnfeplecowiuwrqsaxjhqjfxpotrnytfteghimxlalhjclvnszzu",
        ),
        (
            "spbmtkwqpftyahhnughzxscpavtqymtbanjyybdlhbphfrycpytsgzoeunvxaxuwbmecthomrjgmbvaoyjxxefmtxaxgwswdjdjlkpzsuirbujvhesfzdklgkulkmfnlofytaszwtxacnffvszmobxwmlhaxporskwzrvgmdpneggxqidqsdgvcprcnkdrxtsktibilbtggpazwuddhrgsmaspelglhausmfnyksdfyrwtpftrgtw",
            "avymssugau",
            "axgwswdjdjlkpzsuirbujvhesfzdklgkulkmfnlofytaszwtxacnffvszmobxwmlhaxporskwzrvgmdpneggxqidqsdgvcprcnkdrxtsktibilbtggpazwuddhrgsmaspelglhau",
        ),
    ]

    for s1, s2, solution in test_cases:

        print("String 1:", s1)
        print("String 2:", s2)

        result = two_pointers(s1, s2)
        output = f"     two_pointers = "
        test_ok = solution == result
        output += result[:25] + "..." if len(result) > 30 else result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = two_pointers_opt(s1, s2)
        output = f" two_pointers_opt = "
        test_ok = solution == result
        output += result[:25] + "..." if len(result) > 30 else result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter(s1, s2)
        output = f"          dp_iter = "
        test_ok = solution == result
        output += result[:25] + "..." if len(result) > 30 else result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
