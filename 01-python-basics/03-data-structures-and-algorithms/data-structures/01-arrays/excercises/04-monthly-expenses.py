import array as arr

"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,
  1. In Feb, how many dollars you spent extra compare to January?
  2. Find out your total expense in first quarter (first three months) of the year.
  3. Find out if you spent exactly 2000 dollars in any month
  4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
  5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
"""
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

expenses = arr.array("i", monthly_expenses)

# 1. In Feb, how many dollars you spent extra compare to January?
jan_expenses = expenses[0]
feb_expenses = expenses[1]
expenditure = feb_expenses - jan_expenses
print(f"Spent ${0 if expenditure <= 0 else expenditure} extra in feb compare to jan.")

# 2. Find out your total expense in first quarter (first three months) of the year.
q1_expenses = sum(expenses[:3])
print(f"First quarter expense: {q1_expenses}")

# 3. Find out if you spent exactly 2000 dollars in any month
try:
    index = expenses.index(2000)
    print(f"Month in which spent exactly $2000: {index}")
except ValueError:
    print("Month in which spent exactly $2000: None")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("Before adding june:", *expenses)
# expenses.insert(5, 1980)
expenses.append(1980)
print("After adding june:", *expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

# april index = 3, update the expense by adding the refunded money

current_april_expense = expenses[3]
refunded_amount = 200

new_april_expense = current_april_expense - refunded_amount

print("Before adding refund:", *expenses)

expenses[3] = new_april_expense

print("After adding redund:", *expenses)
