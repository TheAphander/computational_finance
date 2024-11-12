import numpy as np
import pandas as pd
# Given parameters

def annual_contribution(income_y0, income_growth, annual_spending, year):
    if year == 0:
        return 0
    elif year > 0:
        return (income_y0 * pow(1 + income_growth, year) - annual_spending)
'''
#Collecting the arguments for the parameters from the user
deposit_y0 = float(input("How much dollars would you like to deposit as an initial investment amount?: "))
income_y0 = float(input("What is your annual income today>: "))
income_growth = float(input("With how much percent do you expect your income to grow annually? Write it in decimals: "))
annual_spending = float(input("How much dollars do you spend a month?: "))
age = float(input("How old are you?: "))
stock_alloc = float(input("How much percent of your portfolio would you like to invest in stocks? Write it in decimals: "))
stock_return = float(input("How much percent do you expect the stock return to be? Write it in decimals: "))
bond_alloc = float(input("How much percent of your portfolio would you like to invest in bonds? Write it in decimals: "))
bond_return = float(input("How much percent do you expect the bond return to be? Write it in decimals: "))
cash_alloc = float(input("How much percent of your portfolio would you like to invest in cash? Write it in decimals: "))
cash_return = float(input("How much percent do you expect the cash return to be? Write it in decimals: "))
wealth_taxrate = float(input("How much percent is the wealth tax rate?: "))
#There should be a validation function to check if it is a percentage, if the allocation amounts are 100% or 1.00 summed up etc. I should also define if it should be in decimals or percentages. 
'''

deposit_y0 = float(25000)
income_y0 = float(60000)
income_growth = float(0.01)
annual_spending = float(45000)
age = float(20)
stock_alloc = float(.80)
stock_return = float(0.081)
bond_alloc = float(0.18)
bond_return = float(0.024)
cash_alloc = float(0.02)
cash_return = float(0)
wealth_taxrate = float(.15)

year = 0
end_capital = deposit_y0
dataset = [["Age", "Capital Deposited", "Return on Capital", "Tax Paid (total)", "Total Asset Value"]]
cum_capital_deposited = deposit_y0
cum_capital_return = 0
tax_paid = 0
while (year + age) < 60: #this condition should be changed to the goal of the retirement (or maybe not)
    start_capital = end_capital + annual_contribution(income_y0, income_growth, annual_spending, year)
    cum_capital_deposited += annual_contribution(income_y0, income_growth, annual_spending, year)
    end_capital_excl_tax = (start_capital * stock_alloc * (1 + stock_return) + start_capital * bond_alloc * (1 + bond_return) + start_capital * cash_alloc * (1 + cash_return))
    if (end_capital_excl_tax - start_capital) <= 0:
        end_capital_incl_tax = end_capital_excl_tax
    else:
        end_capital_incl_tax = end_capital_excl_tax - (end_capital_excl_tax - start_capital) * wealth_taxrate
    list = [(year + age), cum_capital_deposited, cum_capital_return, tax_paid, end_capital_incl_tax]
    dataset.append(list)
    cum_capital_return = end_capital_incl_tax - start_capital
    tax_paid += end_capital_excl_tax - end_capital_incl_tax
    list = []
    year += 1

df = pd.DataFrame(np.array(dataset))
print(df)

# df.to_csv('compfin_v1.csv', index=False)