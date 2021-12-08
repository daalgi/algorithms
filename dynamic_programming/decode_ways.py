"""
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into 
numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped 
then mapped back into letters using the reverse of the 
mapping above (there may be multiple ways). 

For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot 
be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number 
of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), 
"VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number 
starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", 
neither of which start with 0.
Hence, there are no valid ways to decode this since all digits 
need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the 
leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


def bf_recursion(s: str) -> int:
    # Brute force - recursion
    # Time complexity: O(2^n)
    # Space complexity: O(n)

    # First definte the size of the string to be used 
    # in the recursive function
    size = len(s)
    
    def recursion(s: str, i: int) -> int:
        # Recursive function

        # Base cases
        if i == size:
            # when the pointer reaches the end of the string,
            # return 1, as one solution has been obtained
            return 1
        if s[i] == "0":
            # If the current digit is a zero, invalid solution
            return 0

        # Current count        
        # Move the pointer one digit forward
        count = recursion(s, i + 1)
        
        # If the current and the following digits
        # form a number more than 9 and less than 27, 
        # move the pointer two digits forward
        if i < size - 1:
            # if there are enough digits left,
            # check if the two-digits number is 9 < x < 27
            two_digits_valid_num = (
                s[i] == "1" 
                or (s[i] == "2" and s[i+1] < "7")
            )
            if two_digits_valid_num:
                count += recursion(s, i + 2)
                    
        return count

    # Edge cases
    if size == 0 or s[0] == "0":
        return 0

    # Check invalid 0s ("10" and "20" are the only valid 0s)
    for i in range(1, size):
        if s[i] == "0" and s[i - 1] > "2":
            return 0
    
    # Call the recursive function
    return recursion(s, 0)           
            

def dp_recursion(s: str) -> int:
    
    
    size = len(s)

    # Use memoization to store computed results and avoid
    # repeated work
    memo = [0] * size

    def recursion(s: str, i: int) -> int:
        # Recursive function

        # Base cases
        if i == size:
            # when the pointer reaches the end of the string,
            # return 1, as one solution has been obtained
            return 1
        if s[i] == "0":
            # If the current digit is a zero, invalid solution
            return 0

        # Check if the computation has been already done
        if memo[i]:
            return memo[i]

        # Current count        
        # Move the pointer one digit forward
        count = recursion(s, i + 1)
        
        # If the current and the following digits
        # form a number more than 9 and less than 27, 
        # move the pointer two digits forward
        if i < size - 1:
            # if there are enough digits left,
            # check if the two-digits number is 9 < x < 27
            two_digits_valid_num = (
                s[i] == "1" 
                or (s[i] == "2" and s[i+1] < "7")
            )
            if two_digits_valid_num:
                count += recursion(s, i + 2)
        
        # Store the current computation
        memo[i] = count
        # Return the current count
        return count

    if size == 0 or s[0] == "0":
        return 0

    # Check invalid 0s ("10" and "20" are the only valid 0s)
    for i in range(1, size):
        if s[i] == "0" and s[i - 1] > "2":
            return 0
            
    return recursion(s, 0)


def dp_iter(s: str) -> int:
    # TODO
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Decode ways")
    print("-" * 60)

    test_cases = [
        ("", 0),
        ("0", 0),
        ("08", 0),
        ("12", 2),
        ("226", 3),
        ("227", 2),
        ("886", 1),
        ("123123123", 27),
        ("2080", 0),
        ("2020202020", 1),
        ("2020202030", 0),
        ("260", 0),
        ("2611055", 2),
        ("261105517", 4),
        ("5517", 2),
        ("2611055971756562", 4),
    ]

    for s, solution in test_cases:

        result = bf_recursion(s)
        string = f" bf_recursion({s}) = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_recursion(s)
        string = f" dp_recursion({s}) = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
