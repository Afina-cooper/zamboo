# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: IdeaSprint
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status is not None and record.get('status') != status:
            continue
        if category is not None and record.get('category') != category:
            continue
        if tags is not None:
            record_tags = set(record.get('tags', []))
            if not any(tag in record_tags for tag in tags):
                continue
        filtered.append(record)
    return filtered
