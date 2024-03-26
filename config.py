import json
from pathlib import Path

_STR_URL = 'url'
_STR_URLS = 'urls'
_STR_CATEGORY = 'category'
_STR_DEFAULT_CATEGORY = 'default_category'
_CONFIG_ENCODING='utf-8'

def load_config(input_path: Path) -> list:
	result = []
	data = []
	default_category = []
	
	with input_path.open(encoding=_CONFIG_ENCODING) as f:
		data = json.load(f)
	
	if len(data) == 0: return []
	
	default_category = data[_STR_DEFAULT_CATEGORY]
	for elem in data[_STR_URLS]:
		category = elem.get(_STR_CATEGORY, default_category)
		result.append([elem[_STR_URL], category])
	
	return result
