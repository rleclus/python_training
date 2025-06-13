import uuid

class InvalidTodo(Exception):
	pass

class TodoItem:
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

