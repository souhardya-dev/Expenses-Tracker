# Expenses-Tracker
The Expense Tracker is a menu-driven Python console application designed to help users record, view, and analyze their daily expenses in a simple and organized way.

This program allows users to add expenses, view all recorded expenses, and calculate the total amount spent, using basic Python concepts such as lists, dictionaries, loops, and conditional statements.

⚙️ How the Program Works

Data Storage

All expenses are stored in a list named expenseList.

Each expense is represented as a dictionary containing:

Date – date of the expense

Category – type of expense (Food, Travel, Book, etc.)

Description – details of the expense

Amount – cost of the expense

Menu-Driven Interface

The program runs inside an infinite while loop.

A menu is displayed repeatedly until the user chooses to exit.

The user selects an option by entering a number.

📋 Features of the Expense Tracker
🔹 1. Add Expense

Takes user input for date, category, description, and amount.

Stores the data as a dictionary.

Adds the expense to the expenseList.

🔹 2. View All Expenses

Displays all stored expenses in a formatted list.

Each expense is numbered for easy identification.

If no expenses exist, the program notifies the user.

🔹 3. View Total Cost

Calculates the total amount spent by summing all expense amounts.

Displays the total cost to the user.

🔹 4. Exit

Safely terminates the program with a confirmation message.

🧠 Key Concepts Used

List of Dictionaries for structured data storage

While Loop for continuous execution

Conditional Statements (if-elif-else) for menu selection

User Input Handling using input()

Basic Error Handling using try-except

✅ Advantages

Simple and user-friendly

Easy to understand for beginners

Suitable for academic mini-projects

Can be extended with file handling or GUI support

🏁 Conclusion

This Expense Tracker program is an effective beginner-level Python application that demonstrates how real-life problems such as expense management can be solved using basic programming constructs. It provides a foundation for building more advanced financial tracking systems.
