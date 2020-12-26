"""
Request via keyboard the amount of products you will buy and the price of each product.

Example:
    Buying 5 toilet paper rolls, and each roll cost 2.50 euros.

Requested calculations:
    - total price of your stock
    - Possible sales; When exceeding 500 euros you get a 10 euro discount.
    - Total 'to pay' price
Print the "to pay" amount with a reasonable text.

Extention:
    Whenever you exceed over 1000, there is a 22 euro discount.
"""


def main():
    cashmere_count = int(input('How many Cashmere toilet paper rolls would you like to buy? '))
    cashmere_price = float(input('How much would you like the  Cashmere toilet paper rolls to cost? '))

    total_price = cashmere_count * cashmere_price

    if 500 <= total_price < 1000:  # Is the same as: total_price >= 500 and total_price < 1000:
        total_price = total_price - 10
    elif total_price >= 1000:
        total_price -= 22

    print(f"Your total will be: {total_price:.2f} Euros.")


if __name__ == '__main__':
    main()
