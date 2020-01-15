import math

'''
Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.
'''
# 1st way to do cash to coins


dollarAmount = 18.63
piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def cash_to_coins():
    # finds the total number of quarters that can be used for this dollar amount
    quarters = (int(dollarAmount) * 4) + int((dollarAmount - int(dollarAmount)) / .25)
    # puts the number of quarters into the piggy bank
    piggyBank["quarters"] = quarters

    # find the change left now in the dollar amount
    initial_change = dollarAmount - (quarters * .25)

    # finds the total number of dimes that can be used 
    dimes = int(initial_change / .10)
    # puts the number of dimes into the piggy bank
    piggyBank["dimes"] = dimes

    # find the change left now in the dollar amount
    change_after_dimes = initial_change - dimes * .10
    # converts the change to a whole number
    convert_change = round(change_after_dimes * 100)

    # finds the total number of nickels that can be used 
    nickels = int(convert_change / 5)
    # puts the number of nickels into the piggy bank
    piggyBank["nickels"] = nickels

    # finds the total number of pennies that can be used 
    pennies = convert_change - nickels * 5
    # puts the number of pennies into the piggy bank
    piggyBank["pennies"] = pennies

    print(piggyBank)

cash_to_coins()



# 2nd way to do cash to coins
def make_change():
    dollar_amount = 8.69
    piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
    }
    piggyBank["quarters"] = math.floor(dollar_amount / .25)
    dollar_amount = dollar_amount % .25

    piggyBank["dimes"] = math.floor(dollar_amount / .10)
    dollar_amount = dollar_amount % .10

    piggyBank["nickels"] = math.floor(dollar_amount / .05)
    dollar_amount = dollar_amount % .05

    piggyBank["pennies"] = math.ceil(dollar_amount / .01)

    print(piggyBank)

make_change()