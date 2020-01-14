dollarAmount = 18.63

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def cash_to_coins():
    # dollars = int(dollarAmount)
    # cents = dollarAmount - int(dollarAmount)
    
    # quarters = (dollars * 4) + cents % .25
    quarters = (int(dollarAmount) * 4) + int((dollarAmount - int(dollarAmount)) / .25)
    piggyBank["quarters"] = quarters

    initial_change = dollarAmount - (quarters * .25)

    dimes = int(initial_change / .10)
    piggyBank["dimes"] = dimes
    change_after_dimes = initial_change - dimes * .10
    convert_change = round(change_after_dimes * 100)
    nickles = int(convert_change / 5)
    piggyBank["nickels"] = nickles
    pennies = convert_change - nickles * 5
    piggyBank["pennies"] = pennies

cash_to_coins()

print(piggyBank)
