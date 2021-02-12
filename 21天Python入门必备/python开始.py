# cmd =>C:\Users\Lenovo>python=>print("你好")
# exit()=>退出
#这里是不能保存代码的  所以有要解释器。python 
#可以在cmd中做实验，不会影响程序。这就是好处。cmd 使用的内存，puython 使用的是硬盘。cmd的作用就是调试代码。
a = 2*3/6+1
print(a)
b = 100/(2*5)
print(b)

eat = 3+34+67+34+89
cloth = 34+6+48+89+67+59
print("total:",eat+cloth)
#变量： 数字开头不行  和内置名称相同不行 下划线而不是减号  下互相后面有空格是可以 只能英文和数字结合
#一定使用驼峰体和下划线  这是两个习惯
#驼峰体：两个单词第一个字母大写，
# 不要使用通配符
# 变量名字不要太长
# 下划线可以另个单词三个单词中间加上
# 词意要清晰
# 有覆盖的特性

a =1
b = a
a = 3
print(b)

a = 2
b = a
a = 4
b = a
print(b)

# name = input("what is your name:")
# print("hello"+name)  
# # 逗号或加号
# Username = input("username:")
# password = input("password:")
# print(Username,password)

c = 123
print(type(c))
print(type("abc"))

  
# long (长整数)

# 字符串
name = "wuheng"
name = 'wuheng'
age = "22"
age = 22
msg = '''my name is wuheng,my age is 22'''
hometown = "yanjiao"
print(name)
print(type(age))
print(msg)
print(hometown)

msg = "my's name wuheng,my's age  22"
print(msg)
# defined 定义  没有引号就会认为是变量
# boolean 就两种模式
# 就是逻辑判断
# true false 
a = 10 
b = 15
if a>b:
    print("false")
else:
    print("true")
