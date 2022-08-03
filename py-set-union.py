if __name__ == '__main__':

    n = int(input())
    set_English = set(map(int, input().split()))
    n = int(input())
    set_Frances = set(map(int, input().split()))
    set_general = set().union(set_English,set_Frances)   
    print(len(set_general))
