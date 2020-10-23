# используется для сортировки
from operator import itemgetter


class sec:
    """Section"""

    def __init__(self, id, title, str_count, doc_id):
        self.id = id
        self.title = title
        self.sec_id = doc_id
        self.str_count = str_count

class doc:
    """Document"""

    def __init__(self, id, doc_title):
        self.id = id
        self.doc_title = doc_title


class docsec:
    """
    'Document section' для реализации
    связи многие-ко-многим
    """

    def __init__(self, sec_id, doc_id):
        self.sec_id = sec_id
        self.doc_id = doc_id


# Sections
docs = [
    doc(1, 'ВСАСОИУ_лаб1_метода'),
    doc(2, 'РиП_Лаб1_отчет'),
    doc(3, 'СиТ_методичка_по_первой_лабе'),
]

# Documents
sect = [
    sec(1, 'Теоретическая часть', 50, 1),
    sec(2, 'Задание', 2, 1),
    sec(3, 'Задание', 2, 2),
    sec(4, 'Код программы', 4, 2),
    sec(5, 'Вывод', 1, 2),
    sec(6, 'Теоретическая часть', 30, 3),
    sec(7, 'Задание', 5, 3),


]

Document_Section = [
    docsec(1, 1),
    docsec(2, 1),
    docsec(3, 1),
    docsec(4, 2),
    docsec(5, 2),
    docsec(6, 3),
    docsec(7, 3),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(s.title, s.str_count, d.doc_title)
                   for d in docs
                   for s in sect
                   if s.sec_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.doc_title, ds.sec_id, ds.doc_id)
                         for d in docs
                         for ds in Document_Section
                         if d.id == ds.sec_id]

    many_to_many = [(s.title, doc_name)
                    for doc_name, sec_id, doc_id in many_to_many_temp
                    for s in sect if s.id == doc_id]

    print('Задание B1')
    res_11 = list(filter(lambda x: x[0].startswith('В'), one_to_many))
    print(res_11)

    print('\nЗадание B2')
    res_12_unsorted = []
    for d in docs:
        d_sect = list(filter(lambda i: i[2] == d.doc_title, one_to_many))
        if len(d_sect) > 0:
            count = [str_count for _, str_count, _ in d_sect]
            count_min = min(count)
            res_12_unsorted.append((d.doc_title,  count_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print(res_13)


if __name__ == '__main__':
    main()

