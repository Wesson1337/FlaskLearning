import sqlite3
from dataclasses import dataclass
from typing import Optional, Dict, List

BOOKS = [
    {'id': 0, 'title': 'A byte of python', 'author': 'Swaroop C.H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'War and peace', 'author': 'Leo Tolstoy'},
]

BOOKS_TABLE_NAME = 'books'


@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM sqlite_master "
            f"WHERE type='table' AND name='{BOOKS_TABLE_NAME}';"
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f'CREATE TABLE `{BOOKS_TABLE_NAME}` '
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author)'
            )
            cursor.executemany(
                f'INSERT INTO `{BOOKS_TABLE_NAME}` '
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
            )


def _get_book_obj_from_row(row) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM `{BOOKS_TABLE_NAME}`')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def add_book(book: Book) -> Book:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO `{BOOKS_TABLE_NAME}`
            (title, author) VALUES (?, ?)
            """, (book.title, book.author)
        )
        book.id = cursor.lastrowid
        return book


def update_book_by_id(book: Book):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE {BOOKS_TABLE_NAME}
            SET title = ? , 
                author = ?
            WHERE id = ?
            """, (book.title, book.author, book.id)
        )
        conn.commit()


def delete_book_by_id(book_id):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            DELETE {BOOKS_TABLE_NAME}
            WHERE id = ?
            """, (book_id,)
        )


if __name__ == '__main__':
    init_db(initial_records=BOOKS)
