import json
from datetime import datetime
from pathlib import Path


class TaskManager:
	DATA_FILE = Path(__file__).resolve().parents[2] / 'tasks.json'

	def __init__(self):
		self.tasks = []
		self.load_tasks()

	def load_tasks(self):
		if not Path(self.DATA_FILE).exists():
			with open(self.DATA_FILE, 'w') as f:
				json.dump([], f)

		try:
			with open(self.DATA_FILE, 'r+') as f:
				file_data = json.load(f)

			self.tasks = file_data
		except Exception as error:
			raise Exception('Unknown error while loading tasks') from error

	def save_tasks(self):
		try:
			with open(self.DATA_FILE, 'w') as f:
				json.dump(self.tasks, f)
		except Exception as error:
			raise Exception('Unknown error while saving tasks') from error

	def add_task(self, task):
		try:
			self.tasks.append(
				{
					'id': len(self.tasks) + 1,
					'description': task,
					'status': 'todo',
					'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
					'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
				}
			)

			self.save_tasks()

			print(f'Task added successfully (ID: {self.tasks[-1]["id"]})')

			return self.tasks[-1]
		except Exception as error:
			raise Exception('Unknown error while adding task') from error

	def update_task(self, id, task):
		try:
			index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

			if index is not None:
				self.tasks[index]['description'] = task
				self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

			self.save_tasks()

			return self.tasks[index]
		except Exception as error:
			raise Exception('Unknown error while updating task') from error

	def delete_task(self, id):
		try:
			self.tasks = list(filter(lambda task: task['id'] != id, self.tasks))

			self.save_tasks()

			return self.tasks
		except Exception as error:
			raise Exception('Unknown error while deleting task') from error

	def get_tasks(self):
		return self.tasks

	def get_task(self, id):
		return next((task for task in self.tasks if task['id'] == id), None)

	def get_tasks_by_status(self, status):
		return list(filter(lambda task: task['status'] == status, self.tasks))

	def mark_task(self, id, status):
		if status not in ['todo', 'in-progress', 'done']:
			raise Exception('Invalid status')

		try:
			index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

			if index is not None:
				self.tasks[index]['status'] = status
				self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

			self.save_tasks()

			return self.tasks[index]
		except Exception as error:
			raise Exception('Unknown error while marking task') from error
