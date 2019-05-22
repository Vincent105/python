field = ['Name', 'Age', 'Hometown']
info = ['Vincnet', '35', 'Taiwan']

zipdata = zip(field, info)
print(type(zipdata))

player = list(zipdata)
print(player)

f, i = zip(*player)
print(f)
print(i)


x = (n for n in range(3))
print(type(x))