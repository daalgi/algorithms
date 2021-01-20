# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    bribes = 0
    expected_i, expected_ip1, expected_ip2 = 1, 2, 3
    for i in range(n):
        if q[i] == expected_i:
            expected_i = expected_ip1
            expected_ip1 = expected_ip2
            expected_ip2 += 1
        elif q[i] == expected_ip1:
            bribes += 1
            expected_ip1 = expected_ip2
            expected_ip2 += 1
        elif q[i] == expected_ip2:
            bribes += 2
            expected_ip2 += 1
        else:
            return "Too chaotic"
    return bribes


if __name__ == '__main__':
    t = int(input('\nNumber of queues: '))

    for t_itr in range(t):
        print('-' * 10, f'Queue {t_itr+1}', '-' * 10)
        n = int(input('Length of the queue: '))

        q = list(map(int, input('Queue: ').rstrip().split()))

        b = minimumBribes(q)
        if isinstance(b, int):
            print(f'Minimum bribes: {minimumBribes(q)}')
        else:
            print(b)
