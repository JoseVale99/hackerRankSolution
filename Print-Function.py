"""
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values of n.

"""


if __name__ == '__main__':
    n = int(input())
    
    numbers = ""
    i = 1
    while i <=n:
        numbers += str(i)
        i+=1
    print(numbers)