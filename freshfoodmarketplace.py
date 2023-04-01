# Name: Darlene Bruce
# Prog Purpose: This program calculates the the gross pay, deductions, 
# and net pay for an employee based on the number of hours they worked 
# and their job category. It does this for one employee at a time.
# 
# Category codes and hourly pay rates:
#    C    Cashier         $16.50
#    S    Stocker         $15.75
#    J    Janitor         $15.75
#    M    Maintenance     $19.50
#
# Deduction rates:
# Federal income tax rate:  12%
# State income tax rate:     3%
# Social security tax rate:  6.2%
# Medicare tax rate:         1.45%

import datetime

########### define global variables ##########

# define global variables
employ_name = ''
job_code = ''
hours_worked = 0
gross_pay = 0.0
fed_inc_tax = 0.0
state_inc_tax = 0.0
ss_tax = 0.0
medic_tax = 0.0
total_deduct = 0.0
net_pay = 0.0

# define hourly pay rates per job title as tuple
hourly_pay_rates = (16.50, 15.75, 15.75, 19.50)

# define deduction rates as tuple
deduction_rates = (0.12, 0.03, 0.062, 0.0145)

########## define program functions ##########
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to enter data for another employee? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False


# Asks the user for job category code and hours worked by employee.
def get_user_data():
    global employ_name, job_code, hours_worked
    print('---------------------------------------------')
    print("*********************************************")
    print("****** Fresh Food Marketplace Store    ******")
    print("****** Individual Employee Weekly Pay  ******")
    print("*********************************************")
    print('---------------------------------------------')
    employ_name = input("\nPlease enter the employees full name: ")
    job_code = input("Please enter employees job code (C(Cashier), S(Stocker), J(Janitor), M(Maintenance)): ")
    hours_worked = int(input("How many hours did the employee work?"))

# Calculate the gross pay, deductions, and net pay per employee.
def perform_calculations():
    global job_code, hours_worked, gross_pay, fed_inc_tax, state_inc_tax, ss_tax, medic_tax, total_deduct, net_pay
    if job_code.upper() == "C":
        gross_pay = hours_worked * hourly_pay_rates[0]
    elif job_code.upper() == "S":
        gross_pay = hours_worked * hourly_pay_rates[1]
    elif job_code.upper() == "J":
        gross_pay = hours_worked * hourly_pay_rates[2]
    elif job_code.upper() == "M":
        gross_pay = hours_worked * hourly_pay_rates[3]
    else:
        print("Invalid job code entry. Please try again.")
    fed_inc_tax = gross_pay * deduction_rates[0]
    state_inc_tax = gross_pay * deduction_rates[1]
    ss_tax = gross_pay * deduction_rates[2]
    medic_tax = gross_pay * deduction_rates[3]
    total_deduct = fed_inc_tax + state_inc_tax + ss_tax + medic_tax
    net_pay = gross_pay - total_deduct
    
   
# Print the results to the screen.
def display_results():
    print('---------------------------------------------')
    print('*********************************************')
    print('****** Fresh Food Marketplace Store    ******')
    print('****** Individual Employee Weekly Pay  ******')
    print('*********************************************')
    print('---------------------------------------------')
    print('Employee Name:       ', employ_name)
    print('Job Category Code:   ', job_code)
    print('Hours Worked:        ', hours_worked)
    print('Gross Pay                      $ ' + format(gross_pay, '8,.2f'))
    print('Federal Income Tax Rate        $ ' + format(fed_inc_tax, '8,.2f'))
    print('State Income Tax Rate          $ ' + format(state_inc_tax, '8,.2f'))
    print('Social Security Tax Rate       $ ' + format(ss_tax, '8,.2f'))
    print('Medicare Tax Rate              $ ' + format(medic_tax, '8,.2f'))
    print('Total Deductions               $ ' + format(total_deduct, '8,.2f'))
    print('Net Pay                        $ ' + format(net_pay, '8,.2f'))    
    print('--------------------------------------------')
    print(str(datetime.datetime.now()))

############ call on main program to execute ###########
main()






