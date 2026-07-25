# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: IdeaSprint
def parse_date(s):
    """Парсит дату из строки. Возвращает datetime или None с понятным ошибкой."""
    if not s or not isinstance(s, str):
        return None, "Дата не может быть пустой"
    for fmt in ("%Y-%m-%d", "%d.%m.%y", "%d/%m/%Y", "%Y%m%d"):
        try:
            return datetime.strptime(s.strip(), fmt), None
        except ValueError:
            continue
    return None, f"Неизвестный формат даты: '{s}'"

def format_date(d):
    """Форматирует дату для вывода."""
    if not isinstance(d, datetime):
        return "—"
    try:
        return d.strftime("%d.%m.%Y")
    except Exception:
        return str(d)
