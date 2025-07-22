# BOOK LIST - A program that stores and displays multiple items

# Creating a list - square brackets [] create a list of items
books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "The Catcher in the Rye", "Pride and Prejudice"]

# For loop - repeats an action for each item in the list
for book in books:
    print(book)     # This line runs once for each book in the list

# Key concepts for absolute beginners:
#
# 1. LISTS: books = [item1, item2, item3, ...]
#    - Lists store multiple pieces of data in one variable
#    - Square brackets [] create a list
#    - Items are separated by commas
#    - Each item in this list is a string (book title)
#    - Lists keep items in order - first to last
#
# 2. FOR LOOPS: for item in collection:
#    - Loops repeat code automatically
#    - "for book in books" means: "for each book in the books list"
#    - Python takes each item one by one and puts it in the variable "book"
#    - The indented code runs once for each item
#
# 3. ITERATION (repeating):
#    - 1st time through: book = "1984", prints "1984"
#    - 2nd time through: book = "To Kill a Mockingbird", prints "To Kill a Mockingbird"  
#    - 3rd time through: book = "The Great Gatsby", prints "The Great Gatsby"
#    - And so on... until all books are printed
#
# 4. INDENTATION (spacing):
#    - The print(book) line is indented (moved to the right with spaces/tab)
#    - Indentation tells Python which code belongs to the loop
#    - Everything indented under "for" runs repeatedly
#    - Python is VERY picky about indentation - it must be consistent!
#
# 5. VARIABLE NAMES:
#    - "books" (plural) holds the whole list
#    - "book" (singular) holds one item at a time during the loop
#    - This naming pattern makes code easy to read and understand
#
# 6. WHY LOOPS MATTER:
#    - Without a loop, you'd need to write: print(books[0]), print(books[1]), etc.
#    - Loops let you handle any number of items with just a few lines of code
#    - Imagine if you had 1000 books - the loop stays the same size!