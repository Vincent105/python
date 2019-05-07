travel_place = ['taiwan','toyko','korean','china','india']
print(travel_place)							#呈現原始排列
print(sorted(travel_place))					#使用sorted()暫時排序
print(travel_place)							#核實排序未受到改變
print(sorted(travel_place,reverse=True))	#使用reverse反相暫時排序
travel_place.reverse()						#使用reverse()反轉
print(travel_place)
travel_place.reverse()						#使用reverse()再反轉
print(travel_place)
travel_place.sort()							#使用sort永久排序
print(travel_place)
travel_place.sort(reverse=True)				#使用sort永久排序
print(travel_place)
print(len(travel_place))
