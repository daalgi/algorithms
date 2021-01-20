"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example:
s = mom

The list of all anagrammatic pairs is [m, m], [mo, om]
at positions [[0], [2]], [[0, 1], [1, 2]] respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below.

sherlockAndAnagrams has the following parameter(s):
    string s: a string

Returns
    int: the number of unordered anagrammatic pairs of substrings in 

Input Format
    The first line contains an integer , the number of queries.
    Each of the next  lines contains a string  to analyze.

Sample Input 0
2
abba
abcd

Sample Output 0
4
0

Sample Input 1
2
ifailuhkqq
kkkk

Sample Output 1
3
10
"""
def solution(s):
    count = 0
    n = len(s)
    for size in range(1, n):
        for start in range(0, n+1-size):
            sub1 = ''.join(sorted(s[start:start+size]))
            for position in range(start+1, n+1-size):
                sub2 = ''.join(sorted(s[position:position+size]))
                #print(start, sub1, sub2)
                if sub1 == sub2:
                    count += 1

    return count


test_cases = [
    ("mom", 2),
    ("abba", 4),
    ("abcd", 0),
    ("ifailuhkqq", 3),
    ("kkkk", 10),
    ("cdcd", 5),
    ("dbcfibibcheigfccacfegicigcefieeeeegcghggdheichgafhdigffgifidfbeaccadabecbdcgieaffbigffcecahafcafhcdg", 1464),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 166650)
]
for s, result in test_cases:
    res = solution(s)
    print(f'{s:13}\tAnagrammatic pairs = {res:3}',
        f'\tTest: {"OK" if res == result else "NOT OK"}')
