# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: IdeaSprint
class UndoManager:
    """Откат последнего действия: добавляем в конец файла."""

    def __init__(self):
        self._history = []

    def record(self, action):
        self._history.append(action)

    def undo(self):
        if not self._history:
            print("Нет действий для отката.")
            return None
        action = self._history.pop()
        print(f"Откат: {action}")
        return action

    def history(self):
        return list(reversed(self._history))

    def clear(self):
        self._history.clear()
