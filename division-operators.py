"""
The provided code stub reads two integers, a and b, from STDIN.
add logic to print three lines. The first line should contain the result of a/b.
The second line should contain the result of a%b. The third line should contain the result of a//b.
No rounding or formatting is necessary.
Example
Input:
3
5
Output:
0
0.6
"""



if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)