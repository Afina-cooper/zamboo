# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: IdeaSprint
import copy

class DryRunRegistry:
    def __init__(self):
        self._logs = []
        self._enabled = False

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def execute(self, action, payload):
        if not self._enabled:
            return action(payload)
        log_entry = {
            "action": action.__name__,
            "payload": copy.deepcopy(payload),
            "status": "dry-run"
        }
        self._logs.append(log_entry)
        print(f"[DRY-RUN] {action.__name__}: {payload}")
        return None

    def get_logs(self):
        return self._logs

    def clear(self):
        self._logs.clear()
