"""
https://leetcode.com/problems/text-justification/

Given an array of strings words and a width maxWidth, 
format the text such that each line has exactly maxWidth 
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, 
pack as many words as you can in each line. Pad extra 
spaces ' ' when necessary so that each line has exactly 
maxWidth characters.

Extra spaces between words should be distributed as evenly 
as possible. If the number of spaces on a line does not 
divide evenly between words, the empty slots on the left 
will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified 
and no extra space is inserted between words.

Note:
- A word is defined as a character sequence consisting 
of non-space characters only.
- Each word's length is guaranteed to be greater than 0 
and not exceed maxWidth.
- The input array words contains at least one word.
 
Example 1:
Input: words = 
["This", "is", "an", "example", "of", "text", "justification."], 
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: 
words = ["What","must","be","acknowledgment","shall","be"], 
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " 
instead of "shall     be", because the last line must 
be left-justified instead of fully-justified.
Note that the second line is also left-justified becase 
it contains only one word.

Example 3:
Input: 
words = ["Science","is","what","we","understand","well",
"enough","to","explain","to","a","computer.","Art","is",
"everything","else","we","do"], 
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List


def greedy(words: List[str], max_width: int) -> List[str]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    lines = []
    word_i, n = 0, len(words)
    while word_i < n:

        # Fill the current `line` with words and spaces
        # until its length reaches `max_width`.
        # Mark the spaces with integers, i.e.
        # ["this", 1, "is", 1, "a"]
        chars, line = 0, []
        while word_i < n and chars <= max_width:
            line.append(words[word_i])
            line.append(1)
            chars += len(words[word_i]) + 1
            word_i += 1

        # Remove last space, i.e.
        # ["this", 1, "is", 1, "a", 1]
        line.pop()
        chars -= 1

        # If the number of characters `chars` is still
        # larger than `max_width`, remove the
        # last word and space
        if chars > max_width:
            # Remove last word
            chars -= len(line.pop())
            word_i -= 1
            # Remove the last space
            line.pop()
            chars -= 1

        line_size = len(line)
        if chars < max_width and word_i < n and line_size > 1:
            # If the number of characters `chars` is less
            # than `max_width` and is not the last word,
            # use the remaining characters
            # to increase the spaces from left to right

            # Pointer to space `i` (odd numbers)
            i = 1
            left_spaces = max_width - chars
            while left_spaces:
                line[i] += 1
                left_spaces -= 1
                i += 2
                # If the pointer `i` reaches the end
                # of `line`, start over from the first space
                if i >= line_size:
                    i = 1

        elif word_i == n or line_size == 1:
            # If it's the last word, or only one word
            # fits into `line`, add spaces to the right
            line.append(max_width - chars)

        # Add the current `line` to `lines` with the
        # corresponding spaces
        lines.append(
            "".join(
                line[i] if i & 1 == 0 else " " * line[i] 
                for i in range(len(line))
            )
        )

    return lines


def greedy2(words: List[str], max_width: int) -> List[str]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    res, cur, num_letters = [], [], 0
    for w in words:
        # Check if the current line `cur` fits in `max_width`
        if num_letters + len(w) + len(cur) > max_width:
            # If it doesn't fit
            # Round robin: extra spaces distribution
            for i in range(max_width - num_letters):
                cur[i % (len(cur) - 1 or 1)] += " "
            res.append("".join(cur))
            cur, num_letters = [], 0
        
        # Add current word `w`
        cur += [w]
        num_letters += len(w)

    return res + [" ".join(cur).ljust(max_width)]


if __name__ == "__main__":
    print("-" * 60)
    print("Text justification")
    print("-" * 60)

    test_cases = [
        # (words, max_width, solution)
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            ["This    is    an", "example  of text", "justification.  "],
        ),
        (
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            ["What   must   be", "acknowledgment  ", "shall be        "],
        ),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
        ),
    ]

    for words, max_width, solution in test_cases:

        words_str = str(words)
        if len(words_str) > 60:
            words_str = words_str[:55] + " ...]"
        print("Words:", words_str)
        print("Max width:", max_width)

        result = greedy(words, max_width)
        output = f"      greedy -> "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = greedy2(words, max_width)
        output = f"     greedy2 -> "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        for line in result:
            print(line)

        print()
