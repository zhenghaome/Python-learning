"""
Top k 问题：在一堆数中取前k大/小的数
思路：
1、排序后切片（nlogn + k，+k可以忽略）
2、lowB 三人组（nk）
3、堆排序（nlogk）
堆排序思路：
取列表中前 k 个数建立一个小根堆
用后面的元素依次和堆顶比较，如果比堆顶大，就换上来（下面的元素肯定都比堆顶大，要是还有比堆顶大的，那堆顶肯定不是前 k 大了）
得到前 k 大的元素
"""

## 向下调整函数（小根堆）
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[i]
    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:   # 如果右子节点还有且比左边小
            j = j+1   # j就指向右子节点（不是交换左右子节点）
        if li[j] < temp:   # 如果子节点的值小于temp
            li[i] = li[j]   # 就把子节点往上提拔
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = temp


## topk函数
def topk(li, k):
    # 建堆
    heap = li[0: k]
    for i in range((k-2) // 2, -1, -1):
        sift(heap, 0, k-1)
    # 遍历比较
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 出数
    for i in range(k-1, 0, -1):
         heap[i], heap[0] = heap[0], heap[i]
         sift(heap, 0, i-1)
    return heap

li = [3,5,1,7,9,4,6,0,2,8]
print(topk(li, 3))
