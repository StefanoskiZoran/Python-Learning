"""
Request the amount of seconds via keyboard, turn the seconds into months/days/years/decades etc.

"""

def main():
    value = int(input(f'Please input your desired seconds: '))
    seconds = value % 60
    minutes = value / 60 % 60
    hours = value / 60 / 60 % 24
    days = value / 60 / 60 / 24 % 7
    weeks = value / 60 / 60 / 24 / 7

    print(f"{weeks:02.0f}:{days:02.0f}:{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")


if __name__ == '__main__':
    main()