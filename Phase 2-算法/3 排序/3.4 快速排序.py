"""
快速排序原理（以升序为例）：
1、取一个元素p（第一个元素），使它归位
2、列表被p分成两部分，左边都比p小，右边都比p大
3、递归完成排序
"""
# 写归位函数partition
def partition(li, left, right):
    temp = li[left]                               # 把第一个数取出来存着
    while left < right:                           # 循环退出条件：left和right重合
        while left < right and li[right] > temp:  # 从右边找比temp小的数
            right -= 1                            # 往左走一步
        li[left] = li[right]                      # 把右边值写到左边空位上
        while left < right and li[left] < temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left

li = [2, 4, 1, 6, 5, 3]
partition(li, 0, len(li)-1)
print(li)

# 写快速排序代码
def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)     # 选定的值归位
        quick_sort(li, left, mid-1)          # 对左边部分递归
        quick_sort(li, mid+1, right)         # 对右边部分递归

quick_sort(li, 0, len(li)-1)
print(li)
