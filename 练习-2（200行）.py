import time
from functools import reduce


def eat(a, b, *args):
    print('我想吃', args, a, b)


eat('大米饭', '中米饭', '小米饭')


 def eat(a, b, c='白菜', *args):
    print('我想吃', a, b, c, args,)


eat('豆腐', '粉条', '猪肉', '大葱')  # 代替了里面的了。


def eat(a, b, *args, c='白菜',):
    print('我想吃', a, b, args, c)


eat('猪肉', '粉条', '豆腐', '大葱')  # 代替了里面的了。


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)
# 组成了字典


def func(a, b, c, d):
    print(a, b, c, d)


func(1, 2, 3, 4)


def func(*args, **kwargs):
    print(args, kwargs)


func(1, 23, 5, a=1, b=6)

list = [1, 14, 7]


def func(*args):
    print(args)


func(list[0], list[1], list[2])



list = [1, 14, 7]
def func(*args):
    print(args)
func(*list)





dic = {'a': 1, 'b': 2}
def func(**kwargs):
    print(kwargs)
func(**dic)

dic = {'吴恒':28336.5,'马日东':7762.5,'白毅':8060,'时建':7659,
'刘万鹏':7762.5,'杨斌':12124,'宋志明':5040,'刘随强':6480,'王丽':7555.5,'陈杨':5400,'张大志':4320}
def func(**kwargs):
    print(kwargs)
func(**dic)




def eat(food, drink):
    print(food, drink)
eat('麻辣烫', '肯德基')

def eat(food,drink):
    print(food,drink)
eat('麻辣烫','烧饼')




def fun():
    a = '吴恒'
    print(a)
fun()
# print(a)  # 不存在了




def fun():
    a = 20
    print(a)
fun()
a = 10





def fun():
    a = 40
    b = 20
    print('哈哈')
    print(a, b)
    print(globals())
    print(locals())
fun()




def fun1():
    print(111)
def fun2():
    print(222)
    fun1()
fun2()
print(111)






def fun2():
    print(222)

    def fun3():
        print(666)
    print(444)
    fun3()
    print(888)
print(33)
fun2()
print(555)



list = ['麻花疼', '刘嘉玲', '詹姆斯']
def func():
    list.append('马云')
    print(list)
func()
print(list)







a = 10
def func1():
    a = 20
    def func2():
        nonlocal a
        a = 30
        print(a)
    func2()
    print(a)
func1()
a = 10






def func1():
    a = 20

    def func2():
        # nonlocal a
        a = 30
        print(a)
    func2()
    print(a)


func1()

a = 1


def func_1():
    a = 2

    def func_2():
        nonlocal a
        a = 3

        def func_3():
            a = 4
            print(a)
        print(a)
        func_3()
        print(a)
    print(a)
    func_2()
    print(a)
print(a)
func_1()
print(a)


n = 13
print(eval('n+2'))
n = 9
print(eval('2+n'))



def func():
    print(666)
eval('func()')



print('你好', '我好')
print('你好', '我好', sep='|')  # 分隔符

print('你好')
print('我好')
print('你好', end='')  
print('我好')


print('您好')
print('您好','我好',sep='|')
print('您好','我好',end='')
print('您好','我好')



print(hash('我好'))

help(print)  

print(callable(print))  
print(callable(help))


int(dir(list))
print(abs(-1))

print(divmod(98, 4)) #对于整数，结果与（a//b，a%b）相同。
print(divmod(2,1))
print(divmod(2,1.33))
print(divmod(2,-4))

# ​ pow(a, b) 求a的b次幂, 如果有三个参数. 则求完次幂后对第三个数取余
print(pow(17, 2, 8))
print(pow(34, 2, 9))
print(pow(45, 5, 2))
print(pow(17, 7, 8))
print(pow(17, 2, 4))
print(pow(17, 2, 83))

#  sum() 求和
print(sum([98, 4, 56, 87]))  # sum里边的参数是一个可迭代对象

# max() 求最大值
print(max([98, 4, 56, 87]))

l = reversed('你好')  # list() 将一个可迭代对象转换成列表  re
print(list(l))   

print(format("你好", '>20'))  # 右对齐  f
print(format("你好", '<20'))  # 左对齐
print(format("你好", '^20'))  # 居中

print(format(3, 'b'))  # 二进制
print(format(78, 'c'))  # 转换成unicodezif
print(format(111, 'd'))  # 十进制
print(format(45))  # 和d一样
print(format(23, 'n'))  # 十进制
print(format(327, 'o'))  # 八进制
print(format(2378, 'x'))  # 十六进制(小写字母)
print(format(2378, 'X'))  # 十六进制(大写字母)

print(format(1234567890, 'e'))  # 科学计算法,默认使用6位
print(format(1234567890, '0.2e'))  # 科学计算,保留2位小数(小写)
print(format(1234567890, '0.2E'))  # 科学计算,保留2位小数(大写)
print(format(1234567890, 'f'))  # 小数点计数法,保留6位小数
print(format(1234567890, '0.2f'))  # 小数点计数法,保留2位小数)
print(format(1234567890, '0.10f'))  # 小数点计数法,保留2位数
print(format(1.23456789e+1000, 'F'))  # 小数点计数法

# bytes() 把字符串转换成二进制类型
s = '你好武大郎'
bs = s.encode('utf-8')  # 编码
print(bs)

si = bs.decode('utf-8')  # 解码 de
print(si)  

si = bs.decode('utf-8')  # 解码 de
print(si) 

# 将字节转换成字符串
bs1 = str(bs, encoding='utf-8')
print(bs1)

# repr() 返回一个对象的官方表示形式
print(repr('大家好,\n,\t我叫周杰伦'))
print('大家好我叫周杰伦')
name = 'taibai'
print('我叫%r' % name)

list = ['吴恒', 'wusir', 'taibai']
for i, k in enumerate(list):
    print('这是序号', i)
    print('这是元素', k)  # 添加序号和元素

# all() 可迭代对象中全部是True,结果才是True
list = [1, 2, 3, 4, True, 0, False]
list_1 = [1, 2, 3, 4, True]
print(all(list))
print(all(list_1))

# any() 可迭代对象中有一个是True,就是True
list = [1, 2, 3, 4, True, 0, False]
list_1 = [1, 2, 3, 4, True]
print(any(list))
print(any(list_1))

# zip() 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元祖,
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c', 'd']
list_3 = (12, 34, 45, 35, 26)
for i in zip(list_1, list_2, list_3):  
    print(i)


list_1 = [1,2,3,4]
list_2 = ['q','e','r','g','j']
list_3 = ['t','q','v']
for i in zip(list_1,list_2,list_3):
    print(i)
# 匿名函数,为了解决一些简单的需求而设计的一句话函数


def func(n):
    return n**n
print(func(4))

def func(n):
    return n**n
print(func(9))


def f(x): 
    return x**x
print(f(4))
def func(x):
    return x**6
print(func(4))



#函数名 = lambda 参数:返回值

# 排序函数
list = [1, 2, 5, 4, 7, 9, 19]
list_2 = sorted(list)  
print(list)  
print(list_2)  # 正序
list_3 = sorted(list, reverse=True)  # reverse :是否是倒叙,True 倒叙 False 正序
print(list_3)  


list = [1, 2, 5, 4, 7, 9, 19]
print(list)
list_1 = sorted(list)
print(list_1)
list_2 = sorted(list,reverse=True)
print(list_2)
# 字典使用sorted排序
dic = {1: 'a', 3: 'c', 4: 'd'}
print(sorted(dic))  # 提前键


dic = {1: 'a', 3: 'c', 4: 'd'}
print(sorted(dic))
# 和函数组合使用
# 定义一个列表,然后根据一元素的长度排序
list = ['天龙八部', '西游记', '红楼梦', '三国演义']


def func(s):
    return len(s)
print(sorted(list, key=func))



# 和lambda组合使用
list = ['天龙八部', '西游记', '红楼梦', '三国演义']
print(sorted(list, key=lambda s: len(s)))

list = [{'id': 1, 'name': '吴恒', 'age': 18},
        {'id': 2, 'name': 'wusir', 'age': 17},
        {'id': 3, 'name': 'taibai', 'age': 16}]
# 按照年龄对学生信息进行排序
print(sorted(list, key=lambda e: e['age']))
#语法: filter(function,iterable)

# function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,然后根据function返回的True或者False来判断是否保留此项数据

# iterable:可迭代对象
lst = [{'id': 1, 'name': '吴恒', 'age': 18},
       {'id': 1, 'name': 'wusir', 'age': 17},
       {'id': 1, 'name': 'taibai', 'age': 16}, ]
ls = filter(lambda e: e["age"] > 16, lst)
print(list(ls))

# map映射函数n**n
lst = [1, 2, 4, 5, 6, 7]
def fun(s):
    return s**s
mp = map(fun, lst)
print(mp)
print(list(mp))  # 计算列表中每个元素的平方,返回新列表





lst = [1, 2, 4, 5, 6, 7]
print(list(map(lambda s: s*s, lst)))  # 改写成lambda

# 计算两个列表中相同位置的数据的和
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x+y, lst1, lst2)))

# reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
# 接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
# 临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类推
# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行


def func(x, y):
    return x+y
ret = reduce(func, [5, 6, 7, 8, 9])
print(ret)


# 注意:我们放进去的可迭代对象没有更改
# 以上这个例子我们使用sum就可以完全的实现了.我现在有[1,2,3,4]想让列表中的数变成1234,就要用到reduce了.
# 普通函数版


def func(x, y):
    return x*10+y
l = reduce(lambda x, y: x*10+y, [1, 2, 3, 4, 6])
print(l)

l = reduce(func, [1, 2, 3, 4, 6])
print(l)
# from functools import reduce

l = reduce(lambda x, y: x*10+y, [1, 2, 3, 4, 6])
print(l)


def func():
    print('呵呵')
print(func)




def func():
    print('呵呵')
    print(func)
a = func
a()




def func1():  # 函数名可以当做容器类的元素
    print('呵呵')


def func2():
    print('呵呵')


def func3():
    print('呵呵')


def func4():
    print('呵呵')


lst = [func1, func2, func3, func4]
for i in lst:
    i()


# 函数名可以当做函数的参数
def func():
    print('吃了吗')


def func2(fn):
    print('我是func2')
    fn()  # 执行传递过来的fn
    print('我是func2')


func2(func)  # 把函数func当成参数传递给func2的参数fn.

# 函数名可以作为函数的返回值


def func_1():
    print('这里的函数1')

    def func_2():
        print('这里的函数2')
    print('这里的函数1')
    return func_2


fn = func_1()  # 执行函数1.  函数1返回的是函数2, 这时fn指向的就是上面函数2

fn()  # 执行func_2函数

# 什么是闭包? 闭包就是内层函数, 对外层函数(非全局)的变量的引用. 叫闭包


def func1():
    name = '吴恒'

    def func2():
        print(name)
func2() 


func1()


# 我们可以使用__closure__ 来检测函数是否是闭包. 使用函数名.__closure__返回cell就是
# 闭包. 返回None就不是闭包
def func1():
    name = '吴恒'
    def func2():
        print(name)
    func2()
    print(func2.__closure__)
func1()

def func1():
    name =   "吴恒"
    def func2():
        print(name)
    func2()
    print(func2.__closure__)
func1()





def outer():
    name = '吴恒'
    def innter():
        print(name)
    return innter
fn = outer()  # 访问外部函数, 获取到内部函数的函数地址
fn()  # 访问内部函数
# 这样就实现了外部访问,那如果多层嵌套呢?很简单,只需要一层一层的往外层返回就行了





def func1():
    name = '吴恒'
    def func2():
        s = '呵呵'
        def func3():
            print(name)
        return func3
    return func2
func1()()()  # 访问外部函数, 获取到内部函数的函数地址





# str list tuple dic set 那为什么我们称他们为可迭代对象呢?因为他们都遵循了可迭代协议,那什么又是可迭代协议呢.首先我们先看一段代码:

# 正确的代码:
s = 'abd'
for i in s:
    print(i)

s = 'abd'
print(dir(s))  # dir查看对象的方法和函数
# 在打印结果中寻找__iter__ 如果存在就表示当前的这个类型是个可迭代对dic
# 列表
lst = [1, 2, 5, 6, 8, 9]
print(dir(lst))

tuple = (1, 2, 5, 6, 8, 9)
print(dir(tuple))

dic = {'a': 1, 'b': 2}
print(dir(dic))
set = {2, 3, 8, 9, 5, 7}
print(dir(set))
# 是不是发现以上都有__iter__并且还很for循环啊,其实也可以这么说可以for循环的就有__iter__方法,包括range
s = '我爱北京天安门'  # for的工作原理到底是什么? 继续向下看:
c = s.__iter__()  # 获取迭代器
prnt(c.__next__())
print(c.__net__())
print(c.__next__())
print(c.__next__())

dic# 深浅拷贝
# # 文件dic
# 参数
# def (a1,a2):
# def (a1,a2=None)常用不可变参数不要用可变变参数
# 函数名可以当做函数的参数
# 函数的参数传递的是什么？
v = [11, 22, 33, 44]


def func(arg):
    print(id(arg))  # 列表的内存地址


print(id(v))  # 列表的内存地址
func(v)
# 内外一样 传递的内存地址
# 返回值
# 常见数据类型可以返回

# 函数也可返回
# 特殊
# 默认没有返回就是NONE

# *args 和**kwargs 的作用


def func():
    def innter():
        pass
    return innter


v = func()

# #执行函数
# 函数不被调用 内部代码永远不执行


def func():
    return i


func_list = []
for i in range(10):
    func_list.append(func)
print(i)
v1 = func_list[4]()
v2 = func_list[0]()

func_list = []
for i in range(10):
    func_list.append(lambda: i)  # 函数不被调用内部不执行永远不知道
print(func_list)
func_list[2]()

# 执行函数是 会新开创一块保存之间函数执行的信息
# 闭包


def base(arg):
    return arg


def func(arg):
    def innter():
        return arg
    return innter


# v1 = func(1)
# v2 = func(2)
base_list = []  # [base]
func_list = []  # 有第一次执行func函数的内存地址创建的inner函数arg = 0   arg = 1....
for i in range(10):
    base_list.append(base)
    func_list.append(func(i))

# base_list 总存的函数是base 函数
# func_list 中存储了inner 函数 特别是每个inner 是不同的地址创造
for item in base_list:
    v = item()
    print(v)
for data in func_list:
    v = data()
    print(v)

# 总结
# 传参   位置参数在前  关键字参数在后
# 函数不掉用  内部代码不执行
# 执行函数时每次都会为此次调用开辟一块内存
# 内存中可以保存以后要想用的值
# 函数作用域 如果自己作用域没有 则往上找

# 内置和匿名函数
# 内置和匿名函数
# 匿名函数
# 模块
# getpass
# random
# hashlib
# 内置函数不用导用就能用  不用import
# py 文件就是内置函数
# 内置函数就是精英
# 内容详情
# 作业题回顾


def func(*args, **kwargs):
    print(args, kwargs)


func(12, 3, *[11, 22])
func(('吴恒', '吴佩奇'), name='aric')


def func(arg):
    return arg.pop(1)


result = func([11, 22, 33])
print(result)

func_list = []
for i in range(10):
    func_list.append(lambda: i)
v1 = func_list[0]()
v2 = func_list[5]()
print(v1, v2)


func_list = []
for i in range(10):
    func_list.append(lambda x: x+i)
v1 = func_list[0](2)
v2 = func_list[5](1)
print(v1, v2)

func_list = []
for i in range(10):
    func_list.append(lambda x: x+i)
    # 等于9  func_list 里面都是函数  x: x+i x: x+i
for i in range(0, len(func_list)):
    result = func_list[i](i)
    print(result)


# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1,v2)

def f1():
    print('f1')


def f2():
    print('f2')
    return f1


func = f2()
result = func()
print(result)


def f1():
    print('f1')
    return f3()


def f2():
    print('f2')
    return f1


def f3():
    print('f3')
    # return 666


func = f2()
result = func()
print(result)

name = '进女生'


def func():
    def innter():
        print(name)  # 没有返回值
    return innter()


    # return innter  #家括号执行  不加括号执行参数  不执行函数
v = func()
print(v)


name = '进女生'


def func():
    def innter():
        print(name)  # 没有返回值
        return '老男孩'
    return innter()


    # return innter
    # return innter  #家括号执行  不加括号执行参数  不执行函数
v = func()
print(v)


name = '进女生'


def func():
    def innter():
        print(name)  # 没有返回值
        return '老男孩'
    return innter


    # return innter
    # return innter  #家括号执行  不加括号执行参数  不执行函数
v = func()
result = v()
print(result)


def func(name):
    return lambda x: x+name


v1 = func(1)
v2 = func(2)
result_1 = v1(10)
result_2 = v2(10)
print(result_1, result_2)
# print(v1,v2)

# 装饰器
# 做表面功夫


def func():
    pass


v = func


def base():
    print(1)


def bar():
    print(2)


bar = base
bar()
def base():
    print(1)
def bar():
    print(2)
bar = base
bar()


def func():
    def innter():
        pass
    return innter
v = func()
print(v)

user_status = False
def login():#...
    _username = '吴恒'
    _password = 'abc123'
    global user_status
    if user_status == False:
        user_name = input('user:')
        password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status == True
        else:
            print('wrong username or password')
    else:
        print('用户已登陆，验证已通过.....')
def home():
    print('-----首页------')
def henan():
    login()#执行前加认证
    print('-----河南专区------')
def america():
    login()#执行前加认证
    print('-----欧美专区------')
def japan():
    print('-----日韩专区------')
home()
henan()#这两个只能分别调用
america()
#代码源能扩展不能修改


user_status = False
def login(func):#...
    _username = '吴恒'
    _password = 'abc123'
    global user_status
    if user_status == False:
        user_name = input('user:')
        password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status == True
        else:
            print('wrong username or password')
    else:
        print('用户已登陆，验证已通过.....')
if user_status:
        func()#如果验证通过就调用响应功能
def home():
    print('-----首页------')
def henan():
    # login()#执行前加认证
    print('-----河南专区------')
def america():
    # login()#执行前加认证
    print('-----欧美专区------')
def japan():
    print('-----日韩专区------')
login(henan)
login(america)


user_status = False
def login(func):#...
    _username = '吴恒'
    _password = 'abc123'
    global user_status
    if user_status == False:
        user_name = input('user:')
        password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status == True
        else:
            print('wrong username or password')
    else:
        print('用户已登陆，验证已通过.....')
if user_status:
        func()#如果验证通过就调用响应功能
def login(func):#...
    _username = '吴恒'
    _password = 'abc123'
    global user_status
    if user_status == False:
        user_name = input('user:')
        password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status == True
        else:
            print('wrong username or password')
    else:
        print('用户已登陆，验证已通过.....')
if user_status:
        func()#如果验证通过就调用响应功能
def home():
    print('-----首页------')
def henan():
    # login()#执行前加认证
    print('-----河南专区------')
def america():
    # login()#执行前加认证
    print('-----欧美专区------')
def japan():
    print('-----日韩专区------')
home()
henan = login(henan)

america = login(america)
america()





user_status = False
def login(func):
    def inner():
        _username = 'alxe'
        _password = 'abc123'
        global user_status
        if user_status ==False:
            user_name = input('user:')
            password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status == True
        else:
            print('wrong username or password')
        
        # else:
        #     print('用户已登陆，验证通过....')
        if user_status:
            func()
    return inner

def home():
    print('-----首页------')
@login#装饰器
def henan():
    # login()#执行前加认证
    print('-----河南专区------')
def america():
    # login()#执行前加认证
    print('-----欧美专区------')
def japan():
    print('-----日韩专区------')   
# henan = login(henan)=@login
# print(henan)
henan()#inner
# america = login(america)




user_status = False
def login(func):
    def inner(arg):#家参数arg
        _username = '吴恒'
        _password = 'abc123'
        global user_status
        if user_status ==False:
            user_name = input('user:')
            password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            user_status = True
        else:
            print('wrong username or password')
        
        # else:
        #     print('用户已登陆，验证通过....')
        if user_status:
            func(arg)#老henan
    return inner

def home():
    print('-----首页------')
@login#装饰器
def henan(style):
    # login()#执行前加认证
    print('-----河南专区------',style)
def america():
    # login()#执行前加认证
    print('-----欧美专区------')
def japan():
    print('-----日韩专区------')   
# henan = login(henan)=@login
# print(henan)
henan('3p')#inner




user_status = False
def login(func):#henan
    def inner(*args):#家参数arg
        _username = '吴恒'
        _password = 'abc123'
        global user_status
        if user_status ==False:
            user_name = input('user:')
            password = input('password:')
        if user_name == _username and password == _password:
            print('welcom login....')
            print('用户已登陆，验证通过....')
            user_status = True
        else:
            print('wrong username or password')
        # else:#这里怎么错的？

        #     print('用户已登陆，验证通过....')
        if user_status:
            func(*args)#老henan
    return inner

def home():
    print('-----首页------')
# @login#装饰器
def henan(style):
    # login()#执行前加认证
    print('-----河南专区------',style)
def america():
    # login()#执行前加认证
    print('-----欧美专区------')
# @login
def japan(style1):
    print('-----日韩专区------',style1)   
# henan = login(henan)=@login
# print(henan)
henan('3p')#innerzf
japan('5p')
# 106函数-函数进阶-列表生成式_batch











def func(arg):
    def innter():
        print(arg)
    return innter
v1 = func(1)
v2 = func(2)
print(v1, v2)


def func(arg):
    def inner():
        print(arg)
    return inner
v1 = func(1)
v2 = func(2)
print(v1,2)




def func(arg):
    def innter():
        arg()
    return innter
def f1():
    print(124)
v1 = func(f1)
v1()


def func(arg):
    def inner():
        arg()
    return inner
def f1():
    print(1234)
v1 = func(f1)
v1()



def func(arg):
    def innter():
        arg()
    return innter
def f1():
    print(124)
    return 777
v1 = func(f1)
result = v1()
print(result)


def func(arg):
    def inner():
        arg()
    return inner
def f1():
    print(2345)
    return 3477
v1 = func(f1)
result = v1
print(result)




def func(arg):
    def innter():
        return arg()
    return innter
def f1():
    print(124)
    return 777
v1 = func(f1)
result = v1()
print(result)


def func(arg):
    def inner():
        return arg()
    return inner
def f1():
    print(123)
    return 9980
v1 = func(f1)
result = v1()
print(result)






def func():
    print(1)
def base(): 
    print(2)
v1 = func
func = 666


def func():
    print(2)
def base():
    print(3)
v1 = func
func = 666






def func(arg):
    def innter():
        return arg()
    return innter
def index():
    print('123')
    return '666'
# v1 = index()
# v2 = func(index)
# index = 666
# v3 =v2()
v4 = func(index)
index = v4
index()   


def func(arg):
    def inner():
        return arg()
    return inner
def index():
    print(123)
    return "8888"
v4 = func(index)
index = v4
index()







def func(arg):
    def innter():
        print('afer')
        v = arg()
        print('afddfg')
        return v
    return innter
def index():
    print('123')
    return '666'
# v1 = index()
# v2 = func(index)
# index = 666
# v3 =v2()
index = func(index)
index()








def func(arg):
    def innter():
        print('afer')
        v = arg()

        print('afddfg')
        return v
    return innter


@func  # 执行func 并将下面函数参数传递相当于func(index)
# 第二步将func 的返回值重新负值给下面的函数 index = func(index)
def index():
    print('123')
    return '666'


print(index())
# day13 装饰器引入(上)

index = func(index)


def func(arg):
    def innter():
        print('skog')
        v = arg()
        print("song][[mgm")
        return v
    return innter


@func  # 第一步执行func函数将下面的函数传递func (index)
# 第二步func 的返回值重新负值给下面的函数 index = func(index)
def index():  # 不改变原函数代码在函数执行之前和之后自动执行摸个功能
    print(123)
    return 666


# print(index())
# v = index()
# print(v)
print(index)

# 计算函数执行时间


def func1():
    time.sleep(2)
    print(123)


def func2():
    time.sleep(2)
    print(123)


def func3():
    time.sleep(2)
    print(123)


start_time1 = time.time()
func1()
end_time1 = time.time()
print(end_time1-start_time1)
start_time2 = time.time()
func2()
end_time2 = time.time()
start_time3 = time.time()
print(end_time2-start_time2)
func3()
end_time3 = time.time()
print(end_time3-start_time3)
# 函数名的内存地址


def func():
    print('呵呵')


print(func)  # 打印了地址

# 函数名可以赋值给其他变量


def func():
    print('呵呵')
    print(func)


a = func  # 把函数当成一个值赋值给另一个变量
a()  # 函数调用 func()

# 函数名可以当做容器类的元素


def func1():
    print('呵呵')


def func2():
    print('呵呵')


def func3():
    print('呵呵')


def func4():
    print('呵呵')


def func5():
    print('呵呵')


list = [func1, func2, func3, func4, func5]
for i in list:
    i()

# 函数名可以当做函数的参数


def func():
    print('吃了吗？')


def func2(fn):
    print('我是func2')
    fn()  # 执行传递过来的fn
    print('我是func2')


func2(func)  # 把函数func当成参数传递给func2的参数fn.

# 函数名可以作为函数的返回值


def func_1():
    print('这里是函数1')

    def func_2():
        print('这里是函数2')
    print('这里是函数1')
    return func_2


fn = func_1()  # 执行函数1.  函数1返回的是函数2, 这时fn指向的就是上面函数2
fn()

# '这里是函数1'

# '这里是函数1'
# '这里是函数2'

# 闭包


def func1():
    name = '吴恒'

    def func2():
        print(name)  # 闭包
    func2()


func1()

# 检测闭包__closure__ 来检测函数是否是闭包. 使用函数名.__closure__返回cell就是返回None就不是闭包


def func1():
    name = '吴恒'

    def func2():
        print(name)  # 闭包
    func2()
    print(func2.__closure__)


func1()  # (<cell at 0x00000279308D9CD8: str object at 0x0000027930C4B9F0>,)
# 我们可不可以将里边的函数名当做参数返回给调用者啊


def outer():
    name = '吴恒'
    # 内部函数

    def inner():
        print(name)
    return inner


fn = outer()  # 访问外部函数, 获取到内部函数的函数地址
fn()  # 访问内部函数

# 这样就实现了外部访问,那如果多层嵌套呢?很简单,只需要一层一层的往外层返回就行了


def func1():
    def fucn2():
        s = '和黑'

        def func3():
            print(s)
        return func3
    return func2


func1()()()

#
# 迭代器

s = 'abddc'
for i in s:
    print(i)

# iterable表示可迭代的.表示可迭代协议 那么如何进行验证你的数据类型是否符合可迭代协议.我们可以通过dir函数来查看类中定义好的所有方法
a = 'dpingg,(d,r,f,g)'
print(dir(a))  # dir查看对象的方法和函数
# 在打印结果中寻找__iter__ 如果存在就表示当前的这个类型是个可迭代对象

s = [2, 33, 45, 25, 44, 67, 89, 65]
for i in s:
    print(i)
s = [2, 33, 45, 25, 44, 67, 89, 65]
print(dir(s))
# 列表 f可以
# 元祖 可以
s = (2, 33, 45, 25, 44, 67, 89, 65)
print(dir(s))
# 字典 可以
s = {'name': 33, 'age': 25, 'mappe': 67, 'TabEr': 65}
print(dir(s))
# 集合 可以
s = {33, 25, 67, 65}
print(dir(s))
print(dir(range))
# 是不是发现以上都有__iter__并且还很for循环啊,其实也可以这么说可以for循环的就有__iter__方法,包括range
# 这是查看一个对象是否是可迭代对象的第一种方法,我们还可以通过isinstence()函数来查看一个对象是什么类型的

# 生成器


def func():
    print(11)
    return 22


ret = func()
print(ret)
# 我们只需要修改一个地方就可以把函数变成生成器 就是将函数中的return换成yield就是生成器


def func():
    print(11)
    yield 22


ret = func()
print(ret)
# <generator object func at 0x000002A2DE8B3648>


def func():
    print(1223)
    yield 3455


gener = func()
ret = gener.__next__()
print(ret)
# yield是分段来执行一个函数,yield可以出现多次

# return是直接停止这个函数,return可以出现多次但是只会执行到第一个就结束了


def func():
    print(1223)
    yield 3455
    print(33555)
    yield 87799


gener = func()
ret = gener.__next__()
print(ret)
ret2 = gener.__next__()
print(ret2)
ret3 = gener.__next__()  # 最后⼀个yield执⾏完毕. 再次__next__()程序报错

print(ret3)
# 生成器的作用
# 我们来看一下这个需求,老男孩向楼下好适口的老板订购了10000个包子.好适口老板也实在一下就全部都做出来了　


def eat():
    list = []
    for i in range(1, 100):
        print('包子'+str(i))
    return list


e = eat()
print(e)


def eat():
    list = []
    for i in range(1, 100):
        print('包子'+str(i))
    return list


e = eat()
print(e)
# 这样做是没有问题,但是我们目前这么点人吃不完这么多,只能先放到一个地方,过会在吃的时候包子就凉了.这样也不太好

# 最后是老板能够咱们吃一个他做一个.这样我们就不用考虑没地方和包子凉的问题了,咱们实现一个吃一个做一个


def eat():

    for i in range(1, 100):
        yield ('包子'+str(i))


e = eat()
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())

# 我们再来看一个和__next__类似的东西send()

# send和__next__()一样都可以让生成器执行到下一个yield


def eat():

    for i in range(1, 100):
        a = yield ('包子'+str(i))
        print('a is ', a)
        b = yield '窝窝头'
        print('b is ', b)


e = eat()
print(e.__next__())
print(e.send('大蒜'))
print(e.send('大葱'))
#send可以给上一个yield的位置传递值, 在第一次执行生成器的时候不能直接使用send(),但是可以使用send(None)

# 生成器可以for循环来循环获取内部元素:


def func():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 27


f = func()
for i in f:
    print(i)

# yield from
# 在python3中提供一种可以直接把可迭代对象中的每一个数据作为生成器的结果进行返回


def func():
    list = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    yield from list


g = func()
for i in g:
    print(i)

# 小坑有个小坑,yield from 是将列表中的每一个元素返回,所以 如果写两个yield from 并不会产生交替的效果


def func():
    list = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    list1 = ['馒头', '花卷', '豆包', '大饼']
    yield from list
    yield from list1


g = func()
for i in g:
    print(i)
#推导式   列表推导式
li = []
for i in range(10):
    li.append(i)
print(li)

#列表推导式的常⽤写法:

# [结果 for 变量 in 可迭代对象]
li = [i for i in range(10)]
print(li)
li = ['python%s' % i for i in range(10)]
print(li)

#筛选模式
# [结果 for 变量 in 可迭代对象 if 条件]
li = [i for i in range(100) if i %2 == 0 ]#被2整除
print(li)

#生成器推导式
# 生成器表达式和列表推导式的语法基本上一样的,只是把[]换成()

gen = [i for i in range(34)]
print(gen)
## 结果: <generator object <genexpr> at 0x0000026046CAEBF8>
gen = ['第%s次' % i for i in range(10)]
print(gen)

#生成器表达式也可以进行筛选
# 获取1-100内能被3整除的数
li = [i for i in range(1,100) if i %3 == 0 ]#被2整除
print(li)#被3整除

# 100以内能被3整除的数的平⽅和
gen = [i*i for i in range(1,100) if i %3 == 0 ]#被3整除
# print(li)
for num in gen:
    print(num)

# 寻找名字中带有两个e的人的名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 不用推导式和表达式
result = []
for first in names:
    for name in first:
        if name.count('e')>=2:
            result.append(name)
print(result)

# 推导式
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
gen = (name for first in names for name in first if name.count('e')>=2)
for i in gen:
    print(i)

#生成器表达式和列表推导式的区别:
def func():
    print(111)
    yield 234
g = func()## 生成器g
# print(g)#<generator object func at 0x0000012B17D935C8>

g1 = (i for i in g )# 生成器g1. 但是g1的数据来源于g
g2 = (i for i in g1)# 生成器g2. 来源g1
# list的底层有for循环,for就是一直执行__next__() 所以可以将生成器放到list中
print(list(g))# 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
print(list(g1))# 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
print(list(g2))# 和g1同理理
print(next(g))
print(next(g1))
print(next(g2))  # 可以用next来验证  其实list就是将内容迭代了转换成了列表


#字典推导式
lst1 = ['jay','jj','meet']
lst2 = ['周杰伦','林俊杰','郭宝元']
dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)

dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)

#集合推导式
#集合推导式可以帮我们直接生成一个集合,集合的特点;无序,不重复 所以集合推导式自带去重功能
list = [1,2,3,-1,-3,-4,6,9]
s = {abs(i) for i in list}
print(s)

#装饰器
#在认识它之前我们先来回顾一下闭包
def func1():
    name = '吴恒'
    def func2():
        print(name)
    func2()
func1()

#现在你在公司，领导让你写一个函数，来测试另一个函数的执行效率，你怎么做？
import time


def func():
    print('嘻嘻好好坑坑')
import time

start_time1 = time.time()
time.sleep(0.1)
func()
end_time1 = time.time()
print('......执行效率%s'%(end_time1-start_time1))

#上面你已经写完了，但是你应该放在函数中，这样减少重复代码，可读性好，ok继续做


import time


def func():
    print('嘻嘻好好坑坑')
def timmer(f):
    start_time1 = time.time()
    time.sleep(0.1)
    f()
    end_time1 = time.time()
    print('......执行效率%s'%(end_time1-start_time1))
#好你又写完了，但是执行之前的函数只是func(),而你写玩了这个之后，还得加一步timmer(func),如果要是领导让你测试500个函数的执行效率呢？好，你又进一步改，如下
func()
f1 = func# func
func = timmer# timmer
func(f1)#将他的执行结果改了一下，这样看似func(f1)与原来的调用差不多，但是加了好几步，而且添加了f1参数。
#现在你请教了我，我说来，写个装饰器就能解决。
import time


def timmer(f):#小花
    # print('嘻嘻好好坑坑')
    def inner():# 小红
        start_time1 = time.time()
        time.sleep(0.1)
        f()
        end_time1 = time.time()
        print('......执行效率%s'%(end_time1-start_time1))
#好你又写完了，但是执行之前的函数只是func(),而你写玩了这个之后，还得加一步timmer(func),如果要是领导让你测试500个函数的执行效率呢？好，你又进一步改，如下
    return inner
def func(): #小刚
    print('is func')
func = timmer(func)# inner
func()# inner()

import time


def timmer(f):#小花
    print('嘻嘻好好坑坑')
    def inner():# 小红
        start_time1 = time.time()
        time.sleep(0.1)
        f()
        end_time1 = time.time()
        print('......执行效率%s'%(end_time1-start_time1))
#好你又写完了，但是执行之前的函数只是func(),而你写玩了这个之后，还得加一步timmer(func),如果要是领导让你测试500个函数的执行效率呢？好，你又进一步改，如下
    return inner
def func(): #小刚
    print('is func')
func = timmer(func)# inner
func()# inner()


#语法糖 @  
import time


def timmer(f):#小花
    print('嘻嘻好好坑坑')
    def inner():# 小红
        start_time1 = time.time()
        time.sleep(0.1)
        f()
        end_time1 = time.time()
        print('......执行效率%s'%(end_time1-start_time1))
#好你又写完了，但是执行之前的函数只是func(),而你写玩了这个之后，还得加一步timmer(func),如果要是领导让你测试500个函数的执行效率呢？好，你又进一步改，如下
    return inner
@timmer # func = timmer(func)
# def func(): #小刚
#     print('is func')
# func = timmer(func)# inner
# func()# inner()

# @装饰器函数 == 重新定义被装饰函数=装饰器函数（被装饰函数）
#语法糖的拆解
def func():
    print('嘻嘻哈哈')
func()# inner()

#2、拿来主义，提升开发效率 
#同样的原理，我们也可以下载别人写好的模块然后导入到自己的项目中使用，这种拿来主义，可以极大地提升我们的开发效率，避免重复造轮子。

print('from the tbjx.py')
name = '太白金星'
def read1():
    print('tbjx模块：',name)
def read2():
    print('tbjx模块：')
    read1()
def change():
    global name
    name = 'barry'
#import 翻译过来是一个导入的意思
#模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，它们只在模块名第一次遇到导入import语句时才执行（import语句是可以在程序中的任意位置使用的,且针对同一个模块很import多次,为了防止你重复导入，python的优化手段是：第一次导入后就将模块名加载到内存了，后续的import语句仅是对已经加载到内存中的模块对象增加了一次引用，不会重新执行模块内的语句），如下 
# import spam #只在第一次导入时才执行spam.py内代码,此处的显式效果是只打印一次'from the spam.py',当然其他的顶级代码也都被执行了,只不过没有显示效果.
#代码示例：
import tbjx
# 当前是meet.py
import tbjx.py

#执行结果：只是打印一次：
# from the tbjx.py


#第一次导入模块执行事件
# 1.为源文件(tbjx模块)创建新的名称空间，在tbjx中定义的函数和方法若是使用到了global时访问的就是这个名称空间。

# 2.创建名字tbjx来引用该命名空间
# 这个名字和变量名没什么区别，都是‘第一类的’，且使用tbjx.名字的方式
# # 可以访问tbjx.py文件中定义的名字，tbjx.名字与test.py中的名字来自
# 两个完全不同的地方。
#被导入模块有独立的名称空间
#　　每个模块都是一个独立的名称空间，定义在这个模块中的函数，把这个模块的名称空间当做全局名称空间，这样我们在编写自己的模块时，就不用担心我们定义在自己模块中全局变量会在被导入时，与使用者的全局变量冲突
#示例：

name = '太白金星'
print(name)
print(tbjx.name)
# from the tbjx.py'吴恒
太白金星

def read1():
    print(666)
tbjx.read1()
# from the tbjx.py
'tbjx模块：太白金星'
name = '日天'
tbjx.change()
print(name)
print(tbjx.name)
# from the tbjx.py
# 日天
# barry

#为模块起别名
# 别名其实就是一个绰号,好处可以将很长的模块名改成很短,方便使用..
# import tbjx.py as try:
t.read1()
#有利于代码的扩展和优化
##mysql.py
def sqlparse():
    print('from mysq1 sqlparse')
#oracle.py
def sqlparse():
    print('from orcle sqlparse')
#test.py
db_type = input('>>:')
if db_type == 'mysql':
    import mysq1 as db
elif db_type =='oracle':
    import oracle as db
db.sqlparse()

import json
#推荐写法
# 导入多个模块
import os  # 这样写可以但是不推荐
import sys

#from…import…使用
from tbjx import name, read1

#多行导入 易于阅读 易于编辑 易于搜索 易于维护

print(name)
read1
# 执行结果：
# from the tbjx.py
# 太白金星
# tbjx模块： 太白金星

#from…import… 与import对比
#唯一的区别就是：使用from…import…则是将spam中的名字直接导入到当前的名称空间中，所以在当前名称空间中，直接使用名字就可以了、无需加前缀：tbjx.

# from…import…的方式有好处也有坏处
# 好处：使用起来方便了
# 坏处：容易与当前执行文件中的名字冲突

# 示例演示：

# 执行文件有与模块同名的变量或者函数名，会有覆盖效果。
name = 'oldboy'
from tbjx import name, read1, read2

print(name)
#执行结果：
# 太白金星

from tbjx import name, read1, read2

name = 'oldboy'
print(name)
#执行结果：
# oldboy

def read1():
    print(666)
from tbjx import name, read1, read2

read1()
#执行结果：
# tbjx模块： 太白金星

from tbjx import name, read1, read2


def read1():
    print(555)
read1()
#执行结果：
# tbjx模块： 666
lst = [28336.5, 8060.0,7659.0, 7762.5, 12124.0, 5040.0, 6480.0, 7555.5, 5400.0, 4320.0  ]
print(max(lst))
print(min((lst)))

##2020年11月绩效奖金最高和最低值（字典中查找）
dic = {'吴恒':28336.5,'马日东':7762.5,'白毅':8060,'时建':7659,'刘万鹏':7762.5,
'杨斌':12124,'宋志明':5040,'刘随强':6480,'王丽':7555.5,'陈杨':5400,'张大志':4320}
print(max(dic))									
print(max(dic.values()))									
print(min(dic.values()))
#找到表中的大小金额和名字	
print(min(zip(dic.values(),dic.keys())))
print(max(zip(dic.values(),dic.keys())))

# dic = {'吴恒':28336.5,'马日东':7762.5,'白毅':8060,'时建':7659,'刘万鹏':7762.5,
# '杨斌':12124,'宋志明':5040,'刘随强':6480,'王丽':7555.5,'陈杨':5400,'张大志':4320}


f = open('员工绩效汇总表2020-11.py','r',encoding ='utf-8')
func = f.read()
print(func)
print(f.readable())#文件是否可读
f.close()

f = open('员工绩效汇总表2020-11.py','r',encoding ='utf-8')
# func = f.read()
# print(func)
print(f.readable())#文件是否可读
print('第一行',f.readline(),end='')#文件是否可读
print('第二行',f.readline(),end='')#文件是否可读
print('第三行',f.readline(),end='')#文件是否可读
#文件是否可读
f.close()


f = open('员工绩效汇总表2020-11.py','r',encoding ='utf-8')
# func = f.read()
# print(func)
print(f.readable())
data = f.readlines()
print(data)#文件是否可读
# print('第一行',f.readline(),end='')#文件是否可读
# print('第二行',f.readline(),end='')#文件是否可读
# print('第三行',f.readline(),end='')
# print（f.readlines()#是否可读
#文件是否可读
f.close()

f = open('员工绩效汇总表2020-11-1.py','w',encoding='utf-8')#这里就覆盖前面的重写内容
# f.read()# not readable
f.write('杨定名\n')
f.write('李卫\n')
f.write('杨俊秋\n')
f.writable()#判断是否可以写入内容
f.writelines(['白毅\n','赵继明\n'])#必须是字符串
f.close()

print(chr(90))
print(ord('a'))#找到表格中的代码

print(pow(2,2))#乘方
print(pow(19,2,3))#乘方19**2 3取余数

#写入增加名字
f = open('员工绩效汇总表2020-11.py','a',encoding='utf-8')#这里就覆盖前面的重写内容
# f.read()# not readable
f.write('杨定名\n')
f.write('李卫\n')
f.write('杨俊秋\n')
f.writable()#判断是否可以写入内容
f.writelines(['白毅\n','赵继明\n'])#必须是字符串
f.close()


f = open('员工绩效汇总表2020-11.py','a',encoding='utf-8')#这里就覆盖前面的重写内容/
f.write('杨定明\n')
f.close()


f = open('员工绩效汇总表2020-11.py','r+',encoding='utf-8')#这里就覆盖前面的重写内容
data = f.read()
print(data)
f.close()


#删除溫晓莹：
f = open('员工绩效汇总表2020-11.py','r',encoding='utf-8')#这里就覆盖前面的重写内容
data = f.readline()#读第一行
# data = f.read()
print(data)
f.close()

f = open('员工绩效汇总表2020-11.py','w',encoding='utf-8')

data = f.writelines(data[0])
# print(data)
f.close()

#追加了白海波
f = open('员工绩效汇总表2020-11.py','a',encoding='utf-8')
data = f.write('白海波')
print(data)
f.close()


l = [1,2,3,4,5,6,7]
print(list(map(str,l)))


#将工资全部累加起来
from functools import reduce

l = [28336.5,7762.5,8060,7659,7762.5,12124,5040,6480,7555.5,5400,4320]
ret = reduce(lambda x,y:x+y,l,30)#设定一个初始值
print(ret)


#将末尾有丽的过滤出来
name = ['吴恒','马日东','白毅','时建',
'刘万鹏','杨斌','宋志明','刘随强','王丽','陈杨','张大志']
res = filter(lambda x:x.endswith("丽"),name)
print(res)
print(list(res))


#将末尾有丽的过滤出来 和前面有刘的过滤出来
name = ['吴恒','马日东','白毅','时建',
'刘万鹏','杨斌','宋志明','刘随强','王丽','陈杨','张大志']
# res = filter(lambda x:x.endswith("丽"),name)
res = filter(lambda x:x.startswith("刘"),name)
print(res)
print(list(res))

#不将末尾有丽的过滤出来 和前面有刘的过滤出来
name = ['吴恒','马日东','白毅','时建',
'刘万鹏','杨斌','宋志明','刘随强','王丽','陈杨','张大志']
# res = filter(lambda x:x.endswith("丽"),name)
res = filter(lambda x: not x.startswith("刘"),name)
print(res)
print(list(res))


name = ['吴恒','马日东','白毅','时建',
'刘万鹏','杨斌','宋志明','刘随强','王丽','陈杨','张大志']
print(list(map(str,name)))


name = open("员工绩效汇总表2020-11.py","r+",encoding='utf-8')
name.write('能改变第一行')
name.close()


#b 这是字节形式
f = open("员工绩效汇总表2020-11.py","rb")#b的方式不能指定编码
data = f.read()
print(data)#b"\xe8\x83\xbd\xe6\x94
#再解码
#b 这是字节形式
f = open("员工绩效汇总表2020-11.py","rb")#b的方式不能指定编码
data = f.read()
print(data)#b"\xe8\x83\xbd\xe6\x94
print(data.decode('utf-8'))#b"\xe8\x83\xbd\xe6\x94
#再解码


f = open("员工绩效汇总表2020-11.py","wb")#b的方式不能指定编码
f.write(bytes('111111\n',encoding='utf-8'))
f.write(('杨建'.encod('utf-8')))


f = open("员工绩效汇总表2020-11","w",encoding='utf-8')
print(f.closed)#判断是否关闭
f.encoding
print(f.encoding) #系统编码

f = open("员工绩效汇总表2020-11.py","r",encoding='utf-8')
data = f.read()#判断是否关闭
print(data)



f = open("员工绩效汇总表2020-11.py","r+",encoding='latin-1')
data = f.read()#判断是否关闭
print(data)
f.write('ssssff')

f.flush()
print(f.tell())

print(f.readline())

prin(f.readline())

f1 = open('seek.txt','rb')
print(f1.tell())
f1.seek(10,0)
print(f1.tell())
f1.seek(4,1)
print(f1.tell())


f1 = open('seek.txt','rb')
print(f1.tell())
f1.seek(-5,2)#从开头算起
print(f1.read())
print(f1.tell())
f1.seek(4,1)
print(f1.tell())#tell光标位置


f1 = open('seek.txt','rb')
data = f.readlines()
print(data[-1].decode('utf-8'))#读取最后一行

# f = open('seek.py','rb')
# for i in f:
#     print(i)
f = open('seek.txt','rb')
for i in f:
    offs = -8
    while True:
        f.seek(offs,2)
        data = f.readline()
        if len(data)>1:
            print('文件的最后一行是%s'%(data[-1].decode('utf-8')))
            break
        offs*=2#取最后一行


l = [1,2,3,4,5]
for i in l:#__next__()每次执行
    print(i)

x = 'hello'
# print(dir(x)) #可以迭代
iter_test = x.__iter__()
print(iter_test)
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())#没有报错


l = [1,2,3,4,5]
# print(l[0])
iter_l = l.__iter__()
print(iter_l.__next__())


l = [1,2,3,4,5]
index = 0
while index<len(l):
    print(l[index])
    index+=1
    pass          

set = {1,2,3}
# for i in set:
#     print(i)  
iter_set = set.__iter__()
print(iter_set.__next__())
print(iter_set.__next__())
print(iter_set.__next__())

dic = {'a':1,'b':2,'c':3}
# for i in set:
    # print(i)  
iter_dic = dic.__iter__()
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())#取的是keys


dic = {'a':1,'b':2,'c':3}
# for i in set:
    # print(i)  
iter_dic = dic.__iter__()
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())

f = open('seek.txt','r+')
iter_f = f.__iter__()
print(iter_f.__next__(),end='')
print(iter_f.__next__(),end='')
print(iter_f.__next__(),end='')

l = ['吴恒','erzi','sunzi','chunsun']
iter_l = l.__iter__()#地址
# print(iter_l)
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())
print(next(iter_l))
print(next(iter_l))
print(next(iter_l))
print(next(iter_l))


def test():
    yield '吴恒'
    yield 2
    yield 3
g = test()
print(g)
# g.__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())


#三元表达式
# name= '吴恒'
name= 'linhai  feng'
# if name == '吴恒':
res = 'SB' if name == '吴恒' else '帅哥'
print(res)


# 列表解析
egg_list = []
for i in range(10):
    egg_list.append('吴恒%s'%i)
print(egg_list)

高级方法解析生成器
# l = ['吴恒%s'%i for i in range(10) ]
l = ['吴恒%s'%i for i in range(10)]
l1 = ['吴恒%s'%i for i in range(10) if i>5]
l2 = ['吴恒%s'%i for i in range(10) if i<5]
l3 = ['吴恒%s'%i for i in range(10) ]
print(l)
print(l1)
print(l2)
print(l3)
上面太占内存


生成器表达式和列表推导式的区别
laomuji = ('吴恒%s'%i for i in range(10))#改成括号 
print(laomuji)#内存地址
# print(laomuji.__next__())#内存地址
# print(laomuji.__next__())#内存地址
# print(laomuji.__next__())#内存地址
# print(laomuji.__next__())#内存地址
# print(laomuji.__next__())#内存地址
# print(laomuji.__next__())#内存地址
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))
print(next(laomuji))


sum = (x**2+3 for x in range(4))
print(sum)
print(next(sum))
print(next(sum))
print(next(sum))
print(next(sum))

生成器表达式和列表推导式的语法基本上一样的
sum(i for i in range(100000))
print(sum)
print(sum(i for i in range(100000)))


[i for i in range(10)]


生成器表达式
mm = (i for i in range(10))
print(mm)
print(next(mm))
print(next(mm))
print(next(mm))
print(next(mm))
print(next(mm))

生成器函数
# mm = (i for i in range(10))
def test():
    yield '我'
    # yield '儿子'
    # yield '孙子
    yield 3
    yield 5
res = test()
print(res)
# print(next(res))
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(next(res))
print(next(res))
# print(next(res))




def test():
    # return '我'
    # yield '儿子'
    # yield '孙子
    return 3
    return 5
res = test()
print(res)
# print(next(res))
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(next(res))
print(next(res))

生产包子
def shenchan_baozi():
    ret = []
    for i in range(100):
        ret.append('一屉包子%s'%i)
    return ret
baozi_list = shenchan_baozi()
print(baozi_list)

准备边做边卖
def shenchan_baozi():
    # ret = []
    for i in range(100):
        # ret.append('一屉包子%s'%i)
        print('开始生产包子')
        yield '一屉包子%s'%i
        # print('开始卖包子')
pro_g = shenchan_baozi()
baozi1 = pro_g.__next__()
baozi2 = pro_g.__next__()
baozi3 = pro_g.__next__()
baozi4 = pro_g.__next__()
print('来的人开始吃',baozi1)
print('开始卖包子')
print('来的人开始吃',baozi2)
print('开始卖包子')
print('来的人开始吃',baozi3)
print('开始卖包子')
print('来的人开始吃',baozi4)

# day19-03
def xiadan():
    res = []
    for i in range(100):
        res.append('鸡蛋%s'%i)
    return res
print(xiadan())#占空间大 效率低

# 效率高 内存小
def xiadan():
    # res = []
    for i in range(100):
        yield '鸡蛋%s'%i
        # res.append('鸡蛋%s'%i)

    # return res
# print(xiadan())#占空间大 效率低
alex_jd = xiadan()
# alex_jd1 = xiadan()
jidan = alex_jd.__next__()
print('wuheng',jidan)
jidan1 = alex_jd.__next__()
print('wuheng1',jidan1)
jidan2 = alex_jd.__next__()
print('wuheng2',jidan2)

 
import time


def produce():#生产包子
    ret = []
    for i in range(100):
        time.sleep(0.1)
        ret.append('包子%s'%i)
    return ret
def cousumer(res):#吃包子
    for index,baozi in enumerate(res):
        time.sleep(0.1)
        print('第%s个人，吃了%s'%(index,baozi))
res = produce()
enumerate(res)


def test():
    print('开始啦')
    yield 1
    print('第一次')
    yield 2
    print('第二次')
t = test()
# print(t)
res = t.__next__()
print(res)
# t.__next__()
# t.send(None)
# t.send(3)
res = t.__next__()
print(res)
res = t.__next__()
# print(res)

# print(next(res))
# print(next(res))

def test():
    print('开始啦')
    first = yield 
    print('第一次',first)
    yield 2
    print('第二次')
t = test()
# print(t)
res = t.__next__()
print(res)
# t.__next__()
res = t.send('函数停留在first位置，我就是给first赋值的')
print(res)









def cousumer(name):#吃包子
        print('我是[%s],我准备开始吃包子了'%name)
        while True:
            baozi1 = yield
            print('[%s]很开心的把"%s"包子吃了。'%(name,baozi1))
# c1 = cousumer('吴恒')
# c1.__next__()
# c1.send('屎粑粑馅')
def producer():
    c1 = cousumer('吴恒')
    c1.__next__()
    c1.send('屎粑粑馅')
producer()


bool(None)
bool(3)
bool('anng')
bool([2,5])
bool('')
bool(0)


l1 = [11,22,33]
l2 = [22,33,44]
ret  = set(l1)&set(l2)
print(ret)


def f(name,age,sex):
    pass
f('吴恒',50,'男')
f('马日东',38,'男')
f('王丽',37,'女')
f('杨斌',40,'男')
f('刘万鹏',53,'男')
f('时建',64,'男')
print(f)


def func(x,y,z):
    print(x,y,z)
func(1,2,3)
  


def func(x,z,y=5):
    print(x,y,z)
func(1,4,3)



def func(x,*y,**z):
    print(x,y,z)
func(1,2,3)


def func(x,*y,**z):
    print(x,y,z)
func(1,name='吴恒',age=19)


def func(*y,**z):
    print(y,z)
func([1,2,3,4,5])


def func(*y,**z):
    print(y,z)
func(*[1,2,3,4,5])

def func(*y,**z):
    print(y,z)
func(*[1,2,3,4,5],name='吴恒',age=50)


def func(*y,**z):
    print(y,z)
func(*[1,2,3,4,5],**{'name':'吴恒','age':50})
func(*[1,2,3,4,5],{'name':'吴恒','age':50})
func([1,2,3,4,5],**{'name':'吴恒','age':50})


def func1(x=1,*y,**z):
    print(x,y,z)#1 () {'name': '吴恒'}
    return y #()
    print(x)#return  结束了x没有打印
def func2(arg):
    ret = func1(name=arg)
    print(ret)
result = func2('吴恒') #x=吴恒=arg x =name
print(result)


def func(arg):
    arg.append(55)
li = [11,22,33,44,66]
func(li)
print(li)#[11, 22, 33, 44, 66, 55]
li = func(li)
# li2 = func(li)
print(li)
# print(li2)


def f1(arg):#8
    print(arg+100)#8
def f2(arg ):#7
    ret = f1(arg+1)#7
    print(arg)#78
ret = f2(7)
print(ret)


def func(a1):#10
    return a1+100 #110
func = lambda a1:a1+200#210
ret = func(10)
print(ret)


s = '吴恒'
print(type(s))


s = '吴恒'
a = bytes(s,'utf-8')#字节
s.encode('utf-8')#二进制


#zip用法：
l1 = ['wuheng',11,33,55,44]
l2 = ['is',11,33,55,44]
l3 = ['good',11,33,55,44]
l4 = ['guy',11,33,77,44]
# print('__'.join(list(zip(l1,l2,l3,l4))[0]))
print('__'.join(list(zip(l1,l2,l3,l4))[0]))



def func(a1):#1111111
    print(id(a1))
n =11111
print(id(n))
func(n)
# 2518486075568
# 2518486075568



name_1 = ['吴恒','陈燕']#全局变量
def func():
    name_1 = 123
func()
print(name_1)


name_1 = ['吴恒','陈燕']#全局变量
def func():
    global name_1 #声明123为全局变量
    name_1 = 123
func()
print(name_1)


name_1 = ['吴恒','陈燕']#全局变量
def func():
    name_1.append('杨斌')
func()
print(name_1)



name_1 = ['吴恒','陈燕']#全局变量
def func():
    name_1 = 123
    global name_1 #声明第一个为全局变量
func()
print(name_1)
   
name = '吴恒'
def func():
    name = '王丽'
    def outer():
        name = '马日东'
        def inner():
            global name
            name = '蒙蔽了'
        print(name)
    print(name)
print(name)
ret = func()
print(ret)
print(name)



name = '吴恒'
def func():
    name = '王丽'
    def outer():
        name = '马日东'
        def inner():
            nonlocal name#nonloca取消全局变量 成马日东
            name = '蒙蔽了'
            print(name)
        inner()
    o = outer#没有返回值    
    print(o)
    print(name)
ret = func()
print(ret)
print(name)



name = '苍老师'
def outer(func):
    name = '吴恒'#没有执行
    func()#就是执行了show
def show():
    print(name)
outer(show)

# day19-07 -->1:00
s = '吴恒'
print(type(s))


name = '苍老师'
def outer():
    name = '吴恒'#没有执行
    def inner():
        print(name)
    return inner()
ret = outer()
print(ret)


name = '苍老师'
def outer():
    name = '吴恒'#没有执行
    def inner():
        print(name)
    return inner
ret = outer()
ret()
print(ret)
result = ret()
print(result)



name = '苍老师'
def outer():
    name = '吴恒'#没有执行
    def inner():
        print(name)
    return inner#返回内存地址
ret = outer()
ret()
print(ret)
result = ret()#执行inner函数打印吴恒
print(result)#无返回值 打印none



name = '苍老师'
def outer(func):
    name = '吴恒'#没有执行
    def inner():
        print(name)
    return inner#返回内存地址
ret = outer()
ret()
print(ret)
result = ret()#执行inner函数打印吴恒
print(result)

#1*2*3*4*4*5*6*7*8 的阶乘
# n*(n-1)*...1#倒着来的8 7 6 5 4 3 2 1
def f(n):
    if n == 1:
        return 1
    return n*f(n-1)#8*f(7) 8*f(7) 7*f(6) 6*f(5)   ...2*1
f(8)


#文件的写法有这种
with open('员工绩效汇总表2020-11.py','r') as x,open('员工绩效汇总表2020-11.py','w') as y:
    y.write(x.read())


sum(i for i in range(10000))

def xiadan():
    for i in range(10):

        yield '鸡蛋%s'%i
alex_lmy = xiadan()
print(alex_lmy.__next__())
print(alex_lmy.__next__())
print(alex_lmy.__next__())
print(alex_lmy.__next__())
print(alex_lmy.__next__())
print(alex_lmy.__next__())
print(alex_lmy.__next__())



def get_poluation():
    ret = []
    with open('人口普查','r',encoding='utf-8') as f:
        for i in f:
            ret.append(i)
    return ret
print(get_poluation())


def get_poluation():
    # ret = []
    with open('人口普查.py','r',encoding='utf-8') as f:
        for i in f:
            yield(i)
    # return ret
print(get_poluation())
g = get_poluation()
print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
si = eval(g.__next__())
# print(type(s1)
print(si['poluation'])


def get_poluation():
    # ret = []
    with open('人口普查.py','r',encoding='utf-8') as f:
        for i in f:
            yield(i)
    # return ret
print(get_poluation())
g = get_poluation()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# si = eval(g.__next__())
# # print(type(s1)
# print(si['poluation'])
res = 0
for p in g:
    p1_dic = eval(p)
    print(p1_dic['poluation'])
    res+=p1_dic['poluation']
print(res)




def get_poluation():
    # ret = []
    with open('人口普查.py','r',encoding='utf-8') as f:
        for i in f:
            yield(i)
    # return ret
print(get_poluation())
g = get_poluation()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# si = eval(g.__next__())
# # print(type(s1)
# print(si['poluation'])
# res = 0
# for p in g:
#     p1_dic = eval(p)
#     print(p1_dic['poluation'])
#     res+=p1_dic['poluation']
# print(res)
all_pop = sum(eval(i)['poluation'] for i in g)
print(all_pop)

# day19-04
def test():
    yield 1
    yield 2
t = test()


def run():
    print('from run')#太慢  不停顿
    print('from run')
    print('from run')
    print('from run')
run()


def run():
    print('from run')#太慢  不停顿
    yield 1#停顿了
    print('from run')
    yield 2
    print('from run')
    yield 3
    print('from run')
t = run()
next(t)
print('sssffff ')
print('sssffff ')
print('sssffff ')
print('sssffff ')
print('sssffff ')

next(t)# 从yield 2 在开始跑
# t.__next__()  三个方法
# t.send('123')

def test():
    for i in range(4):
        yield i
# t = test()


#三元
age = 10 
res = True if age>10 else False

l = ['a' for i in range(10)] 

g_l = ('a' for i in range(10))


def test():
    for i in range(4):
        yield i
t = test()
# for i in t:
# #     print(i)
# tl = (i for i in t)
# print(list(tl))


t1 = (i for i in t)
t2 = (i for i in t1)
print(list(t1))
print(list(t2))


#装饰器
# 1 不修改被修改函数的源代码、
# 2 不修改被修饰函数的
import time
def cal(l):
    start_time = time.time()
    res = 0
    for i in l:
        time.sleep(0.1)
        res+= i 
    stop_time = time.time() 
    
    print('运行时间%s'%(stop_time-start_time))
    return res
print(cal(range(100)))
def index():
    pass
def home():
    pass
# day20-02


def foo():
    print('你好形式福')
def test(func):
    print(func)
    func()
test(foo)

#高阶函数
import time
def foo():
    time.sleep(3)
    print('你好形式福')
def test(func):
    print(func)
    start_time = time.time()
    func()
    stop_time = time.time()
    print('函数运行时间是%s'%(stop_time-start_time))
test(foo)
import time
def foo():
    time.sleep(3)
    # print('你好形式福')
def test(func):
    print(func)
    start_time = time.time()
    func()
    stop_time = time.time()
    print('函数运行时间是%s'%(stop_time-start_time))
# foo()
test(foo)


def foo():
    print('from the foo')
def test(func):
    return func
# res = test(foo)
#  print(res)
# res() 
foo = test(foo)
foo()



import time
def foo():
    time.sleep(2)
    print('来自foo')
#不修改foo源代码
#不修改foo调用方式
def timer(func):
    print(func)
    start_time = time.time()
    return func
    stop_time = time.time()
    print('函数运行时间是%s'%(stop_time-start_time))
foo = timer(foo)
foo()
# 6091号已经结算完成，其他4个还没有结算在施工状态。


def bar():
    print('from bar')
def foo():
    print('from foo')
    def test():
        pass


def father(name):
    # print('from father %s'%name)
    def son():
        # name = '林海峰'
        print('我的爸爸是%s'%name)
    
        def grandson():
            print('就是我自己')
            print('我的爷爷是%s'%name)

        grandson()
    # print(locals())#当前层的局部变量
    son()
# father('alex')
father('wuheng')



def father(name):
    # print('from father %s'%name)
    def son():
        # name = '林海峰'
        print('我的爸爸是%s'%name)
    
        def grandson():
            # print('就是我自己')
            print('我的爷爷是%s'%name)

        grandson()
    # print(locals())#当前层的局部变量
    son()
# father('alex')
father('wuheng')



def father(auth_type):
    # print('from father %s'%name)
    def son():
        # name = '林海峰'
        # print('我的爸爸是%s'%name)
    
        def grandson():
            # print('就是我自己')
            print('我的爷爷是%s'%auth_type)

        grandson()
    # print(locals())#当前层的局部变量
    son()
# father('alex')
father('filedb')





import time
def timer(func):#func =test
    def wrapper():
        # print(func)
        start_time = time.time()
        func()#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
    return wrapper
def test():
    time.sleep(3)
    print('test函数运行完毕')
res = timer(test)# 返回wrapper的地址
res()#执行wrapper



import time
def timer(func):#func =test
    def wrapper():
        # print(func)
        start_time = time.time()
        func()#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
    return wrapper
def test():
    time.sleep(3)
    print('test函数运行完毕')
test = timer(test)# 返回wrapper的地址
test()#执行wrapper


import time
def timer(func):#func =test
    def wrapper():
        # print(func)
        start_time = time.time()
        func()#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
    return wrapper
def test():
    time.sleep(3)
    print('test函数运行完毕')
# test = timer(test)# 返回wrapper的地址
# test()#执行wrapper



#@timer 就相当于test = timer(test)
import time
def timer(func):#func =test
    def wrapper():
        # print(func)
        start_time = time.time()
        func()#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
    return wrapper
@timer 
def test():
    time.sleep(3)
    print('test函数运行完毕')
# test = timer(test)# 返回wrapper的地址
test()#执行wrapper





import time
def timer(func):#func =test
    def wrapper():
        start_time = time.time()
        func()#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
        return 'wuheng'
    return wrapper
@timer #就相当于test = timer(test)
def test():
    time.sleep(3)
    print('test函数运行完毕')
    return #test 的返回值
res = test()
print(res)



import time
def timer(func):#func =test
    def wrapper(name,age):
        start_time = time.time()
        func(name,age)#就是运行test
        stop_time = time.time()
        print('运行时间就是%s'%(stop_time-start_time))
        return '吴恒'
    return wrapper
@timer #就相当于test = timer(test)
def test(name,age):
    time.sleep(3)
    print('test函数运行完毕')
    return #test 的返回值
res = test('wuheng',51)
print(res)


# import time
# def timer(func):#func =test
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)#就是运行test
#         stop_time = time.time()
#         print('运行时间就是%s'%(stop_time-start_time))
#         return res
#     return wrapper
# @timer #就相当于test = timer(test)
# def test1(name,age,gender):
#     time.sleep(3)
#     print('test函数运行完毕。姓名是%s,年龄是%s,性别是%s。'%(name,age,gender))
#     return #test 的返回值
# # res = test1('wuheng',51)
# res = test1('wuheng',51,'男')
# print(res)

# def wrapper(*args,**kwargs):
#     print(args)
#     print(kwargs)
# # wrapper(1,2,3,45,name = 3)
# wrapper(*(1,2,3,45),**{'name':'wuheng'})

def wrapper1(name, age, gender):
    print(name)
    print(age)
    print(gender)
def wrapper(*args, **kwargs):
    wrapper1(*args, **kwargs)
    # wrapper(*args,**kwargs)
    # print(args)
    # print(kwargs)
# wrapper1('wuheng',54,'男')
wrapper1('wuheng', 67, '男')




def index():
    pass
def home():
    pass
def shopping_car():
    pass
def order():
    pass





# def auth_func(func):
#     def wrapper(*args,**kwargs):
#         user_name = input('用户名').strip()
#         password = input('密码:').strip()
#         if user_name == 'wuheng' and password == '123':
#             res = func(*args,**kwargs)
#             return res
#         else:
#             print('用户名或密码错误')
#     return wrapper

# @auth_func
# def index():
#     print('欢迎来到京东主页')
# @auth_func
# def home(name):
#     print('欢迎回家')
# @auth_func
# def shopping_car(name):
#     print('%s购物车里有[%s,%s,%s]'%(name,'奶茶','面包','键子'))
# index()
# home('产品经理')
# shopping_car('产品经理')


user_dic = {'user_name':None,'login':False}



def auth_func(func):
    def wrapper(*args,**kwargs):
        user_name = input('用户名').strip()
        password = input('密码:').strip()
        if user_name == 'wuheng' and password == '123':
            res = func(*args,**kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

# @auth_func
# def index():
#     print('欢迎来到京东主页')
# @auth_func
# def home(name):
#     print('欢迎回家')
# @auth_func
# def shopping_car(name):
#     print('%s购物车里有[%s,%s,%s]'%(name,'奶茶','面包','键子'))
# index()
# home('产品经理')
# shopping_car('产品经理')






user_dic = {'user_name':None,'login':False}
def auth_func(func):
    def wrapper(*args, **kwargs):
            if user_dic['user_name'] and user_dic['login']:
                res = func(*args, **kwargs)
                return res
            user_name = input('用户名:').strip()
            password = input('密码:').strip()
            if user_name == 'wuheng' and password == '123':
                user_dic['user_name'] = user_name
                user_dic['login'] = True
                res = func(*args, **kwargs)
                return res
            else:
                print('用户名或密码错误')
    return wrapper
@auth_func
def index():
    print('欢迎来到京东主页')
@auth_func
def home(name):
    print('欢迎回家')
@auth_func
def shopping_car(name):
    print('%s购物车里有[%s,%s,%s]' % (name, '奶茶', '面包', '键子'))
index()
home('产品经理')
shopping_car('产品经理')
     
#day20-010 :16 

uesr_list = [{'name':'吴恒','password':'123'},{'name':'马日东','password':'123'}]



current_dic = {'user_name':None,'login':False}
def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            print('认证类型是',auth_type)
            if current_dic['user_name'] and current_dic['login']:
                res = func(*args, **kwargs)
                return res  
            user_name = input('用户名:').strip()
            password = input('密码:').strip()
            for user_dic in uesr_list:
                if user_name == user_dic['name']and password == user_dic['password']:
                    current_dic['user_name'] == user_name
                    current_dic['login'] == True                    
                    res = func(*args, **kwargs)
                    return res 
            else:
                print('用户名或密码错误')
        return wrapper      
    return auth_func
@auth(auth_type='filedb')#auth(auth_type='filedb')=auth_func--->auth_func   附加了auth_type
def index():
    print('欢迎来到京东主页')
# @auth_func
# def home(name):
#     print('欢迎回家')
# @auth_func
# def shopping_car(name):
#     print('%s购物车里有[%s,%s,%s]' % (name, '奶茶', '面包', '键子'))
print('前',current_dic)
index()
# print('后',current_dic)
# home('产品经理')
# shopping_car('产品经理')    




uesr_list = [{'name':'吴恒','password':'123'},{'name':'马日东','password':'123'}]
current_dic = {'user_name':None,'login':False}
def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            print('认证类型是',auth_type)
            if auth_type == 'filedb':
                if current_dic['user_name'] and current_dic['login']:
                    res = func(*args, **kwargs)
                    return res  
                user_name = input('用户名:').strip()
                password = input('密码:').strip()
                for user_dic in uesr_list:
                    if user_name == user_dic['name']and password == user_dic['password']:
                        current_dic['user_name'] == user_name
                        current_dic['login'] == True                    
                        res = func(*args, **kwargs)
                        return res 
                else:
                    print('用户名或密码错误')
            elif auth_type == 'ldap':
                print('我不会玩了')
            else:
                print('不知道什么类型')
        return wrapper      
    return auth_func
@auth(auth_type='filedb')#auth(auth_type='filedb')=auth_func--->auth_func   附加了auth_type
def index():
    print('欢迎来到京东主页')
@auth(auth_type='ldap')
def home(name):
    print('欢迎回家')
@auth(auth_type='ssssss')
def shopping_car(name):
    print('%s购物车里有[%s,%s,%s]' % (name, '奶茶', '面包', '键子'))
print('前',current_dic)
index()
# print('后',current_dic)
home('产品经理')
shopping_car('产品经理')  






def fetch(data):#查
    print('这是查询功能')
    print('用户输入的是',data)
def add():#加
# def change():#改

# def delete():#关键字
# if __name__ == '__main__':
    # print(__name__)
    # print('test')
# __name__ == '__main__'
    mag = '''
        1.查询
        2.添加
        3.修改
        4.删除
        5.退出'''
    msg = {'1':fetch,'2':add,'3':change,'4':delete,'5':exit}
    while True:
        print(msg)
        choice = input('请输入你的选项:').strip()
        if not choice:Continue
        if choice =='5':break
        data = input('请输入您的数据').strip()
        msg_dic[choice](data)

#上面这个没有做出来
# 我想开发新的短视频节目
#又是增加了约饭的平台
 2222商城50%












            



