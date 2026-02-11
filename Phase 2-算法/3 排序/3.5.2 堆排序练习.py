# 向下调整函数
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[i]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp
    return li

# 建堆
def heap_sort(li):
    n = len(li)
    for i in range((n-2) // 2, -1, -1):
        sift(li, i, n-1)
    for i in range(n-1, 0, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)
    return li

li = [3,5,6,2,1,0,9,7,8,4]
print(heap_sort(li))
