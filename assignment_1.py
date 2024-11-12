def annual_contribution(income_y0, income_growth, annual_spending, year):
    if year == 0:
        return 0
    elif year > 0:
        return (income_y0 * pow(1 + income_growth, year) - annual_spending)


# Asking for input on the needed arguments for the parameters set
age = float(input("How old are you?: "))
income = float(input("What is your annual income today? "))
initial_investment = float(input("How much dollars would you like to deposit as an initial investment amount?: "))
income_growth = float(input("With how much percent do you expect your income to grow annually? Write it in decimals: "))
annual_spending = float(input("How much dollars do you spend annually?: "))
stock_alloc = float(input("How much percent of your portfolio would you like to invest in stocks? Write it in decimals: "))
stock_return = float(input("How much percent do you expect the stock return to be? Write it in decimals: "))
bond_alloc = float(input("How much percent of your portfolio would you like to invest in bonds? Write it in decimals: "))
bond_return = float(input("How much percent do you expect the bond return to be? Write it in decimals: "))
cash_alloc = float(input("How much percent of your portfolio would you like to invest in cash? Write it in decimals: "))
cash_return = float(input("How much percent do you expect the cash return to be? Write it in decimals: "))
wealth_taxrate = float(input("How much percent is the wealth tax rate?: "))
retirement_spending_monthly = 2500
target_withdrawal_rate = 0.04

# Initialization of variables
year = 0
retirement_goal = retirement_spending_monthly * 12 / target_withdrawal_rate
end_capital = initial_investment
list = []
temp_list = []

# Calculating the 
while end_capital < retirement_goal:
    if year == 0:
        cum_deposits_start = initial_investment
    else:
        cum_deposits_start += annual_contribution(income, income_growth, annual_spending, year)
    start_capital = end_capital + annual_contribution(income, income_growth, annual_spending, year)
    cum_returns_start = start_capital - cum_deposits_start 
    roc_before_tax = \
            (start_capital * stock_alloc * (1 + stock_return) \
            + start_capital * bond_alloc * (1 + bond_return) \
            + start_capital * cash_alloc * (1 + cash_return))
    if roc_before_tax <= 0:
        wealth_taxpaid = 0
    elif roc_before_tax > 0:
        wealth_taxpaid = roc_before_tax * wealth_taxrate
    roc_before_tax = roc_before_tax - start_capital
    roc_after_tax = roc_before_tax - wealth_taxpaid
    end_capital = roc_after_tax + start_capital
    temp_list = [(year + age), annual_contribution(income, income_growth, annual_spending, year), start_capital, cum_deposits_start, roc_before_tax, wealth_taxpaid, roc_after_tax, end_capital]
    list.append(temp_list.copy())
    temp_list.clear()
    year += 1

print(f"You can retire at {int(year + age)}")
"""
for item in list:
    print(item)
"""