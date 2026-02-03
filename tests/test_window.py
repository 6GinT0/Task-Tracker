from unittest.mock import patch

from rich.table import Table

from src.ui.window import WindowCLI


@patch('src.ui.window.Console')
def test_render_creates_table(mock_console_class):
	mock_console_instance = mock_console_class.return_value
	window = WindowCLI()

	tasks = [{'id': 1, 'description': 'Test Task', 'status': 'todo', 'createdAt': '2023-01-01'}]

	window.render(tasks)

	mock_console_instance.print.assert_called_once()

	args, _ = mock_console_instance.print.call_args
	printed_object = args[0]

	assert isinstance(printed_object, Table)
