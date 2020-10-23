import sys

from cmath import sqrt


def vku(a, b, c):
    if a == 0:
        t_1 = -c / b
        x1 = x2 = sqrt(t_1)
        x3 = x4 = -sqrt(t_1)
    else:
        d = (b * b) - (4 * a * c)
        t1 = (-b + sqrt(d)) / (2 * a)
        t2 = (-b - sqrt(d)) / (2 * a)
        x1 = sqrt(t1)
        x2 = - sqrt(t1)
        x3 = sqrt(t2)
        x4 = -sqrt(t2)
    return x1, x2, x3, x4

if __name__ == '__main__':
    try:
        a1 = int(sys.argv[1])
        a2 = int(sys.argv[2])
        a3 = int(sys.argv[3])
    except Exception:
        print('Ошибка аргументов командной строки, ввод будет произведен с клавиатуры')
        try:
            a1 = int(input('a1: '))
            a2 = int(input('a2: '))
            a3 = int(input('a3: '))
        except Exception:
            print('Вы ввели неверное значение, программа завершатает свою работу')
            exit(1)

    x1, x2, x3, x4 = vku(a1, a2, a3)
    print(x1, x2, x3, x4)
