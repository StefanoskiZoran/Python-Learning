"""
Request the amount of seconds via keyboard, turn the seconds into months/days/years/decades etc.

"""

def main():
    seconds_request = int(input(f'Please input your desired seconds: '))
    minute_result = 0
    hour_result = 0
    day_result = 0
    month_result = 0
    year_result = 0
    decade_result = 0
    century_result = 0
    millennia_result = 0

    seconds = seconds_request % 60
    minute_result = seconds_request / 60
    minute = minute_result % 60
    hour_result = minute_result / 60
    hour = hour_result % 60
    day_result = hour_result / 24
    day = day_result % 60
    week_result = day_result / 7
    week = week_result % 7
    month_result = day_result / 30
    month = month_result % 30
    year_result = month_result / 12
    year = year_result % 12
    decade_result = year_result / 10
    decade = decade_result % 10
    century_result = decade_result / 10
    century = century_result % 10
    millennia_result = century_result / 10
    millennia = millennia_result % 10

    print(f'{millennia:02.0f}:{century:02.0f}:{decade:02.0f}:{year:02.0f}:{month:02.0f}:{week:02.0f}:{day:02.0f}:{hour:02.0f}:{minute:02.0f}:{seconds:02.0f}')


if __name__ == '__main__':
    main()