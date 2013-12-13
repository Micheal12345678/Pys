import Collection
import OS
import String
import Plural

#encoding: utf-8

# Collection.listDemo()
# print();
# Collection.tupleDemo()
# print()
# Collection.setDemo()
# print()
# Collection.setOperationDemo()
# print()
# Collection.dictDemo()
# print()
# Collection.dictListDemo()

# OS.getCurrentDir()
# OS.changeWorkshop()
# OS.pathModel()
# print()
# OS.globModel()
# print()
# OS.metaInfo()
#print(OS.humansize_size(30770,False))
#print(OS.humansize_size(5242930,False))


# print('List Resolved')
# Collection.listResolved()
# Collection.dictResolved()
# Collection.setResolved()


# String.formatDemo()
# print()
# String.stringOperation()
# print()
# String.stringSlicing()
# print()
# String.byteDemo()
# print()
# String.reDemo()
# print()


#单数转复数，利用正则表达式
#print(Plural.plural('crash'))
#Plural.plural('sex')

#print(Plural.plural2('crash'))

#匹配模式 进行正则表达式的运算
patterns = \
(
	('[sxz]$', '$', 'es'),
	('[^aeioudgkprt]h$', '$', 'es'),
	('(qu|[^aeiou])y$', 'y$', 'ies'),
	('$', '$', 's')
)
rules = [Plural.build_match_and_apply_functions(pattern, search, replace)
		for (pattern, search, replace) in patterns]
#print(rules)

#文件匹配模式
rules = []
fileText =open(r'E:\SkyDrive\Pys\plural-rules.txt')
for line in fileText:
	print(line)
	(pattern,search,replace) = line.split(None,3)
	#print(pattern,search,replace)
	rules.append(Plural.build_match_and_apply_functions(pattern, search, replace))
print(rules)



#斐波那契序列运用到了yield形成一个生成器，可以在for循环中使用
#for循环可以自动调用next()进行迭代
# def fib(max):
# 	a, b = 0, 1 
# 	while a < max:
# 		yield a 
# 		a, b = b, a + b

# for n in fib(1000):
# 	print()
# 	print(n,end="")