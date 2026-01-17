# 位置参数
def user(name, age, gender):
    print (f'您的名字是{name}，年龄是{age}，性别是{gender}')
# 注意调用时传参的顺序
user("小王", 18, "男")


# 关键字参数
def user2(name, age, gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
# 关键字参数可以不按顺序
user2(age = 18,  name = "小明", gender = "男")
# 关键字参数和位置参数可以混用，但是位置参数必须在前,且匹配参数顺序
user2("小明", gender = "男", age = 18)


# 默认参数（缺省参数）
# 所有默认参数都必须出现在位置参数后面，包括定义和调用
# 错误示例：def user3(name, age = 18, gender):
def user3(name, age, gender = "男"):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
# 不传默认参数就会使用默认值，传了就使用传入值
user3("Tom", 18)
user3("Alice", 20, "女")


# 不定长参数：用于不知道要传多少参数和什么参数时
# 不定长-位置参数：*号
# 位置的不定长一般用args作为变量名，数据类型是元组
def user4(*args):
    print(f'args数据类型是{type(args)}，内容是{args}')
user4(1, 2, 3, "小明")

# 不定长-关键字参数：**号
# 关键字的不定长一般用kwargs作为变量名，数据类型是字典
def user4(**args):
    print(f'args数据类型是{type(args)}，内容是{args}')
# 必须要用键值对形式传参
user4(name = "小明", height = 170)

