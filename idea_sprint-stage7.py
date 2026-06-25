# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: IdeaSprint
def sort_records(records, key='date'):
    if not records: return []
    reverse = False
    if key == 'priority':
        def _sort(r): return -r.get('priority', 0)
        reverse = True
    elif key == 'name':
        def _sort(r): return r.get('name', '').lower()
    else: # date or default
        def _sort(r): return r.get(key, datetime.min).isoformat() if isinstance(r[key], datetime) else str(r.get(key, ''))
    return sorted(records, key=_sort, reverse=reverse)
