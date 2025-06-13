import math
def halve_string(input_string):
	input_string_len = len(input_string)
	half = math.ceil(input_string_len / 2)
	return tuple([input_string[:half], input_string[half:]])

def halve_strings(string_list):
	return [halve_string(x) for x in string_list]

print(halve_strings(['Mark', 'Lydia']))
