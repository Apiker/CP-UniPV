# IRPEF 2024 
#
# Compute the taxes given the annual income
# (IRPEF 2024 Italian physical persons tax)
#
#            IRPEF 2024
# Income                         tax rate
# up to 28000                       23%
# from 28001 up to 50000 euros      35%
# above 50000 euros                 43%


print('IRPEF 2024 computation')
income = input('Please insert the income: ')
income = int(income)

if income < 0:
    # income cannot be negative
    print('Warning: income cannot be negative')
    legal_income = True
else:
    if 0 <= income <= 28000:
        tax_rate = 23/100
        bottom = 0
        marginal_income = income
    elif 28000 < income <= 50000: # could be just: income <= 50000
        tax_rate = 35/100
        bottom = 28000*23/100
        marginal_income = income-28000
    elif income > 50000:
        tax_rate = 43/100
        bottom = 28000*23/100+ (50000-28000)*35/100
        marginal_income = income-50000    

    tax = marginal_income * tax_rate + bottom
    print('The tax amount is', tax)
    
