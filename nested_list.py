'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''


if __name__ == '__main__':
    students= {}; names= [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name]= score
    
    sortedScores= list(sorted(students.values()))
    
    for i in range(1, len(sortedScores)):
        if sortedScores[i] > sortedScores[i-1]:
            second= sortedScores[i]
            break
    
    for key, value in students.items():
        if value == second:
            names.append(key)
    
    for _ in sorted(names):
        print(_)