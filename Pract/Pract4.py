def main():
    print(formatvalue_Type1("Ben", 25))
    print(formatvalue_Type1("Ben", 25))


def formatvalue_Type1(name, age):
    return "The age of {} is {}.".format(name, age)


def formatvalue_Type2(name, age):
    return "The age of {name} is {age}.".format(name=name, age=age)


if __name__ == '__main__':
    main()