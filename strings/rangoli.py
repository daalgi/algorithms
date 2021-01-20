"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

ALPHABET RANGOLI
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

def print_rangoli(size):
    # your code goes here
    first = ord('a')
    last = first + size - 1
    width = (size - 1) * 4 + 1
    res = []
    for line in range(size):
        string = '-'.join(chr(letra) for letra in list(range(last-line, last+1))[::-1])
        if line > 0:
            string += string[:-1][::-1]
        #print(string)
        res.append(string.center(width, '-'))
    print('\n'.join(res + res[:-1][::-1]))


if __name__ == "__main__":
    size = int(input('Enter a positive integer:'))
    print_rangoli(size)