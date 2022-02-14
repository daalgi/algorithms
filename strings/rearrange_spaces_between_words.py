"""
https://leetcode.com/problems/rearrange-spaces-between-words/submissions/

You are given a string text of words that are 
placed among some number of spaces. Each word 
consists of one or more lowercase English letters 
and are separated by at least one space. It's 
guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal 
number of spaces between every pair of adjacent 
words and that number is maximized. If you cannot 
redistribute all the spaces equally, place the 
extra spaces at the end, meaning the returned string 
should be the same length as text.

Return the string after rearranging the spaces.

Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. 
We can evenly divide the 9 spaces between the words: 
9 / (4-1) = 3 spaces.

Example 2:
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 
7 / (3-1) = 3 spaces plus 1 extra space. We place this 
extra space at the end of the string.
 
Constraints:
1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.
"""


def count_spaces(text: str) -> str:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Count spaces and split words
    spaces = sum(c == " " for c in text)
    words = text.split()

    # Edge case: if there's only one word,
    # all the spaces at the end
    num_words = len(words)
    if num_words == 1:
        return words[0] + " " * spaces

    # Build a list to store the new text
    # [word1, spaces_in_between, word2, spaces_in_between, ...]
    new_text = []
    num_spaces_in_between = spaces // (num_words - 1)
    spaces_in_between = " " * num_spaces_in_between
    for w in words:
        new_text.append(w)
        new_text.append(spaces_in_between)

    # Remove the last space
    new_text.pop()

    # Check if there's any space left
    left = spaces - num_spaces_in_between * (num_words - 1)
    if left:
        new_text.append(" " * left)

    return "".join(new_text)


if __name__ == "__main__":
    print("-" * 60)
    print("Rearrange spaces between words")
    print("-" * 60)

    test_cases = [
        # (text, solution)
        ("a b c ", "a b c "),
        ("  this   is  a sentence ", "this   is   a   sentence"),
        (" practice     makes   perfect    ", "practice      makes      perfect "),
        (" camion ", "camion  "),
        (" catorce vidas son    dos gatos ", "catorce  vidas  son  dos  gatos "),
    ]

    for text, solution in test_cases:

        text_str = str(text)
        if len(text_str) > 60:
            text_str = text_str[:55] + " ...]"
        print(f'Text:   "{text_str}"')
        print(f'Result: "{solution}"')

        result = count_spaces(text)
        output = f"      count_spaces -> "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
