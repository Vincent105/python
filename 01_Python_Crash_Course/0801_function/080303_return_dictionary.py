#返回字典包含個人訊息,並支援擴增
def build_name(first_name,last_name,age='',education=''):
	'''返回字典包含個人訊息'''
	person ={'first_name': first_name,'last_name': last_name}
	if age:
		person['age']= age
	if education:
		person['education']= education		
	return person

musician = build_name('vincent','wang','22','high school')
print(musician)
print(musician['first_name'])
print(musician['last_name'])
print(musician['age'])
print(musician['education'])

musician_2 = build_name('esther','huang','18','college')
print(musician_2)
print(musician_2['first_name'])
print(musician_2['last_name'])
print(musician_2['age'])
print(musician_2['education'])	
