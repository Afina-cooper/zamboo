# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: IdeaSprint
import json, os

DATA_FILE = "ideasprint_data.json"

def save_to_json(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('ideas', [])
    except (json.JSONDecodeError, IOError):
        return []

def get_or_create_data():
    if not os.path.exists(DATA_FILE):
        save_to_json({'ideas': [], 'settings': {}})
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except (json.JSONDecodeError, IOError):
            data = {'ideas': [], 'settings': {}}
    return data

def add_idea(idea_dict):
    data = get_or_create_data()
    if 'ideas' not in data:
        data['ideas'] = []
    data['ideas'].append(idea_dict)
    save_to_json(data)
