james = ['vicnent', 23, 19, 22, 31, 18]
love =  ['esther', 20, 11, 29, 24, 25]
score = james[4] + love[4]
lkgmae = james[0].title() + ' and ' + love[0].title() + ' 第四場得分為= '
print(lkgmae,score)

love.insert(1,'test')
print(love)

a, *b , c = [1, 2, 3, 4, 5]
print(a,b,c)

string = 'abc'
print(dir(string))
help(string.title)
help(james.insert)
num = 5
print(dir(num))