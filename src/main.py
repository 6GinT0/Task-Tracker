from pathlib import Path

from core.commands import parser
from core.enums import TaskStatus
from core.storage import JsonStorage
from core.task_manager import TaskManager
from ui.window import WindowCLI

# Configuración de rutas y dependencias
ROOT_DIR = Path(__file__).resolve().parents[1]
TASKS_FILE = ROOT_DIR / 'tasks.json'

storage = JsonStorage(TASKS_FILE)
task_manager = TaskManager(storage)
window_cli = WindowCLI()


def main():
	args = parser.parse_args()
	command = args.command

	try:
		if command == 'add':
			new_task = task_manager.add_task(args.description)

			print(f'Task added successfully (ID: {new_task["id"]})')
		elif command == 'update':
			task_manager.update_task(args.id, args.description)
		elif command == 'delete':
			task_manager.delete_task(args.id)
		elif command == 'list':
			if args.status:
				window_cli.render(task_manager.get_tasks_by_status(args.status))

				return

			window_cli.render(task_manager.get_tasks())

			return
		elif command == 'mark-todo':
			task_manager.mark_task(args.id, TaskStatus.TODO)
		elif command == 'mark-in-progress':
			task_manager.mark_task(args.id, TaskStatus.IN_PROGRESS)
		elif command == 'mark-done':
			task_manager.mark_task(args.id, TaskStatus.DONE)

		if command not in ['list', 'add', 'delete', 'update']:
			window_cli.render(task_manager.get_tasks())
	except ValueError as e:
		print(f'Error: {e}')
	except Exception as e:
		print(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
	main()
