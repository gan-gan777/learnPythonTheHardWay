# -*- coding:UTF-8 -*-

cars = 100										 		# 汽车的数量
space_in_a_car = 4										# 车辆载客数
drivers = 30											# 司机的数量
passengers = 90											# 乘客的数量
cars_not_driven = cars - drivers						# 无司机的车辆数量
cars_driven = drivers									# 可以开的汽车数量（等于司机的数量）
carpool_capacity = cars_driven * space_in_a_car			# 拼车能力=可开的车辆*车辆载客数
average_passengers_per_car = passengers / cars_driven	# 每辆车的平均乘客数量=乘客数量/可开的车辆

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

