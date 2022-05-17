dict = {'1': '', '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


def func(list):
    if '1' in list:
        list.remove('1')
    if '0' in list:
        list.remove('0')


    a = dict.get(f'{list[0]}')
    for q in range(len(list) - 1):
        n = len(a)
        for w in range(n):

            b = a.pop(0)

            for e in dict.get(f'{list[q + 1]}'):
                a.append(e + b)

    print(a)
    print(len(a))


print('请输入0-9的字符串')
list = list(str(input()))
func(list)
