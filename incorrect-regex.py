"""
Your task is to find out whether  is a valid regex or not.
"""
import re
if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        try:
            print(bool(re.compile(s)))
        except:
            print('False')
