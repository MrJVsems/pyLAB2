
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



print(*compstr(input(), input()), sep=", ")