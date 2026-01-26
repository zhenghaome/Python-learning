# 从列表中找到最小的，把最小的放在无序区第一个
# 算法关键点：无序区最小数的位置
def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i, len(li)):
            if li[j] < li[i]:               # 如果li[j]小，那就放在第一个
                li[j], li[i] = li[i], li[j]
        print(li)

select_sort([1, 2, 4, 5, 3])


