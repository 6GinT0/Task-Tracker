from datetime import datetime
from typing import Any, Dict, List, Optional

from core.enums import TaskStatus
from core.storage import JsonStorage


class TaskManager:
	def __init__(self, storage: JsonStorage):
		self.storage = storage
		self.tasks: List[Dict[str, Any]] = self.storage.load()

	def _save(self) -> None:
		self.storage.save(self.tasks)

	def add_task(self, description: str) -> Dict[str, Any]:
		self.tasks.append(
			{
				'id': self.tasks[-1]['id'] + 1 if self.tasks else 1,
				'description': description,
				'status': TaskStatus.TODO.value,
				'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
				'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			}
		)

		self._save()

		return self.tasks[-1]

	def update_task(self, id: int, description: str) -> Dict[str, Any]:
		index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

		if index is not None:
			self.tasks[index]['description'] = description
			self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		else:
			raise ValueError(f'Task with ID {id} not found')

		self._save()

		return self.tasks[index]

	def delete_task(self, id: int) -> List[Dict[str, Any]]:
		self.tasks = list(filter(lambda task: task['id'] != id, self.tasks))

		self._save()

		return self.tasks

	def get_tasks(self) -> List[Dict[str, Any]]:
		return self.tasks

	def get_task(self, id: int) -> Optional[Dict[str, Any]]:
		return next((task for task in self.tasks if task['id'] == id), None)

	def get_tasks_by_status(self, status: str) -> List[Dict[str, Any]]:
		return list(filter(lambda task: task['status'] == status, self.tasks))

	def mark_task(self, id: int, status: TaskStatus) -> Dict[str, Any]:
		# Validación extra por seguridad, aunque el Enum ayuda
		if status not in [s.value for s in TaskStatus]:
			raise ValueError(f'Invalid status: {status}')

		index = next((i for i, task in enumerate(self.tasks) if task['id'] == id), None)

		if index is not None:
			self.tasks[index]['status'] = status.value
			self.tasks[index]['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		else:
			raise ValueError(f'Task with ID {id} not found')

		self._save()

		return self.tasks[index]
