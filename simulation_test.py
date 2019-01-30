# noises
import numpy as np
import random
phase_initial = 1

# each month calculate the
daily_interest = (0.065/365)
salary = 2500
initial_debt = 69000
initial_savings = 0
pay_cycle = 14
fixed_expenses = 2000 #biweekly
savings_rate = 0
min_savings = salary * savings_rate
current_debt = initial_debt
current_savings = initial_savings 
accumulated_interest = 0
count = 0
while ((current_savings) < 20000): 
    noise_expenses = random.randrange(100,200,10)
    bi_wkly_expenses = fixed_expenses + noise_expenses
    remainder = salary - bi_wkly_expenses - min_savings
    max_debt_contribution = remainder*0.75
    max_additional_salary = remainder*0.25
    debt_flux = (current_debt+current_debt*(daily_interest*pay_cycle))- max_debt_contribution
    if debt_flux < 0:
        current_savings+= max_debt_contribution
        debt_flux = 0
    current_debt = debt_flux
    current_savings += min_savings + max_additional_salary
    accumulated_interest += initial_debt*(daily_interest*pay_cycle)
    print(f' In  {((count+1) * pay_cycle)/365} years and you will have')
    print(f'accumulated interest: {accumulated_interest}')
    print(f'new updated savings: {current_savings}')
    print(f'remaining debt: {current_debt}')
    count += 1
