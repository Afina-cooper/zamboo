# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: IdeaSprint
def migrate_structure(old_data, version=46):
    """
    Миграция структуры данных IdeaSprint.
    Переводит старые данные в новую структуру с оценками и результатами.
    """
    if version < 46:
        migrated = []
        for idea in old_data:
            if isinstance(idea, dict):
                new_idea = {
                    'hypothesis': idea.get('hypothesis', ''),
                    'task': idea.get('task', ''),
                    'estimation': idea.get('estimation', 0),
                    'result': idea.get('result', ''),
                    'status': idea.get('status', 'new'),
                }
                migrated.append(new_idea)
            elif isinstance(idea, list):
                migrated.append([migrate_structure(item, version) for item in idea])
            else:
                migrated.append(idea)
        return migrated

    return old_data
