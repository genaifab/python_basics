# BOOK CATEGORIZER WITH FUNCTIONS - Organizing code into reusable pieces

# Defining a function - a reusable block of code that performs a specific task
def categorize_book(title, pages):
    # Multiple conditions with elif (else if)
    if pages > 250:
        return f"{title} is a very long book ({pages} pages)"
    elif pages > 150:
        return f"{title} is a medium book ({pages} pages)"
    else:
        return f"{title} is a short book ({pages} pages)"

# Our data - same dictionary structure as before
books = {"1984": 185, "To Kill a Mockingbird": 281, "The Great Gatsby": 180}

# Using the function in a loop
for title, pages in books.items():
    result = categorize_book(title, pages)  # Calling the function
    print(result)

# Key concepts for absolute beginners:
#
# 1. FUNCTIONS: def function_name(parameters):
#    - Functions are like mini-programs that do specific jobs
#    - "def" tells Python "I'm creating a function"
#    - Function names should describe what they do
#    - Code inside the function is indented (just like loops and if statements)
#
# 2. PARAMETERS: title, pages
#    - Parameters are inputs the function needs to work
#    - Think of them as empty boxes that get filled when you call the function
#    - "title" and "pages" are placeholders for actual values
#    - Parameters make functions flexible - they work with different data
#
# 3. RETURN STATEMENTS: return value
#    - "return" sends a result back to whoever called the function
#    - It's like the function's answer or output
#    - The function stops running when it hits a return statement
#    - Without return, functions just do work but don't give back results
#
# 4. ELIF (ELSE IF): elif condition:
#    - "elif" lets you check multiple conditions in sequence
#    - Python checks if, then elif, then else (in that order)
#    - Only the first True condition runs - the rest are skipped
#    - This creates more sophisticated decision-making
#
# 5. CALLING FUNCTIONS: function_name(arguments)
#    - To use a function, write its name followed by parentheses
#    - Put the actual values (arguments) inside the parentheses
#    - categorize_book("1984", 185) means: title="1984", pages=185
#    - The function runs and returns a result
#
# 6. STORING RESULTS: result = function_call()
#    - Functions that return values can be stored in variables
#    - "result" contains whatever the function returned
#    - This separates the calculation from the display
#
# 7. WHY FUNCTIONS MATTER:
#    - REUSABILITY: Write once, use many times
#    - ORGANIZATION: Break big problems into smaller pieces  
#    - TESTING: Easy to test one function at a time
#    - READABILITY: Code becomes self-documenting
#    - If you needed to change the categorization logic, you only change it in one place!
#
# 8. PROGRAM STRUCTURE:
#    - Define functions first (the tools)
#    - Create your data  
#    - Use the functions to process the data
#    - This is how real programs are organized!