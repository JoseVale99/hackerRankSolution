

def find_second(n, arr):
    if len(arr) == n:

        return sorted(list(set(arr)))[-2]



if __name__ == '__main__':
    n = int(input())
    
    arr = map(int, input().split())
    print(find_second(n,list(arr)))
  