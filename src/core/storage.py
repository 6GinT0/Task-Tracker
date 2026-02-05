import json
from pathlib import Path
from typing import Any, Dict, List


class JsonStorage:
	def __init__(self, file_path: Path):
		self.file_path = file_path
		self._ensure_file_exists()

	def _ensure_file_exists(self) -> None:
		if not self.file_path.exists():
			self.save([])

	def load(self) -> List[Dict[str, Any]]:
		with open(self.file_path, encoding='utf-8') as f:
			try:
				return json.load(f)
			except json.JSONDecodeError:
				return []

	def save(self, data: List[Dict[str, Any]]) -> None:
		with open(self.file_path, 'w', encoding='utf-8') as f:
			json.dump(data, f, indent=4)
