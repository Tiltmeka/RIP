from field import field

from unique import Unique

from gen_random import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

data = [1, 1, 11, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


if __name__ == "__main__":
    print(list(gen_random(20, 1, 100)))
    print(list(field(goods, 'title')))
    print(list(Unique(data)))
