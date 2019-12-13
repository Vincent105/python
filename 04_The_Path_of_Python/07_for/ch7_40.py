import os
import csv

buyers = [
    ['James', 1030],
    ['Curry', 893],
    ['Durant', 2050],
    ['Jordan', 990],
]
goldBuyers = []
vipBuyers = []
while buyers:
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:
        vipBuyers.append(index_buyer)
    else:
        goldBuyers.append(index_buyer)
print('vipBuyers:', vipBuyers)
print('goldBuyers:', goldBuyers)


file_path = './data'
file_name = 'example.csv'
rows_shifts1, rows_shifts2, rows_shifts3, rows_shifts4, rows_shifts5, = [], [], [], [], []
rows_shifts_diff = {}

with open(os.path.join(file_path, file_name), encoding='UTF-8-sig', newline='') as file_csv:
    rows = csv.reader(file_csv)
    for row in rows:
        rows_shifts1.append(row[5])
        rows_shifts2.append(row[6])
        rows_shifts3.append(row[7])
        rows_shifts4.append(row[8])
        rows_shifts5.append(row[9])
rows_shifts_diff[rows_shifts1[0]] = rows_shifts1[1:]
rows_shifts_diff[rows_shifts2[0]] = rows_shifts2[1:]
rows_shifts_diff[rows_shifts3[0]] = rows_shifts3[1:]
rows_shifts_diff[rows_shifts4[0]] = rows_shifts4[1:]
rows_shifts_diff[rows_shifts5[0]] = rows_shifts5[1:]
print(rows_shifts_diff)
