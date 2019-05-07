# 在列表中移動元素
sandwich_orders = ['apple','banana','lemon','apple','apple','lemon']
finished_sandwiches = []

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	print("Add order: " + sandwich_order.title())

	finished_sandwiches.append(sandwich_order)

print("\nWe don't have apple in store.")

# 在列表中移除元素
while 'apple' in finished_sandwiches:
	finished_sandwiches.remove('apple')


print("\nThe following users have been confirmed:")
for finished_sandwiche in finished_sandwiches:

	print(finished_sandwiche.title())	



