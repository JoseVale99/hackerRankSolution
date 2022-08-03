if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    n_commands = int(input())

    for i in range(n_commands):

        command = input('').split()

        if 'pop' in command:
            s.pop()
        elif 'remove' in command:
            s.remove(int(command[1]))
        elif 'discard' in command:
            s.discard(int(command[1]))
    
    print(sum(s))
            