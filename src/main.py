from core.commands import parser
from core.task_manager import TaskManager
from ui.window import WindowCLI

task_manager = TaskManager()
window_cli = WindowCLI()


def main():
	args = parser.parse_args()

	if args.command == 'add':
		task_manager.add_task(args.description)

		window_cli.render(task_manager.get_tasks())
	elif args.command == 'update':
		task_manager.update_task(args.id, args.description)

		window_cli.render(task_manager.get_tasks())
	elif args.command == 'delete':
		task_manager.delete_task(args.id)

		window_cli.render(task_manager.get_tasks())
	elif args.command == 'list':
		if args.status:
			window_cli.render(task_manager.get_tasks_by_status(args.status))
		else:
			window_cli.render(task_manager.get_tasks())
	elif args.command == 'mark-todo':
		task_manager.mark_task(args.id, 'todo')

		window_cli.render(task_manager.get_tasks())
	elif args.command == 'mark-in-progress':
		task_manager.mark_task(args.id, 'in-progress')

		window_cli.render(task_manager.get_tasks())
	elif args.command == 'mark-done':
		task_manager.mark_task(args.id, 'done')

		window_cli.render(task_manager.get_tasks())


if __name__ == '__main__':
	main()
