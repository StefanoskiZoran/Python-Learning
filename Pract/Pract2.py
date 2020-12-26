def main():
    k = [12, 50, 6]
    replace(k)
    modify(k)


def replace(v):
    v = [55, 12, 34]
    print("v =", v)


def modify(k):
    k.append(33)
    print("k =", k)


if __name__ == '__main__':
    main()