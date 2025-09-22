"""
BONUS_RATE = 0.1
BONUS_RATE_TWO = 0.15
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
BONUS_RATE = 0.1
BONUS_RATE_TWO = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * BONUS_RATE
    else:
        bonus = sales * BONUS_RATE_TWO
    print(bonus)
    sales = float(input("Enter sales: $"))