class Database:
    _id = 0

    def __init__(self):
        self._id_to_book = {}

    def display_all_books(self):
        for i, v in self._id_to_book.items():
            print(v)

    def add_book(self, book, stock, type="normal"):
        if type != "electronic" and type != "normal":
            print("Type can be either normal or electronic")
            return
        for i in self._id_to_book.keys():
            if self._id_to_book[i] == book and self._id_to_book[i].get_type() == type:
                book.set_type(type)
                a = int(self._id_to_book[i].get_stock())
                b = a + stock
                self._id_to_book[i].set_stock(b)
                # self._id_to_book[Database.id] = book
                print("Added " + str(stock) + " stock to " + str(type) + " book " + (book.get_title()) + " by " + (
                    book.get_author()) + " now with " + str(b) + " copy(s), ID = " + str(i))
                return
        book.set_type(type)
        book.set_stock(stock)
        self._id_to_book[Database._id] = book

        if type == "normal":
            print(
                "Created a new entry for a physical book: " + (book.get_title()) + " by " + (
                    book.get_author()) + " with " + str(
                    book.get_stock()) + " copy(s), ID = " + str(Database._id))
        else:
            print(
                "Created a new entry for a electronic book: " + (book.get_title()) + " by " + (
                    book.get_author()) + " with " + str(
                    book.get_stock()) + " copy(s), ID = " + str(Database._id))
        Database._id += 1

    def get_book_by_id(self, id):
        return self._id_to_book[id]

    def search_book_by_at(self, at, term):
        if at == "a":
            for i, v in self._id_to_book.items():
                if term in v.get_author():
                    print(
                        "MATCH: " + str(
                            v.get_stock()) + " copy(s) - " + v.get_title() + ", " + v.get_author() + "; ID = " + str(i))
        elif at == "t":
            for i, v in self._id_to_book.items():
                if term in v.get_title():
                    print(
                        "MATCH: " + str(
                            v.get_stock()) + " copy(s) - " + v.get_title() + ", " + v.get_author() + "; ID = " + str(i))
        else:
            print("No match")

    def delete_book_by_id(self, id):
        if id not in self._id_to_book.keys():
            print("ERROR: failed to find a book with ID " + str(id))
            return
        a = self._id_to_book[id]
        print("SUCCESS: Deleted " + str(
            a.get_stock()) + " copy(s) of " + a.get_type() + " book " + a.get_title() + " by " + a.get_author())
        del self._id_to_book[id]

    def update_stock(self, id, stock):
        if id not in self._id_to_book.keys():
            print("ERROR: failed to find a book with ID " + str(id))
            return
        book1 = self.get_book_by_id(id)
        a = int(book1.get_stock())
        ss = int(stock + a)
        if ss < 0:
            print("ERROR: Cannot modify stock of " + str(book1.get_type()) + " book " + (book1.get_title()) + " by " + (
                book1.get_author()) + " by " + str(stock) + "; there are only " + str(a) + " available copies")
        else:
            self._id_to_book[id].set_stock(stock + a)
            print(
                "SUCCESS: Modified stock of " + book1.get_type() + " book " + book1.get_title() + " by " + book1.get_author() + " by " + str(
                    stock) + "; now with " + str(ss) + " copy(s).")


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._stock = 1
        self._type = "normal"

    def get_title(self):
        return self._title

    # def set_title(self, title):
    #     self._title = title

    def get_author(self):
        return self._author

    # def set_author(self, author):
    #     self._author = author

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        self._stock = stock

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.get_title() == other.get_title() and self.get_author() == other.get_author()

    def __str__(self):
        return str(self.__dict__)


d3 = Database()
