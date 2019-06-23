from collections import Counter

#
fruits = ['apple', 'organge', 'apple']
fruitsdict = Counter(fruits)
print(fruitsdict)

#
myFruits1 = fruitsdict.most_common()
print(myFruits1)
myFruits1 = fruitsdict.most_common(0)
print(myFruits1)
myFruits1 = fruitsdict.most_common(1)
print(myFruits1)
myFruits1 = fruitsdict.most_common(2)
print(myFruits1)

#
fruits1 = ['apple', 'orange', 'apple']
fruitsdictA =Counter(fruits1)
fruits2 = ['grape','orange', 'orange', 'grape']
fruitsdictB =Counter(fruits2)

fruitsdictAdd = fruitsdictA + fruitsdictB
print(fruitsdictAdd)
fruitsdictSub = fruitsdictA - fruitsdictB
print(fruitsdictSub)

fruitsdictInter = fruitsdictA & fruitsdictB
print(fruitsdictInter)
fruitsdictUnion = fruitsdictA | fruitsdictB
print(fruitsdictUnion)

