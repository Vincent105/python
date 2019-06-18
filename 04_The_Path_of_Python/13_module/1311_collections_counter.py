from collections import Counter

fruits = ['apple','organge','apple']
fruitsdict = Counter(fruits)
print(fruitsdict)

myFruits1 = fruitsdict.most_common()
print(myFruits1)
myFruits1 = fruitsdict.most_common(0)
print(myFruits1)
myFruits1 = fruitsdict.most_common(1)
print(myFruits1)
myFruits1 = fruitsdict.most_common(2)
print(myFruits1)