score = int(input(">>:"))
if score >100:
    print("你输入的成绩无效请重新输入:")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=60:
    print("C")
elif score>=40: 
    print("D")
elif score >=0:
    print("E")
else:
    print("成绩不能为复制请重新输入:")