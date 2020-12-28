"""
Request the weight of an apple in grams, via keyboard.
Create a table that shows 1 to 100 apples with their grams.
example 1 apple = 5 grams, 2 apples = 10 grams, 3 apples = 15 grams etc.

Create this exercise in a for loop and in a while loop.

Is it the for loop best solution or the while loop

"""


def main():
    apple_weight = int(input(f'What is the weight of the apple? '))

    for x in range(1, 101): # for loop when we know how many iterations there will be used
        print("The weight of %d apples is %d" % (x, x*apple_weight))

    count = 1
    while count < 101: # while loop is used when we do not know how many iterations will be used
        print("The weight of %d apples is %d" % (count, count*apple_weight))
        count += 1


if __name__ == '__main__':
    main()