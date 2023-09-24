import argparse
import math


parser = argparse.ArgumentParser(description="The program allows to calculate differentiated or annuity loans")

parser.add_argument("--type", required=True, choices=["diff", "annuity"],
                    help="Only one loan type can be selected")
parser.add_argument("--principal", type=int,
                    help="Denotes the loan principal")
parser.add_argument("--payment", type=int,
                    help="Denotes the annuity payment")
parser.add_argument("--periods", type=int,
                    help="Denotes the number of months")
parser.add_argument("--interest", required=True, type=float,
                    help="Denotes the interest rate")
args = parser.parse_args()

loan_type = args.type
loan_principal = args.principal
annuity_payment = args.payment
number_of_months = args.periods
interest = args.interest / (12 * 100)  # Convert annual monthly interest rate to monthly


def calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal):
    overpayment = math.ceil(annuity_payment * number_of_months - loan_principal)
    print(f"Overpayment = {overpayment}")


def calculate_differentiated_overpayment(total_payments, loan_principal):
    overpayment = math.ceil(total_payments - loan_principal)
    print(f"Overpayment = {overpayment}")


def calculate_months_to_repay(loan_principal, annuity_payment, i):
    number_of_months = math.ceil(math.log((annuity_payment / (annuity_payment - i * loan_principal)), 1 + i))
    years, months = divmod(number_of_months, 12)
    plural_years = "s" if years != 1 else ""
    plural_months = "s" if months != 1 else ""
    if years == 0:
        print(f"It will take {months} month{plural_months} to repay this loan!")
    elif months == 0:
        print(f"It will take {years} year{plural_years} to repay this loan!")
    else:
        print(f"It will take {years} year{plural_years} and {months} month{plural_months} to repay this loan!")
    calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_annuity_payment(loan_principal, number_of_months, i):
    annuity_payment = math.ceil(loan_principal * (i * (1 + i) ** number_of_months) / ((1 + i) ** number_of_months - 1))
    print(f"Your annuity payment = {annuity_payment}!")
    calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_loan_principal(annuity_payment, number_of_months, i):
    loan_principal = math.floor(annuity_payment / ((i * (1 + i) ** number_of_months) / ((1 + i) ** number_of_months - 1)))
    print(f"Your loan principal = {loan_principal}!")
    calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_differentiated_payment(loan_principal, number_of_months, i):
    total_payments = 0
    for m in range(1, number_of_months + 1):
        differentiated_payment = math.ceil((loan_principal / number_of_months) + (i * (loan_principal - (loan_principal * (m - 1) / number_of_months))))
        total_payments += differentiated_payment
        print(f"Month {m}: payment is {differentiated_payment}")

    print("")
    calculate_differentiated_overpayment(total_payments, loan_principal)


if __name__ == '__main__':
    try:
        if loan_type == "annuity" and annuity_payment is None:
            calculate_annuity_payment(loan_principal, number_of_months, interest)
        elif loan_type == "annuity" and loan_principal is None:
            calculate_loan_principal(annuity_payment, number_of_months, interest)
        elif loan_type == "annuity" and number_of_months is None:
            calculate_months_to_repay(loan_principal, annuity_payment, interest)
        elif loan_type == "diff":
            calculate_differentiated_payment(loan_principal, number_of_months, interest)

    except KeyboardInterrupt:
        print("The session has been interrupted.")
