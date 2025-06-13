import random

def generate_tickets(ticket_count, max_number):
	array = []
	count = 0
	while count < ticket_count:
		entry = int(random.random() * float(max_number))
		if entry not in array:
			array.append(entry)
			count += 1
	winner = random.choice(array)
	return tuple([array, winner])

print(generate_tickets(10,10))

class Bunny:
	__count = 0
	def __init__(self):
		self.__speed = 0

	def print_speed(self):
		print(self.__speed)

bunny = Bunny()
bunny.print_speed()
print(hasattr(Bunny, "_Bunny__count"))
