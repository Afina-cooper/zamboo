# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: IdeaSprint
import json


TEMPLATES = {
    "idea": {"title": "Гипотеза", "type": "idea", "priority": "medium"},
    "task": {"title": "Задача", "type": "task", "priority": "high"},
    "result": {"title": "Результат", "type": "result", "priority": "medium"}
}


def create_from_template(template_name, **overrides):
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    record = {**TEMPLATES[template_name]}
    record.update(overrides)
    return record


def list_templates():
    return list(TEMPLATES.keys())
