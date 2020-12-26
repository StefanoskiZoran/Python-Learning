import math
import datetime


def main():
    print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
    print("Match constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

    value = 4 * 20
    'The value is {value}'.format(value=value)

    value = 4 * 20
    f'The value is {value}'

    f'The current time is {datetime.datetime.now().isoformat()}'

    f'Math constants: pi={math.pi}, e={math.e}'
    f'Match constants: pi={math.pi:.3f}, e={math.e:.3f}'

    range(5)
    range(0, 5)

    for i in range(5):
        print(i)


if __name__ == '__main__':
    main()
