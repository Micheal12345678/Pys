
import codecs



def fileDemo():

	#open返回的是一个stream对象

	a_file = open('E:\SkyDrive\Pys\story.txt',"r")
	print(a_file.name)
	print(a_file.encoding)
	print(a_file.mode)
	s = a_file.read()
	#print(type(s))
	print(s)

	#print(s.decode('UTF-8'))
	a_file.close()


#http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html