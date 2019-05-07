# 傳遞列表至function
def greet_users(names):
	'''向列表中的每個人問好'''
	for name in names:
		msg = "Hello " + name + "!"
		print(msg)

usernames = ['vincent','esther','john']		
greet_users(usernames)

#在function中修改列表----以下是原始版本
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print(unprinted_designs)	
print(completed_models)

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Print: " + current_design)
	completed_models.append(current_design)

for completed_model in completed_models:
	print("Completed model:" + completed_model)	

print(unprinted_designs)	
print(completed_models)

#在function中修改列表----以下是重構版本
def print_models(unprinted_designs,completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打	每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# 模拟根据设计制作3D打印模型的过程
		print("Print: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	for completed_model in completed_models:
		print("Completed model:" + completed_model)		

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron','test case']
completed_models = []

print("\n禁止修改列表: 原本的列表還是存在")
print_models(unprinted_designs[:],completed_models)		#透過[:]代表取用列表的副本，而不是異動原始列表。除非必要則盡量少使用此方式。
print(unprinted_designs)
show_completed_models(completed_models)

print("\n沒有禁止修改: 原本的列表將被異動")
print_models(unprinted_designs,completed_models)
print(unprinted_designs)
show_completed_models(completed_models)  #走了兩次 才會變成兩倍，測試用，不用在意。