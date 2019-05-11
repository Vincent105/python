# ex12_1.py
class Myschool():
    title = "明志科大"
    def departments():
        return ['機械','電機','化工']

A = Myschool
print(A.title)
for major in A.departments():
    print(major)
