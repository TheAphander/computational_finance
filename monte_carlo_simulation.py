import numpy as np

def random_daily_return(daily_expected_return, daily_volatility):
    return (daily_expected_return + daily_volatility * np.random.normal(0, 1))

initial_investment_value = 1000
annual_expected_return = .10
annual_volatility = 0.20
trading_days = 252

daily_expected_return = annual_expected_return / trading_days
daily_volatility = annual_volatility / np.sqrt(trading_days)

i = 0
z = 0
list = []
temp_list = []
while z < 5:
    while (i < 3):
        if len(temp_list) == 0:
            temp_list.append(initial_investment_value)
        else:
            new_value = temp_list[i - 1] * (1 + random_daily_return(daily_expected_return, daily_volatility))
            temp_list.append(new_value)
        i += 1
    list.append(temp_list.copy())  
    temp_list.clear()  
    z += 1
    i = 0

print(list)