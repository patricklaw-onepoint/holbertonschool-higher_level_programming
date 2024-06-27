#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    totalScore = 0
    totalWeight = 0
    for t in my_list:
        totalScore += t[0] * t[1]
        totalWeight += t[1]

    if totalWeight == 0:
        return 0

    return totalScore / totalWeight
