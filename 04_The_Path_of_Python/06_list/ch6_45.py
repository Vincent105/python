string = "Python"

print('string[0]= ',string[0],
      '\nstring[1]= ' ,string[1],
      '\nstring[2]= ' ,string[2],
      '\nstring[3]= ' ,string[3],
      '\nstring[4]= ' ,string[4],
      '\nstring[5]= ' ,string[5],
)

print('string[0]= ',string[-1],
      '\nstring[1]= ' ,string[-2],
      '\nstring[2]= ' ,string[-3],
      '\nstring[3]= ' ,string[-4],
      '\nstring[4]= ' ,string[-5],
      '\nstring[5]= ' ,string[-6],
)

s1, s2, s3, s4, s5, s6 = string
print(s1, s2, s3, s4, s5, s6)

x = list(string)
print(x)

x[2:] = 'test'
print(x)

#split
str_1 = 'slicon test 2mins'
str_2 = 'd"\wewe\weqe'
y = str_1.split()
z = str_2.split('\\')
print(y)
print(z)

#join
path = ['D:','ch6','ch6_49.py']
connect = '\\'
print(connect.join(path))      
connect_2 = '*'
print(connect_2.join(path))      

#startswith(),endswith,replace(ch1,ch2)
msg = '''CIA Mark told CIA Linda that the secret USB Had given to CIA Peter'''
print(msg.startswith('CIA'))
print(msg.endswith('CIA'))
print(msg.count('CIA'))
msg = msg.replace('Linda','Vincent')
print(msg)


