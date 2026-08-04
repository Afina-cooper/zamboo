# === Stage 32: Добавь журнал действий пользователя ===
# Project: IdeaSprint
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "action": action_type,
            "details": details
        }
        self.entries.append(entry)
        return entry

    def get(self):
        return list(reversed(self.entries))  # newest first
