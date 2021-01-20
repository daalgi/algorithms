import random
from datetime import datetime

screen = [
    '\n' * 50 + '*' * 50,
    '\n1 - Tabla de multiplicar aleatoria',
    '\n2 - Multiplicaciones aleatorias',
    '\n3 - Exit\n'
]


def main():
    end = False
    while not end:
        print(''.join(screen))
        selection = int(input('Select an option: '))

        if selection == 1:
            tabla_de_multiplicar()
        elif selection == 2:
            multiplicaciones_aleatorias()
        elif selection == 3:
            end = True

def check_multiplication(a, b, res):
    if res.isdigit():
        if int(res) == int(a * b):
            return 10
    return 0

def print_score(score, time_start):
    time = datetime.now() - time_start    
    print(f'\nYour score: {score}/100')    
    input(f'\nTime: {time.seconds} s {int(time.microseconds/1000)} ms\n')

def tabla_de_multiplicar():
    tabla = random.randint(1, 10)
    score = 0
    time_start = datetime.now()
    for i in range(1, 11):
        res = input(f'{i} x {tabla} = ')
        score += check_multiplication(i, tabla, res)
    print_score(score, time_start)

def multiplicaciones_aleatorias():
    score = 0
    time_start = datetime.now()
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        res = input(f'{a} x {b} = ')
        score += check_multiplication(a, b, res)
    print_score(score, time_start)


if __name__ == "__main__":
    main()