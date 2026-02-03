import json
from datetime import datetime
from pathlib import Path


class TaskManager:
	def __init__(self, path_file):
		self.tasks = []
		self.path_file = path_file
		self.load_tasks()

	def load_tasks(self):
		if not Path(self.path_file).exists():
			with open(self.path_file, 'w') as f:
				json.dump([], f)

		with open(self.path_file, 'r+') as f:
			file_data = json.load(f)

		self.tasks = file_data

	def save_tasks(self):
		with open(self.path_file, 'w') as f:
			json.dump(self.tasks, f)

	def add_task(self, task):
		self.tasks.append(
			{
				'id': self.tasks[-1]['id'] + 1 if self.tasks else 1,
				'description': task,
				'status': 'todo',
				'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
				'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			}
		)

		self.save_tasks()

		print(f'Task added successfully (ID: {self.tasks[-1]["id"]})')

		return self.tasks[-1]

	def update_task(self, id, task):
		index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

		if index is not None:
			self.tasks[index]['description'] = task
			self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		else:
			raise Exception('Invalid task ID')

		self.save_tasks()

		return self.tasks[index]

	def delete_task(self, id):
		self.tasks = list(filter(lambda task: task['id'] != id, self.tasks))

		self.save_tasks()

		return self.tasks

	def get_tasks(self):
		return self.tasks

	def get_task(self, id):
		return next((task for task in self.tasks if task['id'] == id), None)

	def get_tasks_by_status(self, status):
		return list(filter(lambda task: task['status'] == status, self.tasks))

	def mark_task(self, id, status):
		if status not in ['todo', 'in-progress', 'done']:
			raise Exception('Invalid status')

		index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

		if index is not None:
			self.tasks[index]['status'] = status
			self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		else:
			raise Exception('Invalid task ID')

		self.save_tasks()

		return self.tasks[index]
