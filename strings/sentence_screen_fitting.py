"""
https://leetcode.com/problems/sentence-screen-fitting/

Given a rows x cols screen and a sentence represented 
as a list of strings, return the number of times the 
given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, 
and a word cannot be split into two lines. A single space 
must separate two consecutive words in a line.

Example 1:
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Example 2:
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

Example 3:
Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.

Constraints:
1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 10^4
"""
from typing import List


def brute_force(sentence: List[str], rows: int, cols: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Check if each word fits in a line
    if any(len(w) > cols for w in sentence):
        return 0

    last_word = len(sentence) - 1
    r = c = i = count = 0
    while r < rows:

        word = sentence[i]

        # Add the current `word`
        if c + len(word) <= cols:
            # It fits in the current row `r`
            c += len(word) + 1
        else:
            # It doesn't fit in the current row `r`,
            # so go to the next one
            r += 1
            if r == rows:
                return count
            c = len(word) + 1

        # Check if we've reached the end of the line
        if c >= cols:
            r += 1
            c = 0

        # Update word pointer
        if i == last_word:
            i = 0
            count += 1
        else:
            i += 1

    return count


def efficient(sentence: List[str], rows: int, cols: int) -> int:
    # Time complexity: O(rows * n)
    # Space complexity: O(n)

    # Strategy: loop over the rows and look, and for each row
    # find where the last col falls within the sentence.
    # Once the whole sentence has been covered, the pointer
    # will accumulate numbers characters (pointer > sentence_chars),
    # and we can keep on checking where the last col falls
    # by means of modulo operations `pointer % num_chars`.
    # At the end, we can find how many times the sentence
    # can be fitted by performing an integer division
    # `pointer // sentence_chars`.

    # Build a string containing all the words of `sentence`
    # separated by a space. Add a space at the end to account
    # for the concatenation with the start of the sentence.
    s = " ".join(sentence) + " "
    sentence_chars = len(s)

    # Loop over the rows
    pointer = 0
    for _ in range(rows):
        pointer += cols - 1

        if s[pointer % sentence_chars] == " ":
            # Case 1: pointer at the end of the line falls exactly
            # on a space
            pointer += 1
        elif s[(pointer + 1) % sentence_chars] == " ":
            # Case 2: pointer at the end of the line coincides
            # with the last letter of a word (next is a space)
            pointer += 2
        else:
            # Case 3: pointer at the end of the line falls in
            # the middle of a word, so we have to move the pointer
            # to the start of that word
            while (
                pointer > 0 
                and s[(pointer - 1) % sentence_chars] != " "
            ):
                pointer -= 1

    return pointer // sentence_chars


def efficient2(sentence: List[str], rows: int, cols: int) -> int:
    # Time complexity: O()
    # Space complexity: O(n)

    s = " ".join(sentence) + " "
    pointer, size = 0, len(s)
    offsets = {i: cols + 1 - len(s[: i + 1].split(" ")[-1]) for i in range(size)}
    for _ in range(rows):
        pointer += offsets[(pointer + cols) % size]

    return pointer // size


if __name__ == "__main__":
    print("-" * 60)
    print("Sentence screen fitting")
    print("-" * 60)

    test_cases = [
        # (sentence, rows, cols, solution)
        (["hello", "world"], 2, 8, 1),
        (["hello", "world"], 1, 11, 1),
        (["hello", "world"], 1, 12, 1),
        (["hello", "leetcode"], 1, 10, 0),
        (["f", "p", "a"], 8, 7, 10),
        (["a", "bcd", "e"], 3, 6, 2),
        (["i", "had", "apple", "pie"], 4, 5, 1),
        (["a"], 20000, 10000, 100000000),
    ]

    for i, (sentence, rows, cols, solution) in enumerate(test_cases):

        print("Sentence:", sentence)
        print("rows, cols:", (rows, cols))

        if i < len(test_cases) - 1:
            result = brute_force(sentence, rows, cols)
            output = f"     brute_force = "
            test_ok = solution == result
            output += str(result)
            output += " " * (50 - len(output))
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = efficient(sentence, rows, cols)
        output = f"       efficient = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = efficient2(sentence, rows, cols)
        output = f"      efficient2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
