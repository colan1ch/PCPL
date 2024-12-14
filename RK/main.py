from operator import itemgetter


class Book:
    def __init__(self, id, title, author, pages_count, lib_id):
        self.id = id
        self.title = title
        self.author = author
        self.pages_count = pages_count
        self.lib_id = lib_id


class Library:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


class BookToLibrary:
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id


libraries = [
    Library(1, 'Российская государственная библиотека', 'г. Москва, ул. Воздвиженка, 3/5'),
    Library(2, 'Центральная библиотека им. Дм. Кедрина', 'г. Мытищи, ул. Летная, 14к1'),
    Library(3, 'Центральная детская библиотека №46 имени А.С. Грибоедова', 'г. Москва, ул. Сущёвский Вал, 66'),
    Library(4, 'Библиотека имени Эйзенштейна', 'г. Москва, ул. Каретный Ряд, 5/10'),
    Library(5, 'Библиотека-читальня им. И.С. Тургенева', 'г. Москва, Бобров переулок, 6, стр. 1'),
]

books = [
    Book(1, '1984', 'Джордж Оруэлл', 312, 1),
    Book(2, 'Понедельник начинается в субботу', 'Аркадий и Борис Стругацкие', 223, 2),
    Book(3, 'Повелитель мух', 'Уильям Голдинг', 345, 2),
    Book(4, 'Убить пересмешника', 'Харпер Ли', 416, 2),
    Book(5, 'Убийство в восточном экспрессе', 'Агата Кристи',225,  3),
    Book(6, 'Убийства по алфавиту', 'Агата Кристи', 282, 4),
    Book(7, 'Три товарища', 'Эрих Мария Ремарк', 388, 4),
    Book(8, 'Гарри Поттер и орден феникса', 'Джоан Роулинг', 685, 5)
]

books_to_libraries = [
    BookToLibrary(1, 1),
    BookToLibrary(2, 1),
    BookToLibrary(2, 2),
    BookToLibrary(2, 3),
    BookToLibrary(2, 4),
    BookToLibrary(3, 5),
    BookToLibrary(4, 6),
    BookToLibrary(4, 7),
    BookToLibrary(5, 8),
]


one_to_many = [
    (book.title, book.author, book.pages_count, lib.name)
    for lib in libraries
    for book in books
    if book.lib_id == lib.id
]

many_to_many_temp = [
    (lib.name, bl.lib_id, bl.book_id)
    for lib in libraries
    for bl in books_to_libraries
    if lib.id == bl.lib_id
]

many_to_many = [
    (book.title, book.author, book.pages_count, lib_name)
    for lib_name, lib_id, book_id in many_to_many_temp
    for book in books if book.id == book_id
]


def main():
    print('Задание 1:\nБиблиотеки, начинающиеся на букву "Б" и список книг')
    libs = {}
    for i in one_to_many:
        if i[-1] in libs:
            libs[i[-1]].append(i[:3])
        else:
            libs[i[-1]] = [i[:3]]
    print({x: libs[x] for x in libs if x[0].startswith('Б')})
    print('\nЗадание 2:\nСписок библиотек с максимальным количеством страниц среди книг в этой библиотеке')
    ans2 = [[l, max(libs[l], key=lambda x: x[2])[2]] for l in libs]
    ans2.sort(key=lambda x: x[1])
    print(ans2)
    print('\nЗадание 3:\nСписок всех книг во всех библиотеках')
    for book_title, book_author, pages_count, lib_name in sorted(many_to_many, key=itemgetter(3)):
        print(f'Книга {book_title} автора {book_author} (кол-во страниц {pages_count}) находится в {lib_name}')


if __name__ == '__main__':
    main()
