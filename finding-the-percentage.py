
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = 0
    for name in student_marks:
        if query_name in student_marks:
            average = sum(student_marks.get(query_name))/len(student_marks.get(query_name))
            print(format(average,'.2f')) 
            break
