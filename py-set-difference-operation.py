if __name__ == '__main__':
    n = int(input())
    student_english = list(map(int, input().split()))
    n = int(input())
    student_French = list(map(int, input().split()))

    # data = set(student_english)

    print(len(set(student_english).difference(student_French)))