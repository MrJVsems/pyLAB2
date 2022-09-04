
def compstr(str1, str2):
    ans = []
    strMax = str1 if len(str1) >= len(str2) else str2
    strMin = str1 if len(str1) < len(str2) else str2
    for i in range(len(strMax)-1):
        podstr = strMax[i:i+2]
        if podstr in strMin:
            ans.append(podstr)
    print(f'Количество совпадений - {len(ans)}')
    return ans


# исключая одинаковые подстроки
def compstr_v2(str1, str2):
    mnoz1 = set([str1[i:i+2] for i in range(len(str1)-1)])
    mnoz2 = set([str2[i:i+2] for i in range(len(str2)-1)])
    itog = mnoz1 & mnoz2
    print(f'Количество совпадений - {len(itog)}')
    return itog


a, b = input(), input()
print(*compstr(a, b), sep=", ")
print(*compstr_v2(a, b), sep=", ")