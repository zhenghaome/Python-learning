"""
查找：在一些数据元素中，通过一定方法找出与给定关键字相同的数据元素的过程
顺序查找：从列表中找指定元素
输入：列表，待查找元素
输出：找到的元素下标（没找到时一般返回None或者-1）
内置顺序查找函数：index()
"""
def linear_search(li, val):
    for i in range(len(li)):
        if li[i] == val:
            return i
    else:
        return None

n = linear_search([1, 2, 3, 4], 3)
print(n)

# 上面这个算法的时间复杂度：O(len(li))