import random

def print_main_menu():
	print('-- Password Generator --')
	print('Choose an option:')
	print('1. generate password')
	print('2. exit the program')

def run_query(query):
	result = ''
	while result != 'y' and result != 'n':
		result = input(query + ': ')
	return result == 'y'

def get_password_length():
	size = -1
	while size == -1:
		size_string = input('Provide password length: ')
		if not size_string.isdigit():
			print('Please enter a valid number!\n')
		else:
			size = int(size_string)
	return size

def generate_password():
	query_list = {'Use uppercase letters': [chr(x) for x in range(65, 91)],
				  'Use digits': [str(x) for x in range(0, 10)],
				  'Use special characters': list("!@#$%^&*()-_=+[]{}|;:',.<>?/~`")}
	password = ''
	size = get_password_length()
	lowercase = [chr(x) for x in range(97,123)]
	password_char_options = [lowercase]
	for query,item in query_list.items():
		if run_query(query):
			password_char_options.append(item)
	for _ in range(0, size):
		password_char_option = random.choice(password_char_options)
		char = random.choice(password_char_option)
		password += char
	return password

running = True
while running:
	print_main_menu()
	option = int(input("Your choice: "))
	if option == 2:
		print('Bye!')
		running = False
	elif option == 1:
		generated_password = generate_password()
		print()
		print("Generated password: " + generated_password)
	else:
		print('Please enter a correct value\n')
