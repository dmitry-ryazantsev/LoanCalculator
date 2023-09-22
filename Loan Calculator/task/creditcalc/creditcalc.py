import math
import textwrap


def get_loan_principal():
    loan_principal = int(input(f"Enter the loan principal:\n"))
    return loan_principal


def get_monthly_payment():
    monthly_payment = int(input(f"Enter the monthly payment:\n"))
    return monthly_payment


def get_loan_interest():
    interest = float(input(f"Enter the loan interest:\n"))
    # return nominal (monthly) interest rate
    return interest / (12 * 100)


def get_number_of_months():
    number_of_months = int(input(f"Enter the number of periods:\n"))
    return number_of_months


def get_annuity_payment():
    annuity_payment = float(input(f"Enter the annuity payment:\n"))
    return annuity_payment


def get_parameter_to_calculate():
    parameter_to_calculate = input(textwrap.dedent("""\
    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:\n"""))
    if parameter_to_calculate.lower() == "n":
        loan_principal = get_loan_principal()
        monthly_payment = get_monthly_payment()
        interest = get_loan_interest()
        calculate_months_to_repay(loan_principal, monthly_payment, interest)
    elif parameter_to_calculate.lower() == "a":
        loan_principal = get_loan_principal()
        number_of_months = get_number_of_months()
        interest = get_loan_interest()
        calculate_annuity_payment(loan_principal, number_of_months, interest)
    elif parameter_to_calculate.lower() == "p":
        annuity_payment = get_annuity_payment()
        number_of_months = get_number_of_months()
        interest = get_loan_interest()
        calculate_loan_principal(annuity_payment, number_of_months, interest)


def calculate_overpayment(annuity_payment, number_of_months, loan_principal):
    overpayment = math.ceil(annuity_payment * number_of_months - loan_principal)
    print(f"Overpayment = {overpayment}")


def calculate_months_to_repay(loan_principal, monthly_payment, i):
    number_of_months = math.ceil(math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i))
    years, months = divmod(number_of_months, 12)
    plural_years = "s" if years != 1 else ""
    plural_months = "s" if months != 1 else ""
    if years == 0:
        print(f"It will take {months} month{plural_months} to repay this loan!")
    elif months == 0:
        print(f"It will take {years} year{plural_years} to repay this loan!")
    else:
        print(f"It will take {years} year{plural_years} and {months} month{plural_months} to repay this loan!")
    calculate_overpayment(monthly_payment, number_of_months, loan_principal)


def calculate_annuity_payment(loan_principal, number_of_months, i):
    annuity_payment = math.ceil(loan_principal * (i * (1 + i) ** number_of_months) / ((1 + i) ** number_of_months - 1))
    print(f"Your annuity payment = {annuity_payment}!")
    calculate_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_loan_principal(annuity_payment, number_of_months, i):
    loan_principal = math.floor(annuity_payment / ((i * (1 + i) ** number_of_months) / ((1 + i) ** number_of_months - 1)))
    print(f"Your loan principal = {loan_principal}!")
    calculate_overpayment(annuity_payment, number_of_months, loan_principal)


if __name__ == '__main__':
    try:
        get_parameter_to_calculate()
    except KeyboardInterrupt:
        print("The session has been interrupted.")
