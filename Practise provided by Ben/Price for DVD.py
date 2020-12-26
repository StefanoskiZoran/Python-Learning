"""
Create a program that can calculate the price of a DVD, via keyboard you will be given number of the release year and a rating(Number 1-5).

The basic price of the DVD is always 5 Euros. For a movie that is less than 2 years old you have to pay 1 euro extra.
For movies with a rating of 4 or 5, you pay 2 euros extra.

Print the value of the DVD.
    - For a movie of Rating 2 or 3 you pay 1 euro extra
    - Make sure that the movie can't exceed 7 euros.
    - Make sure the user can't provide faulty ratings, do a test so the number is either between 1 and or 5
"""
import datetime


def main():
    current_year = datetime.datetime.today().year
    base_price = 5
    result = base_price
    dvd_year = int(input('Which year is the movie released? '))

    dvd_rating = int(input('What is the rating of the movie? '))
    while dvd_rating < 1 or dvd_rating > 5:
        dvd_rating = int(input('The rating is invalid, please choose between 1 - 5: '))

    if current_year - dvd_year < 2:
        result += 1

    if dvd_rating == 4 or dvd_rating == 5:
        result += 2
    elif dvd_rating == 2 or dvd_rating == 3:
        result += 1

    if result >= 7:
        result = 7

    print(f"The cost of the DVD is {result:.2f} Euros.")


if __name__ == '__main__':
    main()