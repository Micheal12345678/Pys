#python的类并没有接口
#这是一个迭代器的类
#需要实现三个特殊的方法
class Fib:
	'''Fibonacci Class'''

	#self并非保留的字符串，但是是个很好的习惯
	#这个方法并非构造函数，而是在对象初始化以后第一次调用
	def __init__(self, max):
		#实例变量，这个变量是全局的
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib