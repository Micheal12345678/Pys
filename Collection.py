import sys
import os
import glob

# encoding: utf-8

def sayHi():
	''' This is the docstring to show you that
		THE FIRST METHOD IN PYTHON.'''
	print("Hi")

def listDemo():
	#Method.__doc__
	'''The method is for list'''

	#初始化一个List
	#List可以有不同类型的元素组成
	a_list = ['a']
	#向List中添加元素有四种方法 + extend insert append
	a_list += [2.0,3.6] # 加号直接往List后面添加元素
	a_list.insert(1,'Insert') #Insert方法可以在插入List任何位置
	a_list.append(['append1','append2']) #append方法是向List后位追加list作为一个元素
	a_list.extend(['extend1','extend2',1.0,1.0]) #extend方法是向List后位追加

	print(a_list)

	#在列表中检索值
	print('How many 1.0 in list? Result:%d'%a_list.count(1.0) )
	print('What is 1.0 index? Result:%d'%a_list.index(1.0) )
	print('Is extend1 in the list? Result:%s'%('extend1' in a_list))

	#删除列表中的元素
	#del a_list[0]
	#a_list.remove(1.0)
	#a_list.pop() # 如果不带参数就删除最后一个元素
	#a_list.pop(3) # 删除第四个元素
	print(a_list)

	#列表切片
	#print(a_list[1:3])
	#print(a_list[:3])

#元组是一系列不可变的集合
#元组的速度比列表要快，而且更加安全
#元组可用作字典键，因为是不变的。（不太理解）
#元组可以转化成列表，列表也可以转化成元组，分别是tuple()冻结或者list()融化
def tupleDemo():
	'''The method is for tuple'''
	#初始化一个元组，注意用的是括号，而不是中括号
	a_tuple = ('a', 'b', 'mpilgrim', 'z', 'example')
	print(a_tuple)

	#一次给变量赋多值的属性
	values = ('a',2.0,True)
	(x,y,z) = values  #这样一次性就给三个变量赋值了
	print(z)
	#利用内建函数range()赋值
	(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY) = range(7)
	print(SATURDAY)

#集合以函数set构造，是无序的值的集合。
#集合之间可以Join,求差等等...
#集合是以{}包裹起来的
def setDemo():
	'''The method is for collection'''
	#先定义一个列表，然后转化成集合
	a_list = ['a', 'b', 'mpilgrim', True, False, 42]
	a_set = set(a_list)
	print(type(a_set))
	print(len(a_set))
	print(a_set)

	#添加：add()
	a_set = {1,2}
	a_set.add(3)
	a_set.add(1) #如果集合中新增已有的元素，将不发生任何变化
	print(a_set)
	#添加：update() 仅仅接收一个集合作为参数
	a_set.update({2,4,6}) #输出结果{1, 2, 3, 4, 6}
	a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})#{1, 2, 3, 4, 5, 6, 8, 9, 13}
	a_set.update([10, 20, 30]) #{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}
	print(a_set) 

	#从集合中删除某个元素
	#可以用discard和remove方法。
	#discard可以删除已经不存在的数据，且不会报错
	#remove删除已经存在的数据会报错
	a_set.discard(10)
	#a_set.remove(10)
	print(a_set)
	#pop()方法也可以删除集合中的一个元素想，并且返回该元素
	#但是因为set是无序的，所以不知道删除的是哪个
	#clear()方法是将集合全部清空
	print(a_set.pop())
	a_set.clear()
	print(a_set);

#集合的操作
#交集，并集，补集，子集，超级的概念
def setOperationDemo():
	a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}

	#元素是否存在于集合中
	print(30 in a_set)  #True
	print(31 in a_set)  #False

	#两个集合相互合并:并集
	b_set ={1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
	print(a_set.union(b_set)) #合并完成后，将重复的元素去除

	#同时出现于两个集合的元素：交集
	print(a_set.intersection(b_set)) #{9, 2, 12, 5, 21}

	#装着出现于A，但未出现于B的集合：补给
	print(a_set.difference(b_set)) #{195, 4, 76, 51, 30, 127}

	#装着所有 只在其中一个 集合中出现的元素。
	print(a_set.symmetric_difference(b_set))

	a_set = {1, 2, 3}
	b_set = {1, 2, 3, 4}
	#判断子集
	print(a_set.issubset(b_set))
	#判断超集
	print(b_set.issuperset(a_set))
	a_set.add(5)
	#判断子集
	print(a_set.issubset(b_set))
	#判断超集
	print(b_set.issuperset(a_set))

#字典类型，主要是键值对
#依然用{}
def dictDemo():
	a_dict = {'server': 'db.ansoft.org', 'database': 'mongodb'}
	print(a_dict['server'])

	#字典类型的新增和修改一样，都是通过键值对
	#字典类型中不允许重复的键
	#字段区分大小写
	a_dict['database'] = 'mysql'
	a_dict['user'] = 'Micheal'
	print(a_dict)

#字典与列表类型混用
def dictListDemo():
	SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
				1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
	print(SUFFIXES)
	print(SUFFIXES[1000][3])


#列表解析
#列表解析实现了通过对列表中每一个元素
#应用一个函数的方法来将一个列表映射到另一个列表.
#列表解析可以与glob os等模块合并使用
#这里的列表解析有点儿像.NET LINQ
def listResolved():
	a_list = [1, 9, 8, 4]
	print(a_list)
	#列表解析的应用
	print([e * 2 for e in a_list])
	print(a_list) #但是不影响原来的列表
	#文件大于 1 KB 的文件
	files = [f for f in glob.glob('*.py') if os.stat(f).st_size > 1024]
	print(files)

#字典解析和列表解析差不多，只是返回的是字典
def dictResolved():
	a_dict = {'a': 1, 'b': 2, 'c': 3}
	print({value:key for key,value in a_dict.items()})

#集合解析，没有键值对，也没有索引
def setResolved():
	#这种写法非常巧妙
	a_set = set(range(10)) 
	print(a_set)
	print({x ** 2 for x in a_set})
	print({x for x in a_set if x % 2 == 0})
	print({2**x for x in range(10)})