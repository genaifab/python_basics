# BOOK CATEGORIZER - Illustrates conditional logic and dictionaries

# Creating a dictionary - curly braces {} with key: value pairs
books = {"1984": 185, "To Kill a Mockingbird": 281, "The Great Gatsby": 180, "The Catcher in the Rye": 214, "Pride and Prejudice": 279}

# Loop through dictionary getting both key and value
for title, pages in books.items():
    # Conditional logic - making decisions based on data
    if pages > 200:
        print(f"{title} is a long book with {pages} pages.")
    else:
        print(f"{title} is a short book with {pages} pages.")

# Key concepts for absolute beginners:
#
# 1. DICTIONARIES: {key: value, key: value, ...}
#    - Dictionaries store pairs of related information
#    - Each "key" (book title) maps to a "value" (page count)
#    - Curly braces {} create a dictionary
#    - Keys and values are separated by colons :
#    - Pairs are separated by commas
#    - Think of it like a real dictionary: word (key) → definition (value)
#
# 2. DICTIONARY METHODS: .items()
#    - books.items() gives us both the key and value from each pair
#    - This lets us get both "title" and "pages" in one loop
#    - Without .items(), we'd only get the keys (titles)
#
# 3. MULTIPLE VARIABLES: title, pages = ...
#    - Python can assign two variables at once
#    - "title" gets the key (book name)
#    - "pages" gets the value (page count)
#    - This is called "unpacking"
#
# 4. CONDITIONAL STATEMENTS: if/else
#    - "if" lets programs make decisions
#    - "pages > 200" is a condition that's either True or False
#    - If True: run the indented code under "if"
#    - If False: run the indented code under "else"
#    - Only one branch runs - never both
#
# 5. COMPARISON OPERATORS:
#    - > means "greater than"
#    - Other examples: < (less than), == (equal to), != (not equal to)
#    - These always result in True or False
#
# 6. PROGRAM LOGIC FLOW:
#    - For each book, Python checks: "Are pages > 200?"
#    - If yes: prints "long book" message  
#    - If no: prints "short book" message
#    - This is how programs make smart decisions automatically!
#
# 7. WHY DICTIONARIES + CONDITIONS MATTER:
#    - Real programs often need to store related data (title + pages)
#    - And make decisions based on that data (long vs short)
#    - This combination is the foundation of data processing