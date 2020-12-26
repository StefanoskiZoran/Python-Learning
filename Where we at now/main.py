def main():
    k = [9, 15, 24]
    modify(k)
    replace(k)
    print("k =", k)


def modify(k):
    k.append(39)
    print("k =", k)


def replace(g):
    g = [17, 28, 45]
    print("g =", g)


def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g =", g)


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")


banner("Sun, Moon and Stars", "*")


banner("Sun, Moon and Stars", border="*")


if __name__ == '__main__':
    main()