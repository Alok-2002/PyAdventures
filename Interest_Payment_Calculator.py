def Loan_Calculator():
    print("----Welcome To Loan Calculator-----")
    print(" ")
    
    principal = float(input("Enter The Loan Amount: "))
    annual_interest_rate = float(input("Enter The Annual Interest Rate: "))
    years = int(input("Input Amount Of Years: "))
    
    monthly_interest_rate = annual_interest_rate / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-amount_of_months))
    
    print("The Monthly Payment For This Loan Is:₹ %.2f "% monthly_payment)

Loan_Calculator()