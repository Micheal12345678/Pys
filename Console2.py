#内容:类和迭代器

import FibonacciClass  #导入一个类
import Files
import sys


#实例化一个类
fib = FibonacciClass.Fib(100)
print(fib.__class__)
print(fib.__doc__)
print(fib.max)

# for n in fib:
# 	print(n)

print('关于OOP的概念，运用的还是太少了')

print('STOP:高级迭代器 单元测试 Page 234 - 300')

print('START:文件 对象序列化 HTTPWEB服务 类库打包 Page 234 - 300')

print()
Files.fileDemo()