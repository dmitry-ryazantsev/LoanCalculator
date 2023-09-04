import math

loan_principal = int(input(f"Enter the loan principal:\n"))

parameter_to_calculate = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n""")

if parameter_to_calculate.lower() == "m":
    monthly_payment = int(input(f"Enter the monthly payment:\n"))
    months_to_repay = math.ceil(loan_principal / monthly_payment)
    s = "s" if months_to_repay != 1 else ""
    print(f"\nIt will take {months_to_repay} month{s} to repay the loan.")

elif parameter_to_calculate.lower() == "p":
    number_of_months = int(input(f"Enter the number of months:\n"))
    payment = math.ceil(loan_principal / number_of_months)
    last_payment = math.ceil(loan_principal - (number_of_months - 1) * payment)
    if payment == last_payment:
        print(f"\nYour monthly payment = {payment}.")
    else:
        print(f"\nYour monthly payment = {payment} and the last payment = {last_payment}.")
