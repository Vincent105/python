# addToInventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + ': ' + str(v))
        item_total += v
    print("Total number of items: " + str(item_total) + '\n')


def addToInventory(inventory, addedItems):
    print("\nInventory updated:")
    c1 = {}
    for something in addedItems:
        c1.setdefault(something, 0)
        c1[something] += 1
    for v in inventory.keys():
        if v not in c1.keys():
            c1.setdefault(v, 0)
            c1[v] += inventory[v]
    for k in c1.keys():
        if k in inventory:
            c1[k] = c1[k] + inventory[k]
    return c1


def displayInventory(inv):
    for k, v in inv.items():
        print(k + ' : ' + str(v))
    print('\n')


displayInventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('Inventory:')
displayInventory(inv)

print('BOSS drop:')
print(dragonLoot)

inv = addToInventory(inv, dragonLoot)

print('\nInventory')
displayInventory(inv)
