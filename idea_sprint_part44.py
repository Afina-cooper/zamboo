# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: IdeaSprint
def backup_data_file(data_file):
    """Create a timestamped backup of the data file and return the backup path."""
    if not data_file:
        return None
    backup_dir = os.path.join(os.path.dirname(data_file), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}.txt")
    try:
        with open(data_file, "r", encoding="utf-8") as src, open(backup_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        return backup_path
    except Exception:
        return None
