a = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while a < len(my_list) and my_list[a] >= 0:
    a = a + 1
    if my_list[a - 1] == 0:
        continue
    print(my_list[a - 1])
