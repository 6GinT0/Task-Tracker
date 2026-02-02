from rich.console import Console
from rich.table import Table


class WindowCLI:
	def __init__(self):
		self.console = Console()

	def render(self, tasks):
		table = Table(title='List of tasks', expand=True)
		table.add_column('ID', justify='center', no_wrap=True)
		table.add_column('Description', justify='center')
		table.add_column('Status', justify='center')
		table.add_column('Created At', justify='center')

		for task in tasks:
			table.add_row(str(task['id']), task['description'], task['status'], task['createdAt'])

		self.console.print(table)
