"""
递归：函数自己调用自己 并且 有结束条件
当有n个盘子时，汉诺塔怎么玩？
1、把n-1个盘子从A经过C移动到B
2、把第n个盘子从A移动到C
3、把n-1个盘子从B经过A移动到C
"""
def hanoi(n, a, b, c):
    if n > 0:                      # n是盘子个数，n=0说明没有盘子需要移动了
        hanoi(n-1, a, c, b)
        print(f"从{a}移动到{c}")
        hanoi(n-1, b, a, c)

hanoi(3, "A", "B", "C")