def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a


def main():
    a = int(input("输入第一个数:"))
    b = int(input("输入第二个数:"))
    common_factor = gcd(a, b)
    print("两个数的比值是:", int(a/common_factor), ":", int(b/common_factor))


if __name__ == '__main__':
    main()