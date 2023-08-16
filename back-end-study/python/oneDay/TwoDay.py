# # if
# age = 16
# if age >= 18:
#     print('你的年龄是', age)
#     print('你已满18岁')
# else:
#     print('你的年龄是', age)
#     print('你未满18岁')
#
# # elif
# age = 3
# if age >= 18:
#     print('已成年')
# elif age >= 6:
#     print('青少年')
# else:
#     print('儿童')
#
# # if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
# age = 20
# if age >= 6:
#     print('青少年')
# elif age >= 18:
#     print('已成年')
# else:
#     print('儿童')
#
# # 简写if判断
# x = 1
# if x:
#     print('True')
#
# # input+if
# birth = input('请输入出生年份：')
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# # int()
# s = input('请输入出生年份：')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# # 循环
# # for ... in
# names = ['张三', '李四', '王五']
# for name in names:
#     print(name)
#
# # 累加求和
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

# # range()函数
# nums = list(range(11))
# print(nums)

# while
# 计算100以内的所有奇数的和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)