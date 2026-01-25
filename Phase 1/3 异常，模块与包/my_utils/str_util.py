# 实现字符串反转
def str_reverse(s):
    return s[::-1]

# 实现字符串切片
def substr(s, x, y):
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello", 2, 4))

