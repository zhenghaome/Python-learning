"""
一、树的概念
1、概念：树是一种可以由递归定义的数据结构
2、根节点
   叶子节点：下面没有分叉的节点
3、树的深度（高度）：一共有几层
4、节点的度：分的叉的个数
   树的度：最大的节点的度
5、父节点/子节点/子树
二、二叉树
1、概念：度不超过2的树（每个节点最多两个子节点）
2、满二叉树：每一层的节点数都达到最大值
3、完全二叉树：叶节点只出现在最下层和次下层，并且最下层的节点都集中在该层最左边的若干位置
三、二叉树的存储方式——顺序存储方式
二叉树在python中按照从上到下，从左到右的顺序，存成一个列表
父节点下标为 i ：左子节点下标为 2i+1，右子节点下标为 2i+2
子节点下标为 i ：父节点下标为 (i-1) // 2
四、堆
1、概念：一颗特殊的完全二叉树
2、分类  大根堆：任一节点都比其子节点大
        小根堆：任一节点都比其子节点小
3、向下调整：当根节点的左右子树都是堆，但自身不是堆时，可以向下调整成一个堆
"""

## 向下调整函数（以大根堆为例）
def sift(li, low, high):   # low 是根节点下标，high 是最后一个节点下标
    i = low   # i最开始是根节点
    j = 2 * i + 1   # j最开始是i的左子节点
    temp = li[i]   # 把堆顶存起来
    while j <= high:   # 只要j指的还有数字就一直循环
        if j+1 <= high and li[j+1] > li[j]:   # 如果右子节点还有且比左边大
            j = j+1   # j就指向右子节点（不是交换左右子节点）
        if li[j] > temp:   # 如果子节点的值大于temp
            li[i] = li[j]   # 就把子节点往上提拔
            i = j
            j = 2 * i + 1   # 往下看一层
        else:   # 如果temp的值大于子节点
            break   # 退出循环
    li[i] = temp   # 把temp放到当前j所在的根节点上


## 建堆：农村包围城市法，从最后一个非叶子节点开始建
def heap_sort(li):
    n = len(li)
    for i in range((n-2) // 2, -1, -1):   # 从最后一个非叶子节点（最后一个节点去找父亲即可）开始，往上面的根节点循环
        sift(li, i, n-1)   # low(i)是根节点下标，high理论上应该是当前小堆的最后一个节点下标，但是不好找，用大堆的high也是一样的
    # 建堆完成
    ## 出数：已经有了一个大堆，只需要挨个儿出数就能排序
    for i in range(n-1, 0, -1):   # i一直指当前堆的最后一个元素，且最后一次不用比
         li[i], li[0] = li[0], li[i]   # 堆顶拿下来放到最后一个位置上
         sift(li, 0, i-1)   # 重新调整剩下的堆（i这时候还没有变，所以high是i-1而不是i）
    return li

li = [3,5,1,7,9,4,6,0,2,8]
heap_sort(li)
print(li)
# 时间复杂度：nlogn


## 堆排序内置模块
import heapq
import random

li = list(range(100))
random.shuffle(li)

heapq.heapify(li)   # 建堆（建的是小根堆）

n = len(li)
for i in range(n):
    print(heapq.heappop(li), end=' , ')   # heappop每次往外蹦最小数，所以要循环n次

my_heap = []
heapq.heappush(my_heap, 10)   # 往堆里添加元素，并且会自动建成小根堆
heapq.heappush(my_heap, 2)
heapq.heappush(my_heap, 4)
print(my_heap)