def main():
    adult_price = 28
    child_price = 15

    adult_count = int(input('How many adults will enter? '))
    child_count = int(input('How many children will enter? '))

    total_people = adult_count + child_count
    total_price = adult_count * adult_price + child_count * child_price

    if total_people >= 15:
        total_price = total_price * 0.9

    print(f"Your total entry fee will be: {total_price} Euros.")


if __name__ == '__main__':
    main()