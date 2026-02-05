import argparse

from core.enums import TaskStatus

parser = argparse.ArgumentParser(description='Task Tracker CLI')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description', type=str, help='Description of the task')

update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int, help='ID of the task')
update_parser.add_argument('description', type=str, help='Description of the task')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id', type=int, help='ID of the task')

list_parser = subparsers.add_parser('list')
list_parser.add_argument(
	'status',
	type=str,
	help='Status of the task',
	nargs='?',
	choices=[status.value for status in TaskStatus],
)

mark_todo_parser = subparsers.add_parser('mark-todo')
mark_todo_parser.add_argument('id', type=int, help='ID of the task')

mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
mark_in_progress_parser.add_argument('id', type=int, help='ID of the task')

mark_done_parser = subparsers.add_parser('mark-done')
mark_done_parser.add_argument('id', type=int, help='ID of the task')
