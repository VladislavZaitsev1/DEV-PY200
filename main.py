BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if id_ < 0:
            raise ValueError('Значение должно быть больше 0')

        if not isinstance(name, str):
            raise TypeError('Ошибка типа! Параметр должен быть str')

        if not isinstance(pages, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if id_ < 0:
            raise ValueError('Значение должно быть больше 0')

        self.id_ = id_
        self.name = name
        self.pages = pages


    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'

# TODO написать класс Library
class Library:

    def __init__(self, books: list = None):
        if not books:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            i = 1
        else:
            list_id = [Book.id_ for Book in list_books]
            i = list_id[-1] + 1
        return i

    def get_index_by_book_id(self, ind) -> (int, str):
        if not isinstance(ind, int):
            raise TypeError('Ошибка типа!')
        list_id = [Book.id_ for Book in list_books]
        if ind in list_id:
            return list_id.index(ind)
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
