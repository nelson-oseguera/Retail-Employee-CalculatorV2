# Nelson Oseguera

# March 9th, 2023
 
# Project 3

# This program will ask the user to input information of a stores monthly sales, and the sales increased percentage. Based on what amount is entered, the program will then output a bonus amount for the store and the employees based on what goals were meant.

# Variables: Real monthlySales, Real storeAmount, Real empAmount, and Real salesIncrease

# Welcome statement

print('Welcome to the program')

# Ask the user (prompt the user) to enter the data needed in this program.

monthlySales=float(input('Enter the monthly sales $'))

# Ask the necessary code to allow the user to input sales increase.

salesIncrease=float(input('Enter percent of sales increase in decimal format. For example 4% should be entered as .04: '))

# Determine the storeAmount bonus

if monthlySales>=110000:
    storeAmount=6000

elif monthlySales>=100000:
    storeAmount=5000

elif monthlySales>=90000:
    storeAmount=4000

elif monthlySales>=80000:
    storeAmount=3000

else:
    storeAmount=0

# Determine the empAmount bonus

if salesIncrease>=.05:
    empAmount=75

elif salesIncrease>=.04:
    empAmount=50

elif salesIncrease>=.03:
    empAmount=40

else:
    empAmount=0

# Add the statements to show all output to the console.

print('The store bonus amount is $', storeAmount)

print('The employee bonus amount is $', empAmount)

if storeAmount==6000 and empAmount==75:
    print('Congrats! You have reached the highest bonus amounts possible!')
