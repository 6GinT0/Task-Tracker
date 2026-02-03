from pathlib import Path

from core.commands import parser
from core.task_manager import TaskManager
from ui.window import WindowCLI

task_manager = TaskManager(Path(__file__).resolve().parents[1] / 'tasks.json')
window_cli = WindowCLI()


def main():
	args = parser.parse_args()
	command = args.command

	if command == 'add':
		task_manager.add_task(args.description)
	elif command == 'update':
		task_manager.update_task(args.id, args.description)
	elif command == 'delete':
		task_manager.delete_task(args.id)
	elif command == 'list':
		if args.status:
			window_cli.render(task_manager.get_tasks_by_status(args.status))

			return
	elif command == 'mark-todo':
		task_manager.mark_task(args.id, 'todo')
	elif command == 'mark-in-progress':
		task_manager.mark_task(args.id, 'in-progress')
	elif command == 'mark-done':
		task_manager.mark_task(args.id, 'done')

	window_cli.render(task_manager.get_tasks())


if __name__ == '__main__':
	main()
