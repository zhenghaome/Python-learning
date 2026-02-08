import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['a', 'b', 'c', 'd'])   # 全是0
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['a', 'b', 'c', 'd'])   # 全是1
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['a', 'b', 'c', 'd'])   # 全是2

## concat合并
result1 = pd.concat([df1, df2, df3])   # concat默认上下合并

# 修改行索引
result2 = pd.concat([df1, df2, df3], ignore_index = True)

# join
df4 = pd.DataFrame(np.ones((3,4))*0, index = [1,2,3], columns = ['a', 'b', 'c', 'd'])
df5 = pd.DataFrame(np.ones((3,4))*1, index = [2,3,4], columns = ['b', 'c', 'd', 'e'])   # 行列索引不同
result3 = pd.concat([df4, df5])   # 默认outer的join模式，求并集，且空缺值用NaN填上
result4 = pd.concat([df4, df5], join = 'inner')   # inner求交集


left = pd.DataFrame({'a': [1,1,1],
                    'b': [2,2,2],
                    'c': [3,3,3]})
right = pd.DataFrame({'a': [4,4,4],
                      'b': [5,5,5],
                      'c': [3,3,3]})

## merge合并
result5 = pd.merge(left, right, on = 'c')   # on表示在哪一列上合并，默认inner
                                            # 也可以在多个列上合并，on = [  ,  ]（有方括号）
                                            # 合并方式how可以等于'inner', 'outer', 'left', 'right'

