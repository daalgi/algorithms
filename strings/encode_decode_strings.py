"""
https://www.lintcode.com/problem/659/description

Description
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded 
back to the original list of strings.

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""
from typing import List


def encode0(strings: List[str]) -> str:
    # Time complexity: O(nk)
    # Space complexity: O(nk)
    return ":;".join(strings)


def decode0(s: str) -> List[str]:
    # Time complexity: O(nk)
    # Space complexity: O(nk)
    return s.split(":;")


def encode(strings: List[str]) -> str:
    # Time complexity: O(nk)
    # Space complexity: O(nk)
    res = []
    separator = ":;"
    # Loop over the strings
    for s in strings:
        # Loop over the characters of the current string
        for c in s:
            res.append(c)
        res.append(separator)
    # Return a string by joining the elements of the list,
    # but removing the last separator
    return "".join(res[:-1])


def decode(s: str) -> List[str]:
    # Time complexity: O(nk)
    # Space complexity: O(nk)
    separator = ":;"
    res = []
    i, n = 0, len(s)
    # List to keep track of the current word
    curr = []
    # Loop over the characters of the string `s`
    while i < n:
        if i < n - 1 and s[i : i + 2] == separator:
            # If a separator, add the current word to the
            # result list
            res.append("".join(curr))
            # Restart the current list
            curr = []
            # Move right two characters the ponter
            i += 2
        else:
            # Add the current character to the current word
            curr.append(s[i])
            i += 1

    # Add the last word
    res.append("".join(curr))

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Encode and decode strings")
    print("-" * 60)

    test_cases = [
        # (both input and solution)
        (["a"]),
        (["a", "b", ":", ";", "#"]),
        (["code", "love", ":", "you"]),
    ]

    for strings in test_cases:

        print(f"Strings: {strings}")

        s = encode0(strings)
        result = decode0(s)
        output = f"\t encode-decode0 = "
        output += " " * (10 - len(output))
        test_ok = strings == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        s = encode(strings)
        result = decode(s)
        output = f"\t  encode-decode = "
        output += " " * (10 - len(output))
        test_ok = strings == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print()
