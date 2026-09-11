# === Stage 45: Добавь восстановление из резервной копии ===
# Project: IdeaSprint
import json, os, sys

def load_backup(backup_path):
    if os.path.exists(backup_path):
        with open(backup_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def restore_backup(backup_path, filename, overwrite):
    backup = load_backup(backup_path)
    if backup is None:
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(backup)
    print(f"Резервная копия восстановлена: {filename}")
    return True
