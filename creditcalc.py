import argparse
import math
import sys


def parse_arguments():
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

    return parser.parse_args()


def calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal):
    overpayment = math.ceil(annuity_payment * number_of_months - loan_principal)
    print(f"Overpayment = {overpayment}")


def calculate_differentiated_overpayment(total_payments, loan_principal):
    overpayment = math.ceil(total_payments - loan_principal)
    print(f"\nOverpayment = {overpayment}")


def calculate_months_to_repay(loan_principal, annuity_payment, interest):
    number_of_months = math.ceil(math.log((annuity_payment / (annuity_payment - interest * loan_principal)), 1 + interest))
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


def calculate_annuity_payment(loan_principal, number_of_months, interest):
    annuity_payment = math.ceil(loan_principal * (interest * (1 + interest) ** number_of_months) / ((1 + interest) ** number_of_months - 1))
    print(f"Your annuity payment = {annuity_payment}!")
    calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_loan_principal(annuity_payment, number_of_months, interest):
    loan_principal = math.ceil(annuity_payment / ((interest * (1 + interest) ** number_of_months) / ((1 + interest) ** number_of_months - 1)))
    print(f"Your loan principal = {loan_principal}!")
    calculate_annuity_overpayment(annuity_payment, number_of_months, loan_principal)


def calculate_differentiated_payment(loan_principal, number_of_months, interest):
    total_payments = 0
    for month in range(1, number_of_months + 1):
        differentiated_payment = math.ceil((loan_principal / number_of_months) + (interest * (loan_principal - (loan_principal * (month - 1) / number_of_months))))
        total_payments += differentiated_payment
        print(f"Month {month}: payment is {differentiated_payment}")
    calculate_differentiated_overpayment(total_payments, loan_principal)


if __name__ == '__main__':
    args = parse_arguments()
    loan_type = args.type
    loan_principal = args.principal
    annuity_payment = args.payment
    number_of_months = args.periods
    interest = args.interest / (12 * 100)

    if (len(sys.argv) != 5
            or (loan_type == "diff" and annuity_payment is not None)
            or any(val is not None and val <= 0 for val in (loan_principal, number_of_months, interest, annuity_payment))):
        print("Incorrect parameters")

    elif loan_type == "annuity" and annuity_payment is None:
        calculate_annuity_payment(loan_principal, number_of_months, interest)
    elif loan_type == "annuity" and loan_principal is None:
        calculate_loan_principal(annuity_payment, number_of_months, interest)
    elif loan_type == "annuity" and number_of_months is None:
        calculate_months_to_repay(loan_principal, annuity_payment, interest)
    elif loan_type == "diff":
        calculate_differentiated_payment(loan_principal, number_of_months, interest)
