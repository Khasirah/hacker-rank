def gradingStudents(grades):

    ans = []

    for grade in grades:
        if (grade % 5 > 2) and not(grade < 38):
            ans.append(grade + 5 - (grade % 5))
        else:
            ans.append(grade)

    return ans


if __name__ == "__main__":
    grades_count = int(input().strip())
    grades = []

    for i in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    results = gradingStudents(grades)

    for item in results:
        print(item)
