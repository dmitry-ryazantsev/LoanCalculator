import math
import textwrap


def get_loan():
    loan_principal = int(input(f"Enter the loan principal:\n"))
    return loan_principal


def get_parameter_to_calculate(loan_principal):
    parameter_to_calculate = input(textwrap.dedent("""\
    What do you want to calculate?
    type "m" - for number of monthly payments,
    type "p" - for the monthly payment:\n"""))
    if parameter_to_calculate.lower() == "m":
        calculate_months_to_repay(loan_principal)
    elif parameter_to_calculate.lower() == "p":
        calculate_monthly_payments(loan_principal)


def calculate_months_to_repay(loan_principal):
    monthly_payment = int(input(f"Enter the monthly payment:\n"))
    months_to_repay = math.ceil(loan_principal / monthly_payment)
    s = "s" if months_to_repay != 1 else ""
    print(f"\nIt will take {months_to_repay} month{s} to repay the loan.")


def calculate_monthly_payments(loan_principal):
    number_of_months = int(input(f"Enter the number of months:\n"))
    payment = math.ceil(loan_principal / number_of_months)
    last_payment = math.ceil(loan_principal - (number_of_months - 1) * payment)
    if payment == last_payment:
        print(f"\nYour monthly payment = {payment}.")
    else:
        print(f"\nYour monthly payment = {payment} and the last payment = {last_payment}.")


if __name__ == '__main__':
    try:
        loan_principal = get_loan()
        get_parameter_to_calculate(loan_principal)
    except KeyboardInterrupt:
        print("The session has been interrupted.")
