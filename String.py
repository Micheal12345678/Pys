import OS
import sys
import re

def formatDemo():
	username = 'Micheal'
	password = '*******'
	print('{0}\'s password is {1}'.format(username,password))

	#比较复杂的格式化
	si_suffixes = OS.SUFFIXES[1024]
	print(si_suffixes)
	#格式化输出
	print('1024{0[0]}=1{0[1]}'.format(si_suffixes))
	print('1MB = 1000{0.modules[OS].SUFFIXES[1000][0]}'.format(sys))

	#字符串格式化说明
	#1.  {0:.2f}  代表着第一个参数，冒号进一步格式化为，精度未2位
	print('{0:.2f}'.format(235.5426)) #输出为 235.54

def stringOperation():
	s ='''Finished files are the sult
	of years scientific study combined 
	with the exprience of years'''
	print(s.splitlines())
	print(s.lower())
	print(s.lower().count('f'))

	#将一个字符串分解成字典
	query = 'user=pilgrim&database=master&password=PapayaWhip'
	a_list = query.split('&')
	print(a_list)
	#v.split('=',1)  以=为单位，分成两个字符串
	a_list_of_lists = [v.split('=',1) for v in a_list]
	print(a_list_of_lists)
	a_dict = dict(a_list_of_lists)
	print(a_dict)

#字符串的分片
def stringSlicing():
	a_string = 'My alphabet starts where your alphabet ends.'
	print(a_string[3:11])
	print(a_string[3:-3])
	print(a_string[:18])
	print(a_string[18:])

#字符集从\x00到\xff编码了的16进制数
def byteDemo():
	by = b'abcd\x65'
	print(by)
	print(type(by))
	print(len(by))
	by += b'\x66' #by += b'\xff'
	print(by)
	print(by[4])

	a_string = '深入 Python'
	print(len(a_string))  #9个字符
	by = a_string.encode('utf‐8')
	print(len(by))        #13个字节
	print(by)

#正则表达式
# ^ 匹配字符串开始. $ 匹配字符串结尾
def reDemo():
	s = '100 BROAD ROAD'
	#$ 匹配字符串结尾
	print(re.sub('ROAD$','RD.',s))
	#\b 表达是空格符，即作为一个单词
	print(re.sub('\\bROAD$', 'RD.', s))
	#r 是原始字符串
	print(re.sub(r'\bROAD$', 'RD.', s))
	#最后定义为只有独立单词的才能改变
	print(re.sub(r'\bROAD\b', 'RD.', s))

	#罗马数字
	# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
	#匹配3个可选的M,且是要连续的
	#^表示从头开始 $表示结束 ^$合起来表示连续的
	#？表示字符串是可选的
	#| 可选的意思
	#\d 匹配所有0‐9的数字. \D 匹配除了数字外的所有字符
	#\d{3} 必须三位数字 \d{0:3} 0到3位数字
	#x* 匹配0个或更多的x。
	#(a|b|c) 匹配单独的任意一个a或者b或者c。
	pattern = '^M?M?M?(CM|CD|D?C?C?C?)$' #检查百位数
	pattern = '^M{0,3}$'                 #匹配0到3个连续的M
	pattern = '^M?M?M?$'                 #检查千位数
	print(re.search(pattern, 'M'))
	print(re.search(pattern, 'MM'))
	print(re.search(pattern, 'MMM'))
	print(re.search(pattern, 'MMMM'))  #返回NONE
	print(re.search(pattern, ''))

	phonePattern = re.compile(r'^(\d{3})‐(\d{3})‐(\d{4})$')
	result = phonePattern.search('800‐555‐1212').groups()
	print(result)

	#\d+ 一个或者多个数字
	phonePattern = re.compile(r'^(\d{3})‐(\d{3})‐(\d{4})‐(\d+)$')
	#result = phonePattern.search('800‐555‐1212-2122').groups()
	#print(result)

