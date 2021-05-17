from random import randint

A = 1
B = 100

def is_valid(text):
    if not text.isdigit():
        return False
    return A <= int(text) <= B

C = randint(A, B)
print('Добро пожаловать в числовую угадайку')
is_guessed = False

while not is_guessed:
    x = input(f'Попробуйте угадать число от {A} до {B}: ')
    if not is_valid(x):
        print(f'А может быть все-таки введем целое число от {A} до {B}?')
        continue
    x = int(x)
    if x < C:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif x > C:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        is_guessed = True
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
