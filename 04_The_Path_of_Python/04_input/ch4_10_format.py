print('%3s%4d%4d%6.1f'%('v',22,33,18.0))

score = 90.65
name = 'vincent'
count = 1 

print('{0}你的第{1}次物理考試成績為{2}'.format(name,count,score))
print('{a}你的第{b}次物理考試成績為{c}'.format(a = 'john',b = 2,c = 100))

print('{0:50s}你的第{1:+20d}次物理考試成績為{2:10.1f}'.format(name,count,score))
print('{0:50s}你的第{1:+20d}次物理考試成績為{2:*<10.1f}'.format(name,count,score))
print('{0:50s}你的第{1:+20d}次物理考試成績為{2:=^10.1f}'.format(name,count,score))
print('{0:50s}你的第{1:+20d}次物理考試成績為{2:+>10.1f}'.format(name,count,score))
print('{0:50s}你的第{1:+20d}次物理考試成績為{2:/>10.1f}'.format(name,count,score))

sp = ' '* 40
print('%s    1231 Del Rd' % sp)
print('{0}    1231 Del Rd'.format(sp))
print('{0}    USA\n\n\n'.format(sp))
print('Dear vincent.')
