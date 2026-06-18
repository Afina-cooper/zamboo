# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: IdeaSprint
class IdeaModel:
    def __init__(self):
        self._data = {}
    
    def add_idea(self, hypothesis: str, task: str, estimate: int) -> bool:
        if not isinstance(hypothesis, str) or len(hypothesis.strip()) < 3:
            return False
        if not isinstance(task, str) or len(task.strip()) < 5:
            return False
        if not isinstance(estimate, int) or estimate < 1 or estimate > 10:
            return False
        self._data[hypothesis] = {"task": task, "estimate": estimate}
        return True
    
    def get_idea(self, hypothesis: str):
        return self._data.get(hypothesis)

def validate_input(user_input: dict) -> tuple[bool, list[str]]:
    errors = []
    if not isinstance(user_input, dict):
        return False, ["Ввод должен быть словарем."]
    
    required_keys = {"hypothesis", "task", "estimate"}
    missing = required_keys - set(user_input.keys())
    if missing:
        errors.append(f"Отсутствуют ключи: {', '.join(missing)}")
        return False, errors
    
    hypothesis = user_input["hypothesis"]
    task = user_input["task"]
    estimate = user_input["estimate"]
    
    if not isinstance(hypothesis, str) or len(hypothesis.strip()) < 3:
        errors.append("Гипотеза должна быть строкой длиной не менее 3 символов.")
    
    if not isinstance(task, str) or len(task.strip()) < 5:
        errors.append("Задача должна быть строкой длиной не менее 5 символов.")
    
    if estimate is None and "estimate" in user_input:
         pass # Already handled by type check above
    
    try:
        int_val = int(estimate)
        if int_val < 1 or int_val > 10:
            errors.append("Оценка должна быть целым числом от 1 до 10.")
    except (ValueError, TypeError):
        errors.append("Оценка должна быть целым числом.")
    
    return len(errors) == 0, errors
