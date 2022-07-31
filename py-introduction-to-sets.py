def average(array):
    # your code goes here

    array_set = set(array)
    average = 0
    for i in array_set:
        average +=i
    return average/len(array_set)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)