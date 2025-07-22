# TIP CALCULATOR WITH FUNCTIONS - Making code reusable and organized

# Function to calculate tip and total
def calculate_tip(bill_amount, tip_percent):
    tip_amount = bill_amount * (tip_percent / 100)
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount  # Returning two values at once!

# Function to display results nicely
def display_results(bill, tip, total):
    print(f"Bill amount: ${bill:.2f}")
    print(f"Tip amount: ${tip:.2f}")
    print(f"Total amount: ${total:.2f}")
    print("-" * 25)  # Prints a line of dashes for separation

# Main program - using our functions
print("=== TIP CALCULATOR ===")

# Calculate tip for multiple scenarios
restaurants = [
    ("Dinner at Mario's", 45.50, 18),
    ("Lunch at Cafe", 22.75, 15),
    ("Coffee date", 8.20, 20)
]

for name, bill, tip_percent in restaurants:
    print(f"\n{name}:")
    tip, total = calculate_tip(bill, tip_percent)
    display_results(bill, tip, total)

# Interactive version using the same functions
print("\n=== CALCULATE YOUR OWN TIP ===")
user_bill = float(input("Enter bill amount: $"))
user_tip_percent = float(input("Enter tip percentage: "))

tip, total = calculate_tip(user_bill, user_tip_percent)
display_results(user_bill, tip, total)

# Key concepts for absolute beginners:
#
# 1. BREAKING DOWN PROBLEMS:
#    - Instead of one long script, we split the work into functions
#    - calculate_tip() handles the math
#    - display_results() handles the formatting
#    - Each function has one clear job
#
# 2. RETURNING MULTIPLE VALUES:
#    - return tip_amount, total_amount sends back TWO results
#    - tip, total = calculate_tip(...) receives both values
#    - Python automatically "unpacks" multiple return values
#
# 3. REUSABILITY IN ACTION:
#    - We use calculate_tip() for 3 restaurant bills AND user input
#    - Same function, different data - no code duplication!
#    - If we need to change the calculation logic, we only change it once
#
# 4. SEPARATION OF CONCERNS:
#    - calculate_tip() only does math (doesn't print anything)
#    - display_results() only handles formatting and printing
#    - This makes each function simple and focused
#
# 5. WHY FUNCTIONS ARE ESSENTIAL:
#    
#    WITHOUT FUNCTIONS (problems):
#    - Code gets repeated (copy/paste the same calculations)
#    - Hard to change (update logic in multiple places)
#    - Difficult to test (can't test parts separately)
#    - Hard to read (everything mixed together)
#    
#    WITH FUNCTIONS (benefits):
#    - DRY PRINCIPLE: "Don't Repeat Yourself"
#    - MAINTAINABLE: Change logic in one place
#    - TESTABLE: Test each function independently
#    - READABLE: Each function has a clear purpose
#    - SCALABLE: Easy to add new features
#
# 6. REAL-WORLD ANALOGY:
#    - Functions are like kitchen appliances
#    - A blender has one job: blend things
#    - You don't buy a new blender for each smoothie
#    - You use the same blender with different ingredients
#    - Functions work the same way: one tool, many uses!
#
# 7. PROFESSIONAL DEVELOPMENT:
#    - All professional code is organized into functions
#    - Functions make teamwork possible (others can use your functions)
#    - They're the building blocks of larger programs
#    - Learning to think in functions is learning to think like a programmer!