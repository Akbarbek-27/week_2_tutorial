# Problem Statement: You are building a pricing system for a movie theater
# . The price of a ticket depends on the customer’s age. 
# Write a program that asks the user for their age and then prints the corresponding ticket price based on the following rules:
# Children (age 12 and under): $8
# Adults (age 13 to 64): $15
# Seniors (age 65 and over): $10
# Key Concepts to Apply:
# Getting user input with input().
# Converting the input string to a number with int().
# Using an if-elif-else statement to handle multiple conditions.
# Hint: Think about the order of your conditions. You can check for the youngest group first (age <= 12), then the oldest (age >= 65), and the else block can handle everyone in between.

# Example Output (for an adult):
# --- Movie Ticket Pricer ---
# Please enter your age: 35
# You fall into the 'Adult' category.
# Your ticket price is: $15
price_young = 8
price_adult = 15
price_senior = 10
user = int(input("Please write your age:"))
if user < 13:
    print("You fall into the 'Children' category")
    print(f"Your ticket value:{price_young}$")
elif user < 65:
    print("You fall into the 'Adult' category")
    print(f"Your ticket value:{price_adult}$")
else:
    print("You fall into the 'Senior' category")
    print(f"Your ticket value:{price_senior}$")
print("---Movie Ticket Pricer---")