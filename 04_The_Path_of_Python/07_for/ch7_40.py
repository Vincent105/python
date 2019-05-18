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
print('vipBuyers:',vipBuyers)        
print('goldBuyers:',goldBuyers)        