# 工作实际运用
# 计算读取文件的速度，但暂时要将文件内容复制黏贴在程序文件中，这样的办法不行必须是手动输入才能够使用计算时间
from functools import reduce
import time


def func():
    print('嘻嘻哈哈等你们来这里')


start_time1 = time.time()
time.sleep(0.1)
func()
end_time1 = time.time()
print('......执行效率%s' % (end_time1-start_time1))


# 2020年11月绩效奖金最高和最低值
# 保存为utf-8格式 在cmd中打开python 在输入才能完成。
lst = [28336.5, 8060.0, 7659.0, 7762.5, 12124.0,
    5040.0, 6480.0, 7555.5, 5400.0, 4320.0]
print(max(lst))
print(min((lst)))


# 2020年11月绩效奖金最高和最低值（字典中查找）
dic = {'吴恒': 28336.5, '马日东': 7762.5, '白毅': 8060, '时建': 7659,
'刘万鹏': 7762.5, '杨斌': 12124, '宋志明': 5040, '刘随强': 6480, '王丽': 7555.5, '陈杨': 5400, '张大志': 4320}
print(max(dic))
print(max(dic.values()))
print(min(dic.values()))
# 找到表中的大小金额和名字
print(min(zip(dic.values(), dic.keys())))
print(max(zip(dic.values(), dic.keys())))

# 陈粒.py  员工名字和金额字典
f = open('员工绩效汇总表2020-11.py', 'r', encoding='utf-8')
func = f.read()  # 读取字典
print(func)
print(f.readable())  # 文件是否可读
f.close()

# 每行读取员工绩效奖金
f = open('员工绩效汇总表2020-11.py', 'r', encoding='utf-8')
# func = f.read()
# print(func)
print(f.readable())  # 文件是否可读
print('第一行', f.readline(), end='')  # 文件是否可读
print('第二行', f.readline(), end='')  # 文件是否可读
print('第三行', f.readline(), end='')  # 文件是否可读
print('第四行', f.readline(), end='')  # 文件是否可读
print('第五行', f.readline(), end='')  # 文件是否可读
print('第六行', f.readline(), end='')  # 文件是否可读
print('第七行', f.readline(), end='')  # 文件是否可读
print('第八行', f.readline(), end='')  # 文件是否可读
print('第九行', f.readline(), end='')  # 文件是否可读
print('第十行', f.readline(), end='')  # 文件是否可读
print('第十一行', f.readline(), end='')  # 文件是否可读
# 文件是否可读
f.close()


# 打印所有的行汇总
f = open('员工绩效汇总表2020-11.py', 'r', encoding='utf-8')
# func = f.read()
# print(func)
print(f.readable())
data = f.readlines()
print(data)
f.close()


# 一点击写就覆盖了原来的内容这里非常要注意
f = open('员工绩效汇总表2020-11.py', 'r', encoding='utf-8')
f.read()  # not readable
f.close()


# 在新的文件中写入新的人名
f = open('员工绩效汇总表2020-11-1.py', 'w', encoding='utf-8')
f.writable()  # 判断是否可以写入内容
f.write('杨定名\n')
f.write('李卫\n')
f.write('杨俊秋\n')
# 再安行添加内容但要\n
f.writelines(['白毅\n', '赵继明\n'])  # 必须是字符串
f.close()


# 在新的文件中写入新的人名
f = open('员工绩效汇总表2020-11-1.py', 'w', encoding='utf-8')
f.writable()  # 判断是否可以写入内容
f.write('杨定名\n')
f.write('李卫\n')
f.write('杨俊秋\n')
# 再安行添加内容但要'\n'
f.writelines(['白毅\n', '赵继明\n'])  # 必须是字符串
f.close()

# 写入增加名字
f = open('员工绩效汇总表2020-11.py', 'a', encoding='utf-8')  # 这里就覆盖前面的重写内容
# f.read()# not readable
f.write('杨定名\n')
f.write('李卫\n')
f.write('杨俊秋\n')
f.writable()  # 判断是否可以写入内容
f.writelines(['白毅\n', '赵继明\n'])  # 必须是字符串
f.close()


f = open('员工绩效汇总表2020-11.py', 'a', encoding='utf-8')  # 这里就覆盖前面的重写内容
f.write('杨定名\n')
f.close()
# 能读能写
f = open('员工绩效汇总表2020-11.py', 'r+', encoding='utf-8')  # 这里就覆盖前面的重写内容
data = f.read()
print(data)
f.close()

f = open('员工绩效汇总表2020-11.py', 'r+', encoding='utf-8')  # 这里就覆盖前面的重写内容
data = f.read()
print(data)

f = open('员工绩效汇总表2020-11.py', 'r+', encoding='utf-8')  # 这里就覆盖前面的重写内容
data = f.read()
print(data)
data = f.write('溫晓莹\n')
print(data)
f.close()

# 追加了白海波
f = open('员工绩效汇总表2020-11.py', 'a', encoding='utf-8')
data = f.write('白海波')
print(data)
f.close()

# 按行读取和按全部读取
f = open('员工绩效汇总表2020-11.py', 'r', encoding='utf-8')  # 这里就覆盖前面的重写内容
# data = f.readline()#读第一行
data = f.read()
print(data)
f.close()

# 这里不用再写不会
with open('timelog1.txt', 'r+') as f:
    f.writelines('2234rt\n')

# 把工资处理成字符串
l = [28336.5, 7762.5, 8060, 7659, 7762.5,
    12124, 5040, 6480, 7555.5, 5400, 4320]
print(list(map(str, l)))

# 将工资全部累加起来
l = [28336.5, 7762.5, 8060, 7659, 7762.5,
    12124, 5040, 6480, 7555.5, 5400, 4320]
ret = reduce(lambda x, y: x+y, l, 30)  # 设定一个初始值
print(ret)

# 将末尾有丽的过滤出来 和前面有刘的过滤出来
name = ['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
# res = filter(lambda x:x.endswith("丽"),name)
res = filter(lambda x: x.startswith("刘"), name)
print(res)
print(list(res))


# 不将末尾有丽的过滤出来 和前面有刘的过滤出来
name = ['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
# res = filter(lambda x:x.endswith("丽"),name)
res = filter(lambda x: not x.startswith("刘"), name)
print(res)
print(list(res))

# b 这是字节形式读取
f = open("员工绩效汇总表2020-11.py", "rb")  # b的方式不能指定编码
data = f.read()
print(data)  # b"\xe8\x83\xbd\xe6\x94
# 再解码字节变成utf-8
print(data.decode('utf-8'))  # b"\xe8\x83\xbd\xe6\x94

# 监理人员列表变为元组
list = ['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨''张大志']


def func(*args):
    print(args)


func(*list)

# 监理人员字典变为字典
dic = {'吴恒': 28336.5, '马日东': 7762.5, '白毅': 8060, '时建': 7659,
'刘万鹏': 7762.5, '杨斌': 12124, '宋志明': 5040, '刘随强': 6480, '王丽': 7555.5, '陈杨': 5400, '张大志': 4320}


def func(**kwargs):
    print(kwargs)


func(**dic)

# 监理人名字代换 传参


def eat(food, drink):
    print(food, drink)


eat('吴恒', '马日东')

# 调用吴恒


def fun():
    a = '吴恒'
    print(a)


fun()
# print(a)  # 不存在了


# 函数调用吴恒   马日东
def func():
    a = '吴恒'
    print(a)


func()
a = '马日东'
print(a)

# 输入吴恒 马日东  全局变量调出方法，再变成字典


def func():
    a = '吴恒'
    b = '马日东'
    print('王丽')
    print(globals())
    print(locals())


func()

# 双函数的循环和调用


def func1():
    print('吴恒')


def func2():
    print('马日东')
    func1()


func2()
print('吴恒')


# 双函数的循环和调用 名字
def fun2():
    print('吴恒')

    def fun3():
        print('马日东')
    print('王丽')
    fun3()
    print('陈杨')


print('陈杨')
fun2()
print('时建')

# 陈杨  吴恒    王丽  马日东     陈杨  时建

# 列表中增加杨斌
list = ['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '宋志明', '刘随强', '王丽', '陈杨''张大志']


def func():
    list.append('杨斌')
    print(list)


func()
print(list)


# 声明不是全局变量
a = '吴恒'


def func1():
    a = '马日东'

    def func2():
        nonlocal a  # 声明不是全局变量
        a = '刘随强'
        print(a)
    func2()
    print(a)


func1()
a = '吴恒'

# 使用全局变量


def func1():
    a = '吴恒'

    def func2():
        # nonlocal a
        a = '刘随强'
        print(a)
    func2()
    print(a)


func1()


a = '吴恒'


def func_1():
    a = '马日东'

    def func_2():
        nonlocal a  # 非局部变量
        a = '王丽'

        def func_3():
            a = '时建'
            print(a)
        print(a)
        func_3()
        print(a)
    print(a)
    func_2()
    print(a)


print(a)  # 吴恒
func_1()
print(a)  # 吴恒
# 马日东
# 王丽
# 时建
# 王丽
# 王丽


# 数字相加
n = 13
print(eval('n+2'))
n = 9
print(eval('2+n'))


# 函数变成了字符串
def func():
    print(666)


eval('func()')

# 中间插入分隔符  换行
print('您好')
print('您好', '我好', sep='|')
print('您好', '我好', end='')
print('您好', '我好')


# 哈西值能够找到每次运行的内存位置
print(hash('你好'))

# 帮助
help(print)

# 请求是否成立
print(callable(print))


# 绝对值
print(abs(-1))


# 返回元组
print(divmod(98, 5))
print(divmod(98, 4))
print(divmod(2, 1))
print(divmod(2, 1.33))
print(divmod(2, -4))

# pow(a, b) 求a的.\b次幂, 如果有三个参数. 则求完次幂后对第三个数取余
print(pow(17, 2, 8))
print(pow(34, 2, 9))
print(pow(45, 5, 2))
print(pow(17, 7, 8))
print(pow(17, 2, 4))
print(pow(17, 2, 83))
# pow(x,y,z)：这个是表示x的y次幂后除以z的余数>>> pow(2,4,5)

#  sum() 求和
print(sum([98223, 42254, 535326, 808777]))  # sum里边的参数是一个可迭代对象
print(sum([98355, 48656, 5655776, 8244557]))  # sum里边的参数是一个可迭代对象
print(sum([9123352, 24454, 5256, 87]))  # sum里边的参数是一个可迭代对象
print(sum([98, 45654, 56, 12387]))  # sum里边的参数是一个可迭代对象
print(sum([98, 4, 7756, 834547]))  # sum里边的参数是一个可迭代对象
print(sum([9348, 4568, 5689, 8724423]))  # sum里边的参数是一个可迭代对象


# max() 求最大值
print(max([984433, 4334, 565565, 3345587]))
print(max([96684433, 4335554, 56555565, 33455555587]))
print(max([9844336433, 4334, 565565, 3345555587]))
print(max([9832254433, 433433334, 5355565565, 333454335587]))
print(max([98443446773, 43347777, 565567775, 334558688897]))
print(max([984433, 4334, 56556533433, 334888765587]))


# list() 将一个可迭代对象转换成列表  re
li = reversed('你好')
print(list(li))
li_1 = reversed('你好')
print(list(li_1)
li_2=reversed('你好')
print(list(li_2))
li_3=reversed('你好')
print(list(li_3))

# 右对齐
print(format("你好", '>20'))
# 左对齐
print(format("你好", '<20'))  # 左对齐
# 居中
print(format("你好", '^20'))
# 二进制
print(format(3, 'b'))
# 转换成 字符串
print(type(format(78, 'c')))
# 十进制
print(type(format(111, 'd')))
# 和d一样
print(type(format(45)))
# 十进制
print(type(format(23, 'n')))
# 八进制
print(type(format(327, 'o')))
# 十六进制(小写字母)
print(type(format(2378, 'x')))
print(type(format(2378, 'X')))


print(format(1234567890, 'e'))  # 科学计算法,默认使用6位
print(format(1234567890, '0.2e'))  # 科学计算,保留2位小数(小写)
print(format(1234567890, '0.2E'))  # 科学计算,保留2位小数(大写)
print(format(1234567890, 'f'))  # 小数点计数法,保留6位小数
print(format(1234567890, '0.2f'))  # 小数点计数法,保留2位小数)
print(format(1234567890, '0.10f'))  # 小数点计数法,保留2位数
print(format(1.23456789e+1000, 'F'))  # 小数点计数法


# bytes() 把字符串转换成二进制类型
s='你好武大郎'
bs=s.encode('utf-8')  # 编码
print(bs)


s='吴恒你好你这个人是这样的呀'
bs=s.encode('utf-8')
print(bs)

s='北京市通州区潞城镇武窑村村民委员会 , 北京市通州区潞城镇武窑村村民委员会 ,北京农商银行通州支行甘棠分理处  ,  54110112A02936040N , 北京市通州区潞城镇武窑村北京市通州区潞城镇武窑村村民委员会 , 北京市通州区潞城镇武窑村村民委员会, 北京农商银行通州支行甘棠分理处,   54110112A02936040N,  北京市通州区潞城镇武窑村008af57e3816d6b9  ,   2018乡镇GL0024 , 	2018-2020年度通州区潞城镇建设项目工程监理服务机构'
bs=s.encode('utf-8')
print(bs)
si=bs.decode('utf-8')  # 解码 de
print(si)
# 将字节转换成字符串
bs1=str(bs, encoding='utf-8')
print(bs1)


# repr() 返回一个对象的官方表示形式
print(repr('大家好,\n,\t我叫周杰伦'))
print('大家好我叫周杰伦')
name='axtxsoirpflpbbce QQ邮箱'
print('我叫%r' % name)

# 添加序号和元素
list=['吴恒', 'wusir', 'taibai']
for i, k in enumerate(list):
    print('这是序号', i)
    print('这是元素', k)

# 列表编辑序号
list=['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
for i, k in enumerate(list):
    print('这是序号', i)
    print('这是序号', k)


# any() 可迭代对象中有一个是True,就是True
list=[1, 2, 3, 4, True, 0, False]
list_1=[1, 2, 3, 4, True]
list_2=[2, 55, 9, 0, None, 90, '吴恒', 'wuheng']
print(any(list))
print(any(list_1))
print(any(list_2))


# zip() 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元祖,
# 然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回
list_1=[1, 2, 3]
list_2=['a', 'b', 'c', 'd']
list_3=(12, 34, 45, 35, 26)
for i in zip(list_1, list_2, list_3):
    print(i)

# 一一对应关系
list_1=[4, 5, 6, 9, 12, ]
list_2=['a', 'b', 'c', 'd', 'e', 'f']
list_3=(38, 78, "wuheng", 89, 70)
for i in zip(list_1, list_2, list_3):
    print(i)


# 匿名函数,为了解决一些简单的需求而设计的一句话函数
def func(n):
    return n**n
print(func(6))

# 排序和倒序
list=['吴恒', '马日东', '白毅', '时建', '刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
list_1=sorted(list)
print(list_1)
list_2=sorted(list, reverse=False)
print(list_2)
list_3=sorted(list, reverse=True)
print(list_3)


# 字典使用sorted排序
dic={"name": '刘随强', 'poluation': 6480},
{"name": '王丽', 'poluation': 7555},
{"name": '陈杨', 'poluation': 5400},
{"name": '张大志', 'poluation': 4320}
print(sorted(dic))  # 打印第一个
# 字典能够提出键值
dic={"name": '刘随强', 'poluation': 6480}
print(sorted(dic))

# 定义一个列表,然后根据元素的长度排序
list=['吴恒', '马日东', '白毅', '时建', '刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
def func(s):
    return len(s)
# func()
print(sorted(list, key=func))

# 和lambda组合使用
list=['吴恒', '马日东', '白毅', '时建', '刘万鹏', '杨斌', '宋志明', '刘随强', '王丽', '陈杨', '张大志']
print(sorted(list, key=lambda s: len(s)))


# 按照年龄对学生信息进行排序
list=[{'id': 1, 'name': '吴恒', 'age': 18},
        {'id': 2, 'name': 'wusir', 'age': 17},
        {'id': 3, 'name': 'taibai', 'age': 16}]
print(sorted(list, key=lambda x: x['age']))
# 按照收入对学生信息进行排序
list=[{'name': '王涛', 'money': 601562},
{'name': '王杰', 'money':	2145061},
{'name': '王宏伟', 'money': 770532},
{'name': '唐哲', 'money':	2227835},
{'name': '市场部', 'money': 586079}]
print(sorted(list, key=lambda y: y['money']))


# 按照名字对学生信息进行排序
list=[{'name': '王涛', 'money': 601562},
{'name': '王杰', 'money':	2145061},
{'name': '王宏伟', 'money': 770532},
{'name': '唐哲', 'money':	2227835},
{'name': '市场部', 'money': 586079}]
print(sorted(list, key=lambda y: y['name']))



# map映射函数n**n
lst=[1, 2, 4, 5, 6, 7]
def fun(s):
    return s**s
mp=map(fun, lst)
print(mp)
print(list(mp))

# 公式计算完成后在排序
lst=[1, 2, 4, 5, 6, 7]
print=(list(map(lambda s: s*s)))
lst=[1, 2, 4, 5, 6, 7]
print(list(map(lambda s: s*s, lst)))

lst1=[1, 2, 3, 4, 5]
lst2=[2, 4, 6, 8, 10]
print(list(map(lambda x, y: x+y, lst1, lst2)))

# 人员名字两辆先加
lst1=['吴恒', '马日东', '白毅', '时建',
'刘万鹏', '杨斌', '宋志明']
lst2=['王丽', '陈杨', '张大志']
print(list(map(lambda x, y: x+y, lst1, lst2)))

# lst1=[1, 2, 3, 4, 5]
# lst2=[2, 4, 6, 8, 10]
# def func(x, y):
#     return x+y
# # ret = reduce(func,lst1,lst2)
# print(list(reduce(func,lst1,lst2)))


# 返回函数地址
def func():
    print('呵呵')
print(func)

def func():
    print('呵呵')
    print(func)
a=func
a()

# 函数名可以当做容器类的元素
def func1():
    print('呵呵')


def func2():
    print('呵呵')


def func3():
    print('呵呵')


def func4():
    print('呵呵')


lst=[func1, func2, func3, func4]
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


def func():
    print('开裆裤')
def func2(fn):
    print('我是func2王丽')
    fn()
    print('我是func2王丽')
func2(func)



def func_1():
    print('这是函数1')
    def func_2():
        print('这是函数2')
    print('这是函数1')
    return func_2()
fn=func_1()
fn()


def func1():
    name='吴恒'
    def func2():
        print(name)
    func2()
func1()



# 我们可以使用__closure__ 来检测函数是否是闭包. 使用函数名.__closure__返回cell就是
# 闭包. 返回None就不是闭包
def func1():
    name='吴恒'
    def func2():
        print(name)
    func2()
    print(func2.__closure__)
func1()



def outer():
    name='吴恒'
    def inner():
        print(name)
    return inner
fn=outer()
fn()


def outer():
    name='吴恒'
    def innter():
        print(name)
    return innter
fn=outer()  # 访问外部函数, 获取到内部函数的函数地址
fn()


def outer():
    name='吴恒'
    def innter():
        print(name)
    return innter
fn=outer()  # 访问外部函数, 获取到内部函数的函数地址
fn()


def outer():
    name='吴恒'
    def innter():
        print(name)
    return innter
fn=outer()  # 访问外部函数, 获取到内部函数的函数地址
fn()
