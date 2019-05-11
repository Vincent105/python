# ex4_1.py
apple = 100
student = 23
day = apple // student
print("蘋果可以吃 %d 天" % day)
print("第 %d 天產生蘋果不足供應" % (day+1))
left = apple % student
not_enough = student - left
print("不足 %d 顆" % not_enough)




