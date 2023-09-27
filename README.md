# Loan Calculator
This Python program allows you to calculate differentiated or annuity loans based on user input.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed (the program was written in Python 3.8.3).
3. Run the program by executing `creditcalc.py` in your terminal or IDE of choice.

## Command Line Arguments
```
--type: The type of loan (choices: "diff" for differentiated, "annuity" for annuity).
--principal: The loan principal amount.
--payment: The annuity payment (for annuity loans).
--periods: The number of months.
--interest: The annual interest rate.
```

## Examples
1. Calculating differentiated payments:
```
$ python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
```

2. Calculating how many months it will take to repay the loan:
```
$ python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000
```

3. Calculating the loan principal for a client paying 8,722 per month for 120 months (10 years) at 5.6% interest:
```
python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800019!
Overpayment = 246621
```

4. Calculating the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest
```
python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
```

## Negative cases
1. No loan type selected:
```
$ python creditcalc.py --principal=1000000 --periods=60 --interest=10
usage: creditcalc.py [-h] --type {diff,annuity} [--principal PRINCIPAL] [--payment PAYMENT] [--periods PERIODS] --interest INTEREST
creditcalc.py: error: the following arguments are required: --type
```

2. Invalid loan type used:
```
$ python creditcalc.py --type=none --payment=8722 --periods=120 --interest=5.6
usage: creditcalc.py [-h] --type {diff,annuity} [--principal PRINCIPAL] [--payment PAYMENT] [--periods PERIODS] --interest INTEREST
creditcalc.py: error: argument --type: invalid choice: 'none' (choose from 'diff', 'annuity')
```

3. No interest rate provided:
```
$ python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
usage: creditcalc.py [-h] --type {diff,annuity} [--principal PRINCIPAL] [--payment PAYMENT] [--periods PERIODS] --interest INTEREST
creditcalc.py: error: the following arguments are required: --interest
```

4. Less than four parameters used:
```
$ python creditcalc.py --type=annuity --principal=1000000 --interest=10
Incorrect parameters
```

5. Negative values:
```
$ python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
```
