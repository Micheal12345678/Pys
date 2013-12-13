import re

#依然是正则表达式
#单复数匹配的改变的问题
def plural(noun):
	'''Regular express'''

	#[abc] 匹配其中之一，用o替换了
	print(re.sub('[abc]', 'o', 'caps'))

	#'[sxz]$' 在字符串结尾匹配有s x z中任何一个元素
	if re.search('[sxz]$', noun):
		#$的意思是如果匹配到了s x z直接在字符串末尾加上es
		return re.sub('$', 'es', noun)
	#^除了[]的字母以外...后面必须紧跟着h
	elif re.search('[^aeioudgkprt]h$', noun):
		return re.sub('$', 'es', noun)
	elif re.search('[^aeiou]y$', noun):
		return re.sub('y$', 'ies', noun)
	else:
		return noun + 's'


#将正则表达式分解成不同方法
#这样做代码复用率极高
def plural2(noun):
	for matches_rule, apply_rule in rules:
		if matches_rule(noun):
			return apply_rule(noun)



def match_sxz(noun):
	return re.search('[sxz]$', noun)
def apply_sxz(noun):
	return re.sub('$', 'es', noun)
def match_h(noun):
	return re.search('[^aeioudgkprt]h$', noun)
def apply_h(noun):
	return re.sub('$', 'es', noun)
def match_y(noun): 
	return re.search('[^aeiou]y$', noun)
def apply_y(noun):
	return re.sub('y$', 'ies', noun)
def match_default(noun):
	return True
def apply_default(noun):
	return noun + 's'

#函数列表
rules = ((match_sxz, apply_sxz), 
		 (match_h, apply_h),
		 (match_y, apply_y),
		 (match_default, apply_default))

#匹配模式列表
def build_match_and_apply_functions(pattern, search, replace):
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (matches_rule, apply_rule)

