#make_food
def make_icecream(*toppings):
    # 列出配料
    print("配料如下:")
    for topping in toppings:
        print('---', topping)


def make_drink(size, drink):
    print("所點飲料如下:")
    print('---',size.title())
    print('---',drink.title())