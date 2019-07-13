from random import randint

flat = 1

while flat:
    print("现在随机生成了一个0-10之间的数字，请猜一下")
    x = randint(0,10)

    while 1:
        a = int(input("请输入你认为的数字(不想玩了请输入110)："))
        if a == 110:
            flat = 0
            break
        if a == x:
            print("你真棒，猜对了，886")
            break

        if a > x:
            print("加油，离正确答案不远了，再小一点！")
            continue
        if a < x:
            print("加油，离正确答案不远了，再大一点！")
