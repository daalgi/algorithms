class FenwickTree:
    def __init__(self, array: list, verbose: bool = True):
        self.n = len(array) + 1
        self.bit = [0, *array]
        string = ''
        for index in range(1, self.n):

            if verbose:
                string  = f'Index: {index:>2}'
                string += f'\tValue: {array[index-1]:>2}'
                string += f'\tNext index: {index + (index & -index):>2}'

            next_index = index + (index & -index)
            if next_index < self.n:
                self.bit[next_index] += self.bit[index]
                
                if verbose:
                    string += f'\tNext bit: {self.bit[next_index]:>2}'
                    print(string)

    def prefix_sum(self, index):
        index += 1
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index ^= index & -index
        return ans

    def update(self, index, diff):
        index += 1
        while index < self.n:
            self.bit[index] += diff
            index += index & -index
    
    def __str__(self) -> str:
        return str(self.bit)