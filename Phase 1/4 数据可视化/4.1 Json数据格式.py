# Json是一种在各个编程语言中通用的数据格式，类似于国际通用语言是英语
# 通过python学Json是有优势的，Json格式是python的字典或列表那样，只不过列表内的元素也都是字典（其实就是字符串）

"""
python和json的相互转换
"""

#python列表转json
import json
text = [{"name":"张三", "age":18}, {"name":"李四", "age":16}, {"name":"王五", "age":13}]
json_str = json.dumps(text, ensure_ascii=False)
# dumps用来转json
# ensure这个参数表示数据内容不要转成ascii码，而是直接输出，这样就能输出中文
print(type(json_str))
print(json_str)

# python字典转json
text2 = {"name":"周", "height":180}
json_str2 = json.dumps(text2, ensure_ascii=False)
print(type(json_str2))
print(json_str2)

# json转python
# s这里必须是单引号
s = '[{"name":"张三", "age":18}, {"name":"李四", "age":16}, {"name":"王五", "age":13}]'
# loads用来转python
l = json.loads(s)
print(type(l))
print(l)
