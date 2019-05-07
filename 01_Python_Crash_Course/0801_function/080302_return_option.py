#
def get_formatted_name(first_name,last_name,middle_name=''):
	'''返回完整名字，但可以不輸入中間名'''
	full_name = first_name + " " + middle_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('vincent','wang')
musician_2 = get_formatted_name('vincent','wang','esther')
print(musician)
print(musician_2)
