def annual_contribution(income_y0, income_growth, annual_spending, year):
    if year == 0:
        return 0
    elif year > 0:
        return (income_y0 * pow(1 + income_growth, year) - annual_spending)


# Asking for input on the needed arguments for the parameters set
year = 0
age = 20
initial_investment = 25000 
end_capital = 0
cum_deposits_start = 0
roc_before_tax = 0
wealth_taxpa = 0
roc_after_tax = 0
income = 60000
income_growth = 0.01
annual_spending = 45000
stock_alloc = 0.8
stock_return = 0.081
bond_alloc = 0.18
bond_return = 0.024
cash_alloc = 0.02
cash_return = 0
wealth_taxrate = 0.15

# Calculating the investment returns, deposits, paid taxed etc.
end_capital = initial_investment
while year < 2:
    if year == 0:
        cum_deposits_start = initial_investment
    else:
        cum_deposits_start += annual_contribution(income, income_growth, annual_spending, year)
    start_capital = end_capital + annual_contribution(income, income_growth, annual_spending, year)
    cum_returns_start = start_capital - cum_deposits_start 
    roc_before_tax = \
            (start_capital * stock_alloc * (1 + stock_return) \
            + start_capital * bond_alloc * (1 + bond_return) \
            + start_capital * cash_alloc * (1 + cash_return)) \
            - start_capital
    if roc_before_tax <= 0:
        wealth_taxpaid = 0
    elif roc_before_tax > 0:
        wealth_taxpaid = roc_before_tax * wealth_taxrate
    roc_after_tax = roc_before_tax - wealth_taxpaid
    end_capital = roc_after_tax + start_capital
    print(f"year: {year}, cum_deposits_start: { cum_deposits_start}, start_capital: {start_capital}, cum_returns_start: {cum_returns_start}, roc_before_tax: {roc_before_tax}, wealth_taxpaid: {wealth_taxpaid}, roc_after_tax: {roc_after_tax}, end_capital: {end_capital}")
    year += 1


# calculating the retirement amount needed