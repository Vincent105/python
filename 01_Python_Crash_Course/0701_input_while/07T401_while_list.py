# 在列表中移動元素
sandwich_orders = ['apple','banana','lemon']
finished_sandwiches = []

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	print("Add: " + sandwich_order.title())

	finished_sandwiches.append(sandwich_order)

print("\nThe following users have been confirmed:")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche.title())	



