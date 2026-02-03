import json

import pytest

from src.core.task_manager import TaskManager


@pytest.fixture
def task_manager(tmp_path):
	temp_file = tmp_path / 'tasks_test.json'

	return TaskManager(temp_file)


def test_add_task(task_manager):
	task = task_manager.add_task('Comprar leche')

	assert task['description'] == 'Comprar leche'
	assert task['id'] == 1
	assert task['status'] == 'todo'
	assert len(task_manager.get_tasks()) == 1


def test_data_persistence(tmp_path):
	temp_file = tmp_path / 'tasks_test.json'
	manager = TaskManager(temp_file)
	manager.add_task('Persistencia')

	with open(temp_file) as f:
		data = json.load(f)

	assert len(data) == 1
	assert data[0]['description'] == 'Persistencia'


def test_update_task(task_manager):
	task = task_manager.add_task('Tarea original')
	updated = task_manager.update_task(task['id'], 'Tarea actualizada')

	assert updated['description'] == 'Tarea actualizada'
	assert task_manager.get_task(task['id'])['description'] == 'Tarea actualizada'


def test_delete_task(task_manager):
	task = task_manager.add_task('Para borrar')
	task_manager.delete_task(task['id'])

	assert len(task_manager.get_tasks()) == 0


def test_mark_task_status(task_manager):
	task = task_manager.add_task('Tarea nueva')
	task_manager.mark_task(task['id'], 'in-progress')

	assert task_manager.get_task(task['id'])['status'] == 'in-progress'


def test_mark_task_invalid_status(task_manager):
	task = task_manager.add_task('Tarea')

	with pytest.raises(Exception) as excinfo:
		task_manager.mark_task(task['id'], 'invalid-status')

	assert 'Invalid status' in str(excinfo.value)
