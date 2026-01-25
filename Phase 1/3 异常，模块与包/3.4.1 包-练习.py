import my_utils.str_util
print(my_utils.str_util.str_reverse("包模块的综合练习"))

from my_utils import str_util
s = str_util.substr("包模块的综合练习", 1, 3)
print(s)

from my_utils import file_util
file_util.print_file_name("exercise.txt")
file_util.append_to_file("exercise2.txt", "test")
