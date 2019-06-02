def make_icecream(icecream_type, *toppings):
    print(icecream_type + ":配料如下" + "\n")
    for topping in toppings:
        print("---------" + topping)
    print(type(toppings))
    print(toppings)


# make_icecream()
make_icecream('草莓冰', '草莓')
make_icecream('綜合冰', '草莓', '花生')


def build_dict(name, age, **players):
    info = {}
    info['name'] = name
    info['age'] = age
    for key, value in players.items():
        info[key] = value
    return info


player_info = build_dict('vincent', '35', city='taipei', state='taiwan')
print(player_info)
