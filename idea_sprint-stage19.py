# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: IdeaSprint
def archive_completed(records):
    """Archive records marked as completed or older than 30 days."""
    today = datetime.date.today()
    archived = []
    for rec in records:
        if rec.get("status") == "completed":
            archived.append(rec)
        elif rec.get("created", "").strip():
            try:
                created = datetime.strptime(rec["created"], "%Y-%m-%d").date()
                if (today - created).days > 30:
                    rec["status"] = "archived"
                    archived.append(rec)
            except ValueError:
                pass
    return records, archived
