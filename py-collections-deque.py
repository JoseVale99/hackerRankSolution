from collections import deque
if __name__ == '__main__':
    n = int(input())

    d = deque()
    for i in range(n):
        methods = input().split()

        if 'append' in methods:
            d.append(int(methods[1]))
        elif 'appendleft' in methods:
            d.appendleft(int(methods[1]))
        elif 'pop' in methods:
            d.pop()
        elif 'popleft' in methods:
            d.popleft()
    print(*d)