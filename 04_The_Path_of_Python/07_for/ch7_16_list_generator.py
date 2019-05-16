colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square", "Line"]
result = [[color, shape] for color in colors for shape in shapes]

#List unpacking
for color, shape in result:
    print(color, shape)

oddlist = []
for num in range(1, 10):
    if num % 2 == 1:
        oddlist.append(num)

oddlist = [num for num in range(1, 10) if num % 2 == 1]

for x in range(32, 128):
    print(chr(x),end='')

for x in range(0x6d2a, 0x6e2a):
    print(chr(x),end='')

