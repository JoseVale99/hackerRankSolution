# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.


def print_formatted(number):
    width=len(bin(number))-2
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)