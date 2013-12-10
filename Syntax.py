import sys

# encoding: utf-8

def sayHi():
	''' This is the docstring to show you that
		THE FIRST METHOD IN PYTHON.'''
	print("Hi")

def listDemo():
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



#var x  =SayHi().__doc__
#print(SayHi.__doc__)
#print(sys.path)
#print(u'一切皆对象'.decode('utf-8', 'ignore'))
#print(type(7))


# + 
#append 
#extend 
#insert

