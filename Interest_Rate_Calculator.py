def main():
    print("This is Ballershopke monthly Payment Loan Calculator")
    print("")


    principal = float(input("Enter the Loan amount: "))
    apr= float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))



    monthly_interest_rate= apr/1200
    amount_of_months= years*12
    monthly_payment= principal * monthly_interest_rate/ (1-(1+ monthly_interest_rate) ** (-amount_of_months))



    print("The monthly payment for this loan is : ", monthly_payment)

main()
