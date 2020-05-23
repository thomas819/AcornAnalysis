# 수식을 통한 분산 ,표준편차
grades = [1, 3, -2, 4]


def show_grades(grades):
    for g in grades:
        print(g, end=' ')


show_grades(grades)


def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
    return tot


print("합은", grades_sum(grades))


def grades_ave(grades):
    tot = grades_sum(grades)
    ave = tot / len(grades)
    return ave


print("평균은", grades_ave(grades))


def grades_variance(grades):
    ave = grades_ave(grades)
    vari = 0
    for su in grades:
        vari += (su - ave) ** 2
    return vari / len(grades)  # return vari / len(grades) - 1


print('분산은', grades_variance(grades))


def grades_std(grades):
    return grades_variance(grades) ** 0.5


print('표준편차는,', grades_std(grades))

# numpy

import numpy as np

print('합은', np.sum(grades))
print('평균은', np.average(grades))  # =mean
print('분산은', np.var(grades))
print('표준편차', np.std(grades))
