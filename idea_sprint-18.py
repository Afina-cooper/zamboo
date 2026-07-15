# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: IdeaSprint
def add_tag(item_id, tag):
    """Добавить тег к элементу."""
    items = _load_items()
    if item_id not in items:
        print(f"Ошибка: элемент {item_id} не найден")
        return False
    item = items[item_id]
    tags = item.get("tags", [])
    if tag in tags:
        print(f"Тег '{tag}' уже существует у элемента {item_id}")
        return False
    tags.append(tag)
    _save_items(items)
    print(f"Тег '{tag}' добавлен к элементу {item_id}: {', '.join(tags)}")
    return True

def remove_tag(item_id, tag):
    """Удалить тег из элемента."""
    items = _load_items()
    if item_id not in items:
        print(f"Ошибка: элемент {item_id} не найден")
        return False
    item = items[item_id]
    tags = item.get("tags", [])
    if tag not in tags:
        print(f"Тег '{tag}' отсутствует у элемента {item_id}")
        return False
    tags.remove(tag)
    _save_items(items)
    print(f"Тег '{tag}' удалён из элемента {item_id}: {', '.join(tags)}")
    return True

def list_tags(item_id):
    """Показать все теги элемента."""
    items = _load_items()
    if item_id not in items:
        print(f"Ошибка: элемент {item_id} не найден")
        return []
    tags = items[item_id].get("tags", [])
    return tags

def list_all_tags():
    """Показать все уникальные теги по всем элементам."""
    items = _load_items()
    all_tags = set()
    for item in items.values():
        all_tags.update(item.get("tags", []))
    return sorted(all_tags)
