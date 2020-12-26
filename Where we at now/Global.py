def main():
    count = 0


def show_count():
    print('count')


def set_count(c):
    global count
    count = c


show_count()


if __name__ == '__main__':
    main()