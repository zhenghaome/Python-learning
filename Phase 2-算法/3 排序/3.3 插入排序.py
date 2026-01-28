# 插入排序：随便摸一个数，按照大小顺序插入手里已经有的数中，以此类推
def insert_sort(li):
    for i in range(1, len(li)):          # i表示摸到的数的下标
        temp = li[i]
        j = i-1                          # j表示手里的数的下标
        while j >= 0 and li[j] > temp:   # 注意：循环走到头了也不交换，这个容易漏
            li[j+1] = li[j]
            j -= 1
        li[j+1] = temp
    print(li)

insert_sort([2, 4, 1, 5, 3])

