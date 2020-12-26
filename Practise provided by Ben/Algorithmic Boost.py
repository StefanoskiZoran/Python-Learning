def main():
    adult_price = 28
    children_price = 15

    adult_count = int(input('How many adults will enter? '))
    children_count = int(input('How many children will enter? '))

    total_price = adult_count * adult_price + children_count * children_price
    print(total_price)


if __name__ == '__main__':
    main()