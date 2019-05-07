# 函数并非总是直接显示输出，可以处理数据，并返回一个或一组值。 函数返回的值被称为返回值 。
def get_formatted_name(first_name,last_name):
	'''返回簡要的名字'''
	full_name = first_name + " " + last_name
	return full_name.title()

def get_place_name(name,place):
	'''返回簡要的名字'''
	full_place = name + " love " + place
	return full_place.title()

musician = get_formatted_name('vincent','wang')
love = get_place_name('esther','tw')

print(musician)
print(love)
