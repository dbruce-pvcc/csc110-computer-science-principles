
# Name: Darlene Bruce
# Prog Purpose: This program calculates the cost for one pizza order. The program asks
# for pizza size and number of pizzas of that size. It only allows the user to order
# one pizza size at a time, but the user has the option to place additional orders.
# 
# Pizza size codes and prices:
#    S    Small          $ 9.99
#    M    Medium         $12.99
#    L    Large          $14.99
#    X    Extra Large    $17.99
#
# Sales tax rate: 5.5%

import datetime

########### define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_S_PIZZA = 9.99
PR_M_PIZZA = 12.99
PR_L_PIZZA = 14.99
PR_X_PIZZA = 17.99

# define global variables
pizza_size = ""
num_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

########## define program functions ##########
def main():
    more_pizza = True
    while more_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order another pizza? (Y/N): ")
        if yesno.upper() != "Y":
            more_pizza = False


# Asks the user for pizza sizes and number of pizzas.
def get_user_data():
    global num_pizza, pizza_size
    print("\n**************************************")
    print("****** Welcome to Palermo Pizza ******")
    print("****** Please Place Your Order  ******")
    print("**************************************\n")
    pizza_size = input("What size pizza would you like (S(Small), M(Medium), L(Large), X(Extra Large))?")
    num_pizza = int(input("How many of that size pizza would you like?"))

# Calculate the total pizza order amount.
def perform_calculations():
    global pizza_size, subtotal, sales_tax, total
    if pizza_size.upper() == "S":
        subtotal = PR_S_PIZZA * num_pizza
    elif pizza_size.upper() == "M":
        subtotal = PR_M_PIZZA * num_pizza
    elif pizza_size.upper() == "L":
        subtotal = PR_L_PIZZA * num_pizza
    elif pizza_size.upper() == "X":
        subtotal = PR_X_PIZZA * num_pizza
    else:
        print("Invalid pizza size entry. Please order again.")
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
   
# Print the results to the screen.
def display_results():
    print('---------------------------------')
    print('********* Palermo Pizza *********')
    print('Hot and fresh pizza made to order')
    print('---------------------------------')
    print('Pizza Cost     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax      $ ' + format(sales_tax, '8,.2f'))
    print('Total          $ ' + format(total, '8,.2f'))    
    print('---------------------------------')
    print(str(datetime.datetime.now()))

############ call on main program to execute ###########
main()
 