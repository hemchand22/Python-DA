class Staff:
    def __init__(self, salary, work):
        self.salary = salary
        self.work = work

    def calculate_salary_hike(self):
        hike_dict = {'chef': 0.05, 'waiter': 0.025, 'cleaner': 0.01, 'cashier': 0.025}
        for key in hike_dict:
            if self.work.lower() == key:
                return self.salary * hike_dict[key]

    def calculate_attendance(self, num_months):
        total_days = num_months * 30  # Assuming each month has 30 days
        present_days = int(total_days * 0.9)  # Assuming 90% attendance
        absent_days = total_days - present_days
        return present_days, absent_days

    
    def calculate_tax(total_amount):
        tax_percentage = 0.05  # 5% tax
        tax_amount = total_amount * tax_percentage
        return tax_amount

    def print_details(self, num_employees):
        hike = self.calculate_salary_hike()
        present_days, absent_days = self.calculate_attendance(2)  # Assuming 2 months of attendance
        
        print("Type of Work:", self.work.capitalize())
        print("Number of Employees:", num_employees)
        print("Salary per Employee:", self.salary)
        print("Salary Hike:", hike)
        print("Attendance (working days):")
        print("   Working Days:", present_days)
        print("   Non Working Days:", absent_days)
        print("\n")


menu = {
    "Croissant": 250,
    "Baguette": 300,
    "Muffin": 75,
    "Cupcake": 40,
    "Brownie": 80,
    "Bread": 35,
    "Cake": 250,
    "Cookies": 15,
    "Samosa": 25,
    "Veg puff": 27,
    "Paneer puff": 30,
    "Mushroom puff": 35,
    "Gobi puff": 29,
    "Chicken puff": 37,
    "Veg sandwich": 49,
    "Paneer sandwich": 27,
    "Chicken sandwich": 27,
    "Rose milk": 50,
    "Badam milk": 37,
    "Potato chips": 50,
    "Banana chips": 50,
    "Bitter gourd chips": 50,
    "Candles": 15,
    "Extra cheese": 15
}

def display_menu():
    print("******* Welcome to Heavenlybake *******")
    print("      From Our Oven to Your Heart      ")
    print("Menu:")
    for item, price in menu.items():
        print(f"    {item}: ${price}")

def get_customer_details():
    name = input("Enter your name: ")
    while True:
        phone_number = input("Enter your phone number: ")
        if phone_number.isdigit() and len(phone_number) in (10, 11):
            break
        print("Invalid phone number! Please enter a valid phone number (10 or 11 digits).")
    address = input("Enter your address: ")
    return name, phone_number, address

def take_order():
    order = {}
    while True:
        item = input("Enter the item you want to order (or type 'done' to finish): ").capitalize()
        if item == 'Done':
            break
        elif item in menu:
            quantity = input(f"Enter the quantity of {item}: ")
            if quantity.isdigit() and int(quantity) > 0:
                order[item] = int(quantity)
            else:
                print("Invalid quantity! Please enter a positive integer.")
        else:
            print("Invalid item! Please choose from the menu.")
    return order

def generate_bill(customer_name, order):
    total_price = 0
    table_number = input("Enter table number: ")

    while True:
        date_str = input("Enter date (DD/MM/YYYY): ")
        if len(date_str) == 10 and date_str[2] == '/' and date_str[5] == '/':
            day, month, year = date_str.split('/')
            if all(part.isdigit() for part in (day, month, year)) and (1 <= int(day) <= 31) and (1 <= int(month) <= 12):
                break
        print("Invalid date format! Please enter date in DD/MM/YYYY format.")

    while True:
        time_str = input("Enter time (HH:MM): ")
        if len(time_str) == 5 and time_str[2] == ':' and all(part.isdigit() for part in time_str.split(':')):
            hour, minute = map(int, time_str.split(':'))
            if 0 <= hour < 24 and 0 <= minute < 60:
                break
        print("Invalid time format! Please enter time in HH:MM format.")

    print("                HeavenlyBake Bakery                ")
    print("             From Our Oven to Your Heart           ")
    print("                 Opp VIT Main Gate                 ")
    print("                      Vellore                      ")
    print("---------------------------------------------------")
    
    print(f"Table {table_number}                         Date: {date_str} ")
    print(f"Customer Name: {customer_name}                 Time: {time_str} ")
    print("...................................................")
    print("Description              QTY      RATE       AMOUNT")
    print("...................................................")
    
    for item, quantity in order.items():
        price = menu[item] * quantity
        total_price += price
        print(f"{item:<25}{quantity:<3}      ${menu[item]:<5}       ${price:<7}")
    
    tax_amount = Staff.calculate_tax(total_price)
    total_price_with_tax = total_price + tax_amount

    print("...................................................")
    print(f"TOTAL PRICE                                  ${total_price:<5}")
    print(f"Tax (5%):                                    ${tax_amount:<5}")
    print("---------------------------------------------------")
    print(f"TOTAL AMOUNT (including CGST and SGST)       ${total_price_with_tax:<5}")
    print(" ")
    print("THANK YOU VISIT AGAIN")
    print("For Home Delivery Contact: 8074240766")
    print("\n")


def main():
    while True:
        print("Customer Service and Staff Details")
        print("-----------------------------------")
        role = input("Are you a customer or staff? Enter 'customer' or 'staff': ").lower()
        if role == 'customer':
            display_menu()
            if input("Ready to give order? (yes/no): ").lower() == 'yes':
                name, phone_number, address = get_customer_details()
                order = take_order()
                generate_bill(name, order)
            else:
                print("Please come back when you are ready to give an order.")
        elif role == 'staff':
            chef = Staff(salary=30000, work='chef')
            waiter = Staff(salary=15000, work='waiter')
            cleaner = Staff(salary=10000, work='cleaner')
            cashier = Staff(salary=12000, work='cashier')
            print("\nStaff Details:")
            print("Total number of employees are 10\n")
            chef.print_details(num_employees=4)
            waiter.print_details(num_employees=3)
            cleaner.print_details(num_employees=2)
            cashier.print_details(num_employees=1)
        else:
            print("Invalid input. Please enter 'customer' or 'staff'.")

if __name__ == "__main__":
    main()
