#выписывать из списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive = []
negative = []
for i in my_list:
        if i >= 0:
            positive.append(i)
            print(i)
        else:
            negative.append(i)
            break
