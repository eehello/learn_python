#--coding:utf-8--
h=input("请输入你的身高\n")
kg=input("请输入你的体重\n")
h=float(h)
kg=float(kg)
bmi=kg/(h*h)
if bmi<18.5 :
    print("过轻")
elif bmi<=25 :
    print("正常")
elif bmi<=28:
    print("过重")
elif bmi<=32:
    print("肥胖")
elif bmi>32:
    print("严重肥胖")
