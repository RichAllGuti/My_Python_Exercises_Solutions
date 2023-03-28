"""
You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. 
With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

The function must return the numeric value of the balance years that will pass the specifict threshold.
"""
def calculate_balance_deposit_profit(deposit, rate, threshold):
    
    # Just initialize varables to use later
    balance = deposit
    years = 0

    # Iterate until the balance exceeds the treshold
    while balance < threshold:

        # Calculate the increase, in the balance based on the growth rate.
        increase = balance * (rate/100)

        # 
        balance += increase

        #
        years += 1
    
    return years

deposit = 100 
rate = 20
threshold = 170

print(calculate_balance_deposit_profit(deposit, rate, threshold))

