def main():
    m = [9, 15, 24]
    modify(m)


def modify(k):
    k.append(39)
    print("k=", k)


if __name__ == '__main__':
    main()