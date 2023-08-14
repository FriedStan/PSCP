"""Grade III"""


def grader(score):
    """Grade your score"""
    if 95 <= score <= 100:
        grade = 4
    elif 90 <= score < 95:
        grade = 3.5
    elif 85 <= score < 90:
        grade = 3
    elif 80 <= score < 85:
        grade = 2.5
    elif 75 <= score < 80:
        grade = 2
    elif 70 <= score < 75:
        grade = 1.5
    elif 65 <= score < 70:
        grade = 1
    elif 60 <= score < 65:
        grade = 0.5
    elif 0 <= score < 60:
        grade = 0
    else:
        grade = 0
    return grade


def gpa_calc(subject, score_sum):
    """Calculate the average of the grade"""
    return score_sum/subject


def main():
    "Main function"
    score_sum = 0
    subject = int(input())
    for _ in range(subject):
        score_sum += grader(float(input()))
    ans = int((gpa_calc(subject, score_sum) * 100)) / 100
    print("{:.2f}".format(ans))


main()
