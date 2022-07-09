""" 
The provided code stub reads and integer, a, from STDIN. For all non-negative integers i < n, print i^2
"""


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)
"""
Solution #2
if __name__ == '__main__':
    n = int(input())

    count = 0
    while count < n:
        print(count ** 2)
        count += 1
"""