"""
https://leetcode.com/problems/most-common-word/

Given a string paragraph and a string array of the banned 
words banned, return the most frequent word that is not 
banned. It is guaranteed there is at least one word that 
is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer 
should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", 
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most 
frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more 
because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', 
or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""
from typing import List


def sol1(paragraph: str, banned: List[str]) -> str:
    # Time complexity: O(m+n)
    # Space complexity: O(m)

    def split_into_words(p: str) -> List[str]:
        curr, res = [], []
        signs = set([" ", "!", "?", "'", ",", ":", "."])
        for c in p:
            if c in signs:
                if curr:
                    res.append("".join(curr))
                    curr = []
            else:
                curr.append(c.lower())

        # Add last word
        if curr:
            res.append("".join(curr))

        return res

    # Count of words
    count = dict()
    # Turn `banned` into a set
    banned = set(banned)
    # Most common variables
    max_freq, most_common = 0, ""
    # Loop over the words
    for word in split_into_words(paragraph):
        if word in banned:
            continue

        count[word] = count.get(word, 0) + 1
        if count[word] > max_freq:
            max_freq = count[word]
            most_common = word

    return most_common


def one_pass(paragraph: str, banned: List[str]) -> str:
    # Time complexity: O(m+n)
    # Space complexity: O(m)

    banned = set(banned)
    signs = set([" ", "!", "?", "'", ",", ";", ":", "."])
    i, n = 0, len(paragraph)
    curr = []
    count = {}
    max_freq, most_common = 0, ""
    while i < n:

        # Skip signs
        while i < n and paragraph[i] in signs:
            i += 1

        # Get next word
        while i < n and paragraph[i] not in signs:
            curr.append(paragraph[i].lower())
            i += 1

        if not curr:
            continue

        word = "".join(curr)
        curr = []

        # Skip banned words
        if word in banned:
            continue

        # Update count
        count[word] = count.get(word, 0) + 1
        if count[word] > max_freq:
            max_freq = count[word]
            most_common = word

    return most_common


if __name__ == "__main__":
    print("-" * 60)
    print("Most common word")
    print("-" * 60)

    test_cases = [
        # (paragraph, banned, solution)
        ("a.", [], "a"),
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
        ("Bob. hIt, baLl", ["bob", "hit"], "ball"),
    ]

    for paragraph, banned, solution in test_cases:

        print(f"Paragraph: {paragraph}\nBanned: {banned}")

        result = sol1(paragraph, [*banned])
        output = f"\t     sol1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_pass(paragraph, [*banned])
        output = f"\t one_pass = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
