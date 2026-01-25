# 实现打开文件，并且如果文件不存在要捕获错误
def print_file_name(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding="utf-8")
        print(f.read())
    except Exception as e:
        print("未找到文件")
    # f此时是None，不能直接close，所以if语句是说如果f == True就close，如果是None就不执行
    finally:
        if f:
            f.close()

# 实现文件追加功能
def append_to_file(file_name, text):
    f = open(file_name, 'a', encoding = "utf-8")
    f.write(text)
    f.close()

if __name__ == '__main__':
    print_file_name("file.txt")
    # append_to_file("file.txt", "hello")


