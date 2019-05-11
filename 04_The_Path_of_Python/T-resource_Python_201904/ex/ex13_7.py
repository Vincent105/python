# ex13_7.py
import random                               # 導入模組random

lotterys = random.sample(range(1,50), 6)    # 6組號碼
specialNum = random.randint(1,8)            # 特別號

print("第1000期威力彩號碼 ")
print("特別號:%d" % specialNum)             # 列印特別號
for lottery in sorted(lotterys):            # 排序列印威力彩號碼
    print(lottery, end=" ")














