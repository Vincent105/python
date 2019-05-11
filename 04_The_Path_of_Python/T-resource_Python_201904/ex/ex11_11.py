# ex11_11.py
def make_pizza(pizza_size, *toppings):
    # 列出製作pizza的配料
    print("這個 ", pizza_size, " 吋Pizza所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_pizza(5, '海鮮')
make_pizza(7, '蔬菜', '辛香料', '香菇', '起司','海鮮')

