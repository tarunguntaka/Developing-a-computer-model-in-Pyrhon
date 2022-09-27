import sys
import re

from Database import *

text = sys.argv[1]

pattern_insert = re.compile(
    "(?P<action>insert)\s(?P<pe>[pe]?)\s(?P<title>\"(.*?)\")\s(?P<author>\"(.*?\s*\"))\s(?P<stock>[0-9]+)")
pattern_query = re.compile("(?P<action>query)\s(?P<at>[at]?)\s(?P<term>\"(.*?)\")")
pattern_delete = re.compile("(?P<delete>delete)\s(?P<id>[0-9]+)")
pattern_update = re.compile("(?P<update>update)\s(?P<id>[0-9]+)\s(?P<stock>-?[0-9]+)")


def insert(matches):
    for match in matches:
        pe = match.group("pe")
        title = match.group("title")
        author = match.group("author")
        stock = int(match.group("stock"))
        type1 = "electronic" if pe == "e" else "normal"
        d3.add_book(Book(title, author), stock=stock, type=type1)


def query(matches1):
    for match1 in matches1:
        at = match1.group("at")
        term = match1.group("term")
        term = term.strip('\"')
        d3.search_book_by_at(at, term)


def delete(matches_del):
    for match in matches_del:
        id1 = match.group("id")
        d3.delete_book_by_id(int(id1))


def update(matches_update):
    for match in matches_update:
        id1 = int(match.group("id"))
        stock = int(match.group("stock"))
        d3.update_stock(id1, stock)


def main():
    with open(text, 'rt') as f:
        contents = f.read()
    matches = pattern_insert.finditer(contents)
    matches1 = pattern_query.finditer(contents)
    matches_del = pattern_delete.finditer(contents)
    matches_update = pattern_update.finditer(contents)
    print(type(matches))
    insert(matches)
    query(matches1)
    delete(matches_del)
    update(matches_update)
    program = True
    while program:
        print("---------------Welcome to Library Inventory Tracker---------------")
        print("---------------THIS PROGRAM ACCEPTS SOME BASIC COMMANDS--------------")
        print("---------------Insert, query, delete, update, exit and display---------------")
        print("Enter your command below ")
        command = input("Enter here: ")
        contents = command.split(' ')
        if contents[0] == "insert":
            mat1 = pattern_insert.finditer(command)
            insert(mat1)
        elif contents[0] == "delete":
            mat2 = pattern_delete.finditer(command)
            delete(mat2)
        elif contents[0] == "update":
            mat3 = pattern_update.finditer(command)
            update(mat3)
        elif contents[0] == "query":
            mat4 = pattern_query.finditer(command)
            query(mat4)
        elif contents[0] == "exit":
            print("GOOD BYE!!!!!!!!!!!!!!!!!!!!!")
            sys.exit()
        elif contents[0] == "display":
            d3.display_all_books()


main()
