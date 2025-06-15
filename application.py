import math
def halve_string(input_string):
	input_string_len = len(input_string)
	half = math.ceil(input_string_len / 2)
	return tuple([input_string[:half], input_string[half:]])

def halve_strings(string_list):
	return [halve_string(x) for x in string_list]

print(halve_strings(['Mark', 'Lydia']))


class A:
	x = 'x'

	def alarm(self):
		print('a' + self.x)


class B(A):
	def alarm(self):
		super().alarm()


class C(B):
	x = 'y'


C().alarm()

file = open('data.txt', 'w+')
print('Name of the file: ', file.name)

s = 'Peter Wellert\nHello everybody'
file.write(s)
file.seek(0)
for line in file:
	print(line)

file.close()
L = [i for i in range(-1, -2)]
print(len(L))


class Class:
	var = 1

	def __init__(self, value):
		self.prop = value


object_1 = Class(2)
print(object_1.__dict__)
x = [0, 1, 2]
x.insert(0, 1)
del x[1]
print(sum(x))
