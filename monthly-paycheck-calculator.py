# define a function that does the commission calculation
# if the dollar ammount of sales is between $10000 and $100000 the commission is 2% of the sale
# if the dollar ammount of sales is between $100001 and $500000 the commission is 15% of the sale
# if the dollar ammount of sales is between $500001 and $1000000 the commission is 28% of the sale
# if the dollar ammount of sales is great than $1000000 the commission is 35% of the sale
def commission_ammount(sales):
    if sales >= 10000 and sales <= 100000:
        commission = 0.02 * sales
    elif sales >= 100001 and sales <= 500000:
        commission = 0.15 * sales
    elif sales >= 500001 and sales <= 1000000:
        commission = 0.28 * sales
    elif sales > 1000000:
        commission = 0.35 * sales
    else:
        commission = 0
    return(commission)
# define the function that calculates the bonus
# Only the employeees that worked for the company for 3 months and their sale was at least 100001 receive a bonus
def bonus_ammount(month, sales):
    if month >= 3:
        if sales >= 100001 and sales <= 500000:
            bonus = 1000
        elif sales >= 500001 and sales <= 1000000:
            bonus = 5000
        elif sales > 1000000:
            bonus = 100000
        else:
            bonus = 0
    else:
        bonus = 0
    return(bonus)
# main function, asks the user for input
base_pay = 2000
AddionalBonus = 1000
deduction = 200
name = input("Enter your name: ")
month = float(input("Enter the numer of months that you worked: "))
vacation = float(input("Enter the number of days you took off: "))
sales = float(input("Enter the dollar amount of sales you made: "))
# Calls out the commission function and prints the results
print("Hello ", name)
print("You have been with the company for ", month, "months")
print("Your commission is $",commission_ammount(sales))
print("Your base salary is $",base_pay,)
# Employees that have been with the company more than 5 years will
# receive an additional $1000 bonus
if month > 60 and sales > 100000:
    Final_bonus = bonus_ammount(month, sales) + AddionalBonus
    print("Your additional bonus is $",AddionalBonus)
else:
    Final_bonus = bonus_ammount(month, sales)
print("Your final bonus is $",Final_bonus)
# if employee takes more than 3 days off work in a month their 
# paycheck will reduce by 200
if vacation > 3:
    pay_check = commission_ammount(sales) + Final_bonus + base_pay - deduction
    print("Your paycheck deduction is $",deduction)
else:
    pay_check = commission_ammount(sales) + Final_bonus + base_pay
print("Your total gross pay is $",pay_check)








