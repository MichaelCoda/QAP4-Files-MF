# A program designed to Calculate insurance policy information for customers.
# Michael Fewer
# Nov-19-2023

import datetime

# Defining Constants 
POLICY_NUM = 1944.00
BASIC_PREMIUM = 869.00
DISCOUNT_CARS = .25
LIA_COVERAGE = 130.00
GLASS_COVERAGE = 86.00
LOANER_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
PREVIOUS_CLAIMS = [4500, 9000, 1750]

# Creating lists for input validation
province_validation = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
fm_validation = ["F", "M"]
# Main Program Loop
# Recieving Customer information
while True:
    print()
    first_name = input("Enter your first name: ").title()
    last_name = input("Enter your last name: ").title()
    address = input("Enter your address: ").title()
    city = input("Enter your city: ").title()
    province = input("Enter your province (XX): ").upper()

    # Validating province input
    while True:
        if province not in province_validation:
            province = input("Enter a valid province (XX)").upper()
        elif province in province_validation:
            break
            
    # Recieving user input
    postal_code = input("Enter your Postal Code: ").upper()
    phone_num = input("What is your phone number?: ")
    cars_insured = (int(input("Enter amount of cars insured: ")))
    extra_liability = input("Would you like extra liability UP TO $1,000,000? (Enter Y or N): ").upper()
    extra_glass = input("Would you like extra glass? (Enter Y or N): ").upper()
    loaner_option = input("Would you like extra loaner vehicle (Enter Y or N): ").upper()
    full_or_monthly = input("Pay in full or monthly payment plan (F,M: )").upper()

    # Validating payment input
    while full_or_monthly not in fm_validation :
        full_or_monthly = input("Enter a valid payment option (F/M)").upper()
    
       

    # Determining the down payment amount
    if full_or_monthly == 'F':
        downp_amount = 0
    elif full_or_monthly == 'M':
        downp_amount = float(input("Enter amount of down payment: "))
    
    customer_date = datetime.datetime.now()
    prev_claim_cost = sum(PREVIOUS_CLAIMS)

    # Calculating extra costs
    total_extra_costs = (cars_insured - 1) * BASIC_PREMIUM * DISCOUNT_CARS

    if extra_liability == 'Y':
        total_extra_costs += cars_insured * LIA_COVERAGE

    if extra_glass == 'Y':
        total_extra_costs += cars_insured * GLASS_COVERAGE

    if loaner_option == 'Y':
        total_extra_costs += cars_insured * LOANER_COVERAGE

    total_insurance_premium = BASIC_PREMIUM + total_extra_costs
    total_hst = total_insurance_premium * HST_RATE
    total_cost = total_insurance_premium + total_hst

   # Calculating monthly payment
    monthly_payment = total_cost + PROCESSING_FEE / 8
    if downp_amount > 0:
        monthly_payment = (total_cost - downp_amount) + PROCESSING_FEE / 8


    # Displaying receipt
    print("\nReceipt:")
    print("------------------------------------------------")
    print(f"Policy Number: {POLICY_NUM}")
    print(f"Customer Name: {first_name} {last_name}")
    print(f"Address: {address}, {city}, {province} {postal_code}")
    print(f"Phone Number: {phone_num}")
    print(f"Number of Cars: {cars_insured}")
    print(f"Extra Liability Coverage: {extra_liability}")
    print(f"Extra Glass Coverage: {extra_glass}")
    print(f"Loaner Car Coverage: {loaner_option}")
    print(f"Payment Plan: {full_or_monthly}")
    print(f"Down Payment: ${'{:,.2f}'.format(downp_amount)}" if downp_amount > 0 else "")
    print("\nPremium Details:")
    print(f"Basic Premium: ${'{:,.2f}'.format(total_insurance_premium)}")
    print(f"HST ({HST_RATE * 100}%): ${'{:,.2f}'.format(total_hst)}")
    print(f"Total Cost: ${'{:,.2f}'.format(total_cost)}")
    print(f"Monthly Payment: ${'{:,.2f}'.format(monthly_payment)}" if monthly_payment > 0 else "")
    print("\nInvoice Date:", customer_date.strftime("%Y-%m-%d"))
    print(f"--------------------------------------------------")

    # Display previous claims
    print("\nPrevious Claims:")
    print("-----------------")
    print("Claim #  Claim Date    Amount")
    print("-----------------------------")
    for i, claim_amount in enumerate(PREVIOUS_CLAIMS, start=1):
        claim_date = customer_date.strftime("%Y-%m-%d")  
        print(f"{i}.     {claim_date}   ${'{:,.2f}'.format(claim_amount)}")

    # Ask if the user wants to continue.
    another_customer = input("\nDo you want to enter information for another customer? (Y or N): ").upper()
    if another_customer != 'Y':
        break
    
   
