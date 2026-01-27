def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print(li)

# 优化：如果一趟结束没有排序，说明本身就是排好序的，可以直接结束算法
def bubble_sort2(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return

bubble_sort([2, 4, 1, 6, 5])
bubble_sort2([1, 2, 3, 4, 5])

