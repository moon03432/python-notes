#!/usr/bin/env python3
# coding=utf-8 (for Python 2)

# return: a list of lists. inner list performs intersection, outer list performs union
# for example: [[1,2], [3,4]] means (1 ∩ 2) ∪ (3 ∩ 4)
def union(groups, operators):
    if len(groups) == 1:
        return [groups]
    if len(groups) == 2 and len(operators) == 1:
        if operators[0] == '∪':
            return list([x] for x in groups)
        elif operators[0] == '∩':
            return [groups]

    res_groups = union(groups[0:-1], operators[0:-1])
    if operators[-1] == '∪':
        return res_groups + [[groups[-1]]]
    elif operators[-1] == '∩':
        return list(x+[groups[-1]] for x in res_groups)

    return []

# groups = [1, 2, 3, 4, 5, 6]
# operators = ['∪', '∩', '∪', '∩', '∪']

groups = [1, 2, 3]
operators = ['∩', '∪']

res_groups = union(groups, operators)

print(res_groups)