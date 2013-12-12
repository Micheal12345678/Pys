import os
import glob
import time

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
			1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def humansize_size(size, a_kilobyte_is_1024_bytes=True):
	'''Convert a file size to human‐readable form.
		Keyword arguments:
		size ‐‐ file size in bytes
		a_kilobyte_is_1024_bytes ‐‐ if True (default), use multiples of 1024
		if False, use multiples of 1000
		Returns: string'''
	if size < 0:
		raise ValueError('number must be non‐negative')
	#这种写法太过牛B了
	multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
	
	for suffix in SUFFIXES[multiple]: #这个循环一次是控制单位的
		size /= multiple              #取余，且除以1024
		print(size)
		if size < multiple:
			return '{0:.2f} {1}'.format(size, suffix)


def getCurrentDir():
	print(os.getcwd())

def changeWorkshop():
	pass
	#os.chdir('E:/SkyDrive/Workshop')

def pathModel():
	#打印当前用户的根目录
	print(os.path.expanduser('~'))
	#当前用户的根目录，并且构造新的目录
	print(os.path.expanduser('~'),'examples', 'humansize.py')
	#拼接路径
	print(os.path.join('/Users/shouan.xu/examples/', 'humansize.py'))

	pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
	#拆分路劲
	print(os.path.split(pathname)) #将路径和文件名拆分
	(dirname, filename) = os.path.split(pathname)
	(shortname, extension) = os.path.splitext(filename)#将文件名和后缀名拆分
	print(dirname)
	print(filename)
	print(shortname)
	print(extension)

	#构造绝对路径
	os.path.realpath('/Users/shouan.xu/examples/Hi.py')

def globModel():
	currentPath = os.getcwd()
	currentFile = os.path.join(os.getcwd(),'OS.py') 
	print(currentFile)
	print(currentPath)

	#开始匹配所有.py的文件
	# * 是通配符
	print(glob.glob('*.py')) #列表类型['Console.py', 'OS.py', 'Syntax.py']

#获取文件的信息
def metaInfo():
	currentFile = os.path.join(os.getcwd(),'OS.py') 
	metadata = os.stat(currentFile)
	print(metadata.st_size)  #返回的是字节数目
	print(metadata.st_mtime)
	print(time.localtime(metadata.st_mtime))