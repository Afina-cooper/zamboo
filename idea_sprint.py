# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: IdeaSprint
import json, uuid
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional, List

@dataclass
class SprintItem:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str  # hypothesis|task|result
    title: str
    description: str = ""
    status: str = "todo"  # todo|done|blocked
    score: int = 0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

def init_demo_data() -> List[SprintItem]:
    return [
        SprintItem(type="hypothesis", title="Улучшить UX входа", description="Сократить время регистрации до 15 сек"),
        SprintItem(type="task", title="Прототип формы входа", status="done", score=3),
        SprintItem(type="result", title="Время регистрации: 12 сек", description="Цель достигнута"),
    ]

if __name__ == "__main__":
    items = init_demo_data()
    print(json.dumps([asdict(i) for i in items], indent=2))
