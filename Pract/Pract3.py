def main():
    p = [22, 34, 44]
    modify(p)
    replace(p)


def replace(p):
    b = [35, 77, 89]
    print("b =", b)


def modify(p):
    p.append(35)
    print("p =", p)


if __name__ == '__main__':
    main()