Name: Dave Iregha
 Course: COS102
 Assignment: Personal Income Tax Calculator (2009 Rates)

def calculate_tax(status, income):
    tax = 0.0

    # Tax brackets for each filing status
    if status == 0:  # Single
        limits = [8350, 33950, 82250, 171550, 372950]
        rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    elif status == 1:  # Married filing jointly
        limits = [16700, 67900, 137050, 208850, 372950]
        rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    elif status == 2:  # Married filing separately
        limits = [8350, 33950, 68525, 104425, 186475]
        rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    elif status == 3:  # Head of household
        limits = [11950, 45500, 117450, 190200, 372950]
        rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    else:
        print("Invalid filing status.")
        return

    previous_limit = 0

    for i in range(len(limits)):
        if income > limits[i]:
            tax += (limits[i] - previous_limit) * rates[i]
            previous_limit = limits[i]
        else:
            tax += (income - previous_limit) * rates[i]
            break
    else:
        tax += (income - previous_limit) * rates[-1]

    return tax


 MAIN PROGRAM 
print("Personal Income Tax Calculator (2009)")
print("0 - Single")
print("1 - Married Filing Jointly")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Enter your filing status (0-3): "))
income = float(input("Enter your taxable income: "))

total_tax = calculate_tax(status, income)

if total_tax is not None:
    print(f"Your total tax is: ${total_tax:.2f}"
