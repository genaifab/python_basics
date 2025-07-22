# TIP CALCULATOR - A program that calculates tips and totals

# Getting user input - the input() function asks the user to type something
bill = input("Enter the total bill amount: $")
tip_percentage = input("Enter the tip percentage (e.g., 15 for 15%): ")

# Converting text to numbers - input() always gives us text (strings)
bill = float(bill)              # float() converts text to decimal number
tip_percentage = float(tip_percentage)  # We need numbers to do math!

# Mathematical calculations - Python can do arithmetic just like a calculator
tip_amount = bill * (tip_percentage / 100)  # Calculate tip: bill × (percentage ÷ 100)
total_amount = bill + tip_amount            # Add tip to original bill

# Displaying results with formatted strings (f-strings)
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount (including tip): ${total_amount:.2f}")

# Key concepts for absolute beginners:
#
# 1. VARIABLES: bill, tip_percentage, tip_amount, total_amount
#    - Variables are like labeled boxes that store data
#    - You can put data in them and use it later
#    - The = sign assigns (puts) a value into a variable
#
# 2. USER INPUT: input() function
#    - Pauses the program and waits for user to type something
#    - The text in parentheses is called a "prompt" - it tells user what to enter
#    - Whatever the user types becomes a string (text)
#
# 3. DATA TYPES: strings vs numbers
#    - input() always returns a string, even if user types numbers
#    - float() converts strings to decimal numbers so we can do math
#    - You can't do math with strings like "15" - you need the number 15
#
# 4. ARITHMETIC OPERATORS:
#    - * means multiply
#    - / means divide  
#    - + means add
#    - Parentheses control order of operations (just like in math class)
#
# 5. F-STRINGS: f"text {variable}"
#    - The f before the quote makes it a "formatted string"
#    - Curly braces {} let you insert variables into text
#    - :.2f means "show 2 decimal places" (perfect for money!)
#
# 6. PROGRAM FLOW:
#    - Get input from user
#    - Process/calculate the data  
#    - Display results
#    - This is the basic pattern of many programs!