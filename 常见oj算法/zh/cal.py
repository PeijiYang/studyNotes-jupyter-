# 在一个长度为m(m<=12)的数字字符串中插入若干个+-号，使得运算结果为k(k>0)，问有多少种插入方法？
# 例: 字符串“1234”，k = 11
# 则只有12+3－4=11这一种方法，故输出为1

def solve(x:list, cur, res):

    l = len(x)

    for i in range(3):
        if i == 0: