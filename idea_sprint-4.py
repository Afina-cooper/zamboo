# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: IdeaSprint
def edit_record(record_id: int, new_data: dict) -> bool:
    if not isinstance(records, list):
        return False
    for i, record in enumerate(records):
        if record.get('id') == record_id:
            records[i].update(new_data)
            print(f"Запись #{record_id} обновлена.")
            return True
    print("Запись с таким ID не найдена.")
    return False
