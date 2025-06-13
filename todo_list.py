import uuid

default_file_name = 'todo_list.txt'

class InvalidTodo(Exception):
	pass

class TodoItemAppendError(Exception):
	pass

class TodoItemReadError(Exception):
	pass

class InvalidMenuSelection(Exception):
	pass

class TodoItem:
	file_name = default_file_name
	def __init__(self, task=None, deadline=None):
		self.id = str(uuid.uuid4())
		self.task = task
		self.deadline = deadline

	def load_line(self, line):
		entries = line.split('|')
		if len(entries) != 3:
			raise InvalidTodo
		self.id = entries[0].strip()
		self.task = entries[1].strip()
		self.deadline = entries[2].strip()

	def write(self):
		todo_entry = str(self) + '\n'
		try:
			with open(TodoItem.file_name, 'a') as file:
				file.write(todo_entry)
		except:
			raise TodoItemAppendError()

	def __str__(self):
		return f'{self.id} | {self.task} | {self.deadline}'

	def __eq__(self, other):
		return isinstance(other, TodoItem) and self.id == other.id

class TodoManager:
	file_name = default_file_name
	def __init__(self):
		self.todo_items = []
		self.load_list_from_file()

	def load_list_from_file(self):
		try:
			with open(TodoManager.file_name, 'a+') as file:
				file.seek(0)
				for line in file:
					todo_item = TodoItem()
					todo_item.load_line(line)
					self.todo_items.append(todo_item)
		except:
			raise TodoItemReadError()

	def add_todo_item(self):
		print('[Add Task]')
		task = input('What is the task? ')
		deadline = input('What is the deadline? ')
		todo_item = TodoItem(task=task, deadline=deadline)
		todo_item.write()
		self.todo_items.append(todo_item)

	def write(self):
		with open(TodoManager.file_name, 'w') as file:
			for todo_item in self.todo_items:
				file.write(str(todo_item)  + '\n')

	def print_tasks(self):
		print('[YOUR TASKS]')
		if len(self.todo_items) == 0:
			print('Empty list')
			return
		for todo_item in self.todo_items:
			print(todo_item)
	def complete_task(self):
		print('[COMPLETE TASK]')
		print()
		self.print_tasks()
		print()
		if len(self.todo_items) == 0:
			print('No tasks to complete')
			return
		todo_id = input('Enter an id to complete: ')
		todo_item = list(filter(lambda x: x.id == todo_id, self.todo_items))
		if len(todo_item) == 1:
			self.todo_items.remove(todo_item[0])
			self.write()
		else:
			print(f'\nThere is no item with id: {todo_id}')

	def print_menu(self):
		print('== TODO LIST ==')
		print('[1] show task')
		print('[2] add task')
		print('[3] complete task')
		print('[4] exit')

	def get_menu_choice(self):
		selection = 0
		while selection == 0:
			try:
				selection = int(input('Your choice: '))
				if selection < 1 or selection > 4:
					selection = 0
					raise InvalidMenuSelection()
			except:
				print('Invalid selection. Please try again')
		return  selection

	def run(self):
		while True:
			self.print_menu()
			selection = self.get_menu_choice()
			print()
			if selection == 4:
				break
			elif selection == 3:
				self.complete_task()
			elif selection == 2:
				self.add_todo_item()
			else:
				self.print_tasks()
			print()
		print('Bye!')

TodoManager().run()
