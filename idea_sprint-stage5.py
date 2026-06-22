# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: IdeaSprint
def delete_record(record_id: int) -> bool:
    """Удаление записи по ID с безопасной обработкой отсутствия объекта."""
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    del records[record_id]
    print(f"Запись с ID {record_id} успешно удалена.")
    return True

def get_record_safe(record_id: int) -> dict | None:
    """Получение записи по ID, возвращает None если запись отсутствует."""
    return records.get(record_id, None)
