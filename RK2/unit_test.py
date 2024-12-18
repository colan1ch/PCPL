import unittest
from main import *


class TestTasks(unittest.TestCase):
    def setUp(self):
        self.libraries = [
            Library(1, 'Российская государственная библиотека', 'г. Москва, ул. Воздвиженка, 3/5'),
            Library(2, 'Центральная библиотека им. Дм. Кедрина', 'г. Мытищи, ул. Летная, 14к1'),
            Library(3, 'Центральная детская библиотека №46 имени А.С. Грибоедова', 'г. Москва, ул. Сущёвский Вал, 66'),
            Library(4, 'Библиотека имени Эйзенштейна', 'г. Москва, ул. Каретный Ряд, 5/10'),
            Library(5, 'Библиотека-читальня им. И.С. Тургенева', 'г. Москва, Бобров переулок, 6, стр. 1'),
        ]

        self.books = [
            Book(1, '1984', 'Джордж Оруэлл', 312, 1),
            Book(2, 'Понедельник начинается в субботу', 'Аркадий и Борис Стругацкие', 223, 2),
            Book(3, 'Повелитель мух', 'Уильям Голдинг', 345, 2),
            Book(4, 'Убить пересмешника', 'Харпер Ли', 416, 2),
            Book(5, 'Убийство в восточном экспрессе', 'Агата Кристи', 225, 3),
            Book(6, 'Убийства по алфавиту', 'Агата Кристи', 282, 4),
            Book(7, 'Три товарища', 'Эрих Мария Ремарк', 388, 4),
            Book(8, 'Гарри Поттер и орден феникса', 'Джоан Роулинг', 685, 5)
        ]

        self.books_to_libraries = [
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

        self.one_to_many = make_one_to_many(self.books, self.libraries)
        self.many_to_many = make_many_to_many(self.books, self.libraries, self.books_to_libraries)

    def test_task1(self):
        result = task1(self.one_to_many)
        true_result = {
            'Библиотека имени Эйзенштейна': [('Убийства по алфавиту', 'Агата Кристи', 282), ('Три товарища', 'Эрих Мария Ремарк', 388)],
            'Библиотека-читальня им. И.С. Тургенева': [('Гарри Поттер и орден феникса', 'Джоан Роулинг', 685)]
        }
        self.assertEqual(result, true_result)

    def test_task2(self):
        result = task2(self.one_to_many)
        true_result = [
            ['Центральная детская библиотека №46 имени А.С. Грибоедова', 225],
            ['Российская государственная библиотека', 312],
            ['Библиотека имени Эйзенштейна', 388],
            ['Центральная библиотека им. Дм. Кедрина', 416],
            ['Библиотека-читальня им. И.С. Тургенева', 685]
        ]
        self.assertEqual(result, true_result)

    def test_task3(self):
        result = task3(self.many_to_many)
        true_result = [
            'Книга Убийства по алфавиту автора Агата Кристи (кол-во страниц 282) находится в Библиотека имени Эйзенштейна',
            'Книга Три товарища автора Эрих Мария Ремарк (кол-во страниц 388) находится в Библиотека имени Эйзенштейна',
            'Книга Гарри Поттер и орден феникса автора Джоан Роулинг (кол-во страниц 685) находится в Библиотека-читальня им. И.С. Тургенева',
            'Книга 1984 автора Джордж Оруэлл (кол-во страниц 312) находится в Российская государственная библиотека',
            'Книга 1984 автора Джордж Оруэлл (кол-во страниц 312) находится в Центральная библиотека им. Дм. Кедрина',
            'Книга Понедельник начинается в субботу автора Аркадий и Борис Стругацкие (кол-во страниц 223) находится в Центральная библиотека им. Дм. Кедрина',
            'Книга Повелитель мух автора Уильям Голдинг (кол-во страниц 345) находится в Центральная библиотека им. Дм. Кедрина',
            'Книга Убить пересмешника автора Харпер Ли (кол-во страниц 416) находится в Центральная библиотека им. Дм. Кедрина',
            'Книга Убийство в восточном экспрессе автора Агата Кристи (кол-во страниц 225) находится в Центральная детская библиотека №46 имени А.С. Грибоедова'
        ]

        self.assertEqual(result, true_result)


if __name__ == '__main__':
    unittest.main()
