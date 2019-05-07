def describe_pet(animal_type, pet_name='test'):	#給予預設值，若無指定時，將以預設值帶值。無預設值須先列出。
	"""顯示寵物的資訊"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name)

describe_pet('hamster','vincent')
describe_pet('dog','esther')

#傳遞關鍵字給參數
describe_pet(pet_name='esther',animal_type='hamster')

#套用關鍵字
describe_pet('dog')
describe_pet('cat','tttt')

#同意調用
describe_pet('cat')
describe_pet(animal_type='cat')

describe_pet('cat','test')
describe_pet(animal_type='cat',pet_name='test')
describe_pet(pet_name='test',animal_type='cat')

# describe_pet() 