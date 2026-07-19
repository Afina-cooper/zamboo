# === Stage 20: Добавь восстановление записей из архива ===
# Project: IdeaSprint
import json, os

ARCHIVE_FILE = "idea_sprint_archive.json"


def load_archived_ideas():
    """Загружает записи из архива и возвращает список. Если файл отсутствует — пустой список."""
    if not os.path.exists(ARCHIVE_FILE):
        return []
    try:
        with open(ARCHIVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        raise ValueError("Некорректный формат архива")
    except (json.JSONDecodeError, ValueError):
        print("⚠️  Архив повреждён — начнём с нуля.")
        os.remove(ARCHIVE_FILE)
        return []


def archive_idea(idea: dict) -> None:
    """Архивирует идею в отдельный файл. Формат записи: {id, title, hypothesis, task, score, result, archived_at}."""
    import datetime
    record = {
        "id": idea.get("id"),
        "title": idea.get("title"),
        "hypothesis": idea.get("hypothesis"),
        "task": idea.get("task"),
        "score": idea.get("score", 0),
        "result": idea.get("result"),
        "archived_at": datetime.datetime.now().isoformat()
    }
    records = load_archived_ideas()
    if not isinstance(records, list):
        records = []
    records.append(record)
    with open(ARCHIVE_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
