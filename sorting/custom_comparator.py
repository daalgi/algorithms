from functools import cmp_to_key

class Player:

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f'{self.name}: {self.score}'

    def comparator(a, b):
        # Sort in descending order by score
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            # If the same score, sort in ascending order by name
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            return 0


if __name__ == "__main__":
    print('-' * 60)
    print('Sorting by means of a custom comparator')
    print('-' * 60)
    players = [
        Player("Amy", 100),
        Player("David", 100),
        Player("Heraldo", 50),
        Player("Aakansha", 75),
        Player("Aleksa", 150),
    ]
    print('--> Original list:')
    for i in players:
        print(i)

    classification = sorted(players, key=cmp_to_key(Player.comparator))
    print('\n--> Sorted list:')
    for i in classification:
        print(i)
    print()