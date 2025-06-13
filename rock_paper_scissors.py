import random

class Entry:
	def beats(self, entry):
		return 0
class Rock(Entry):
	def beats(self, entry):
		if isinstance(entry, Rock):
			return 0
		elif isinstance(entry, Scissors) or isinstance(entry, Lizard):
			return 1
		else:
			return -1
	def __str__(self):
		return 'r'

class Paper(Entry):
	def beats(self, entry):
		if isinstance(entry, Paper):
			return 0
		elif isinstance(entry, Rock) or isinstance(entry, Spock):
			return 1
		else:
			return -1
	def __str__(self):
		return 'p'

class Scissors(Entry):
	def beats(self, entry):
		if isinstance(entry, Scissors):
			return 0
		elif isinstance(entry, Paper) or isinstance(entry, Lizard):
			return 1
		else:
			return -1
	def __str__(self):
		return 's'

class Lizard(Entry):
	def beats(self, entry):
		if isinstance(entry, Lizard):
			return 0
		elif isinstance(entry, Spock) or isinstance(entry, Paper):
			return 1
		else:
			return -1
	def __str__(self):
		return 'l'

class Spock(Entry):
	def beats(self, entry):
		if isinstance(entry, Spock):
			return 0
		elif isinstance(entry, Scissors) or isinstance(entry, Rock):
			return 1
		else:
			return -1
	def __str__(self):
		return 'v'

options = [Rock, Paper, Scissors, Lizard, Spock]

options_shorts = {str(cls()): cls for cls in options}

def print_main_menu():
	print('--- Rock Paper Scissors Lizard Spock Game ---')

def rounds_question():
	tries  = 0
	while tries == 0:
		lines_string = input('How many rounds would you like to play? ')
		if lines_string.isdigit():
			tries = int(lines_string)
		else:
			print('\nEnter a valid number of tries!\n')
	return tries
def get_proposed_entry():
	proposed_entry = ''
	while True:
		proposed_entry = input('Rock, Paper, Scissors, Lizard, or Spock [' + '/'.join([x for x in options_shorts.keys()]) + ']? ')
		if proposed_entry not in options_shorts.keys():
			print('Invalid choice. Please try again\n')
		else:
			break
	return options_shorts[proposed_entry]()

def get_computer_entry():
	return options_shorts[random.choice(list(options_shorts.keys()))]()

win_count = {
	'you' : 0,
	'computer' : 0
}
print_main_menu()
rounds = rounds_question()
for _ in range(rounds):
	round_entry = get_proposed_entry()
	computer_entry = get_computer_entry()
	print(f"You: {round_entry} | Computer: {computer_entry}")
	wins = round_entry.beats(computer_entry)
	if wins == 0:
		print('This round is a tie')
	elif wins == 1:
		print('You won this round!')
		win_count['you'] += 1
	else:
		print('You lose this round!')
		win_count['computer'] += 1
	print()
win_count_you = win_count['you']
win_count_computer = win_count['computer']
print(f'[Game summary] Your points {win_count_you} | Computer points: {win_count_computer}')
if win_count_computer == win_count_you:
	print('It was a tie!')
elif win_count_computer > win_count_you:
	print('Computer won!')
else:
	print('You won!')


