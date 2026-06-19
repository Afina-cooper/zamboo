# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: IdeaSprint
class IdeaSprint:
    def __init__(self):
        self.records = []
    
    def add_record(self, hypothesis: str, task: str, estimate: int, result: str) -> None:
        record = {
            "hypothesis": hypothesis,
            "task": task,
            "estimate": estimate,
            "result": result
        }
        self.records.append(record)

    def get_records(self):
        return self.records
