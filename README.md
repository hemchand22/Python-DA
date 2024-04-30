# BAKERY-MANAGEMENT
The provided code is a Python program that simulates a bakery management system for a fictional bakery named HeavenlyBake. It consists of classes and functions to handle customer orders, generate bills, display the menu, manage staff details, and calculate salary-related information. Here is a breakdown of the key components:
## Classes:
## Staff Class:
### Attributes:
salary, work
### Methods:
calculate_salary_hike(): Calculates the salary hike based on the type of work.
calculate_attendance(num_months): Calculates the number of present and absent days based on attendance percentage.
calculate_tax(total_amount): Calculates the tax amount based on a fixed percentage.
print_details(num_employees): Prints details such as work type, number of employees, salary, salary hike, and attendance.
## Functions:
display_menu(): Displays the bakery menu with items and prices.
get_customer_details(): Takes customer details like name, phone number, and address.
take_order(): Allows customers to place orders by selecting items and quantities from the menu.
generate_bill(customer_name, order): Generates a bill for the customer with details like table number, date, time, ordered items, total price, tax amount, and final amount.
## Main Functionality:
The main() function handles the main flow of the program by prompting the user to choose between being a customer or staff.
If the user is a customer, they can view the menu, place an order, provide details, and generate a bill.
If the user is staff, details of different staff roles (chef, waiter, cleaner, cashier) are displayed including salary, salary hike, and attendance information.
This program effectively demonstrates a simple bakery management system with features for both customers and staff, showcasing interactions like ordering, billing, and staff management.
