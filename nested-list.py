"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
"""
if __name__ == '__main__':

    list_score,aux, new_list = [],[],[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_score.append([name, score])
        aux.append(score)
    # order list
    list_score.sort(key=lambda x: x[1])    
    aux = sorted(list(set(aux)))
    
    for name, score in list_score:
        if aux[1] == score:
            new_list.append([name,score])
        new_list.sort(key=lambda x: x[0])
    
    for name, score in new_list:
        print(name)