# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: IdeaSprint
import json, os

def load_from_json(file_path):
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'items' in data:
            return data['items']
        print("Неверный формат JSON файла.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []

# Пример вызова (раскомментируйте при наличии файла)
# ideas = load_from_json('ideas.json')
