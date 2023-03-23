
# Name: Darlene Bruce
# Prog Purpose: This program finds the cost of movie tickets
#    Price for one ticket: $10.99
#    Sales tax rate: 5.5%

import datetime

########### define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

########## define program functions ##########
def main():
    get_user_data()
    perform_calculations()
    display_results()

# Asks the user how many tickets they would like to purchase.
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

# Calculate the total ticket sales.
def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

# Print the results to the screen.
def display_results():
    print('-----------------------------')
    print('**** Cinema House Movies ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax   $ ' + format(sales_tax, '8,.2f'))
    print('Total       $ ' + format(total, '8,.2f'))    
    print('-----------------------------')
    print(str(datetime.datetime.now()))

############ call on main program to execute ###########
main()
