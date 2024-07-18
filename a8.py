my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

res = []

for i in range(len(my_list)):
    if (i + 1) % 2 == 0:
        res.append(my_list[i])


print(res)

