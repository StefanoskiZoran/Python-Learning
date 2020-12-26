"""
Enter two values, 'a' and 'b',
do the biggest number minus the lowest number.
After that - Multiply that result by 5 and print the output.

Example:
    8 - 5 = 3
    3 x 5 = 15

Disclaimer:
    AVOID DOUBLE CODE!

DEMAND:
    The output has to be the same as the example above.
"""


def main():
    a = int(input('My sire, what value would you like it to be? '))
    b = int(input('My sire, what about value B? '))

    result = 0

    if not(a >= b):
        temp = a
        a = b
        b = temp

    result = a - b
    print(f'{a} - {b} = {result}')
    print(f'{result} x 5 = {result * 5}')


if __name__ == '__main__':
    main()
