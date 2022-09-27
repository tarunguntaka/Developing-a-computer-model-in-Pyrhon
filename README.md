

# DESCRIPTION OF THE MODEL
- I have implemented the model using two classes DataBase and Book.
- Book class contains four types of attributes title, author, stock, and kind. They are private in nature.
- There are a few getters and setters functions for the Book class.
- I have overridden the equality function ( __eq__ ) and also ( __str__ ) string representation function in order to check the quality between the objects and to print the objects.
- The Database class has functions to insert, query, update and delete a book.
- It has a private attribute _id_to_book which contains an id mapping to a book object.
- The main.py is the whole implementation of these classes. 
- A database d3 was already created in the database class. 
- In the main file, I have implemented the insert, query, update, and delete methods based on the matches given by regex patterns. 
- The main.py also needs one argument to run it and it has to be a .txt file that initializes the database. It accepts 5 commands, insert, query, update, delete and exit. This input is parsed by regex expressions and the corresponding commands are called in the database class functions where we have already implemented our core idea. 
- I have implemented both ebooks and normal books in a book class where the type of the class takes care of these two types of books. Since these are stored in a dictionary it’s easy to perform operations on them. It is incremented each time whenever a book object is created.


# STEPS TO RUN 

- Run the main.py with one argument
- python main.py startup.txt
- ENTER THE COMMAND IN THE COMMAND LINE SUCH AS insert p "project" "tarun" 1 

