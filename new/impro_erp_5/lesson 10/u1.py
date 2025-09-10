""" U1 """
"""
a) Ndërtoni një funksion i cili merr ka si parametër n
   që është sasia e numrave që do të marrë nga përdoruesi
   dhe krijon me to një listë.
b) Ndëtoni një funksion i cili ruan një një file json
    listën me numra, shumën, sasinë e elementëve
    dhe mesataren e numrave të listës si më poshtë:

shembull:
lst = [10, 7, 3, 1, 9]

json:
{
    "list": [10, 7, 3, 1, 9],
    "sum": 30,
    "len": 5,
    "avg": 6
}
"""
import json


def create_lst(n):
    lst = []
    for i in range(n):
        el = int(input(f'el {i + 1}: '))
        lst.append(el)
    return lst


def save_json(lst):
    s = sum(lst)
    n = len(lst)
    res = {
        "list": lst,
        "sum": s,
        "len": n,
        "avg": s / n,
    }
    with open("data/u_1.json", "w") as f:
        json.dump(res, f)


l = create_lst(5)
save_json(l)
