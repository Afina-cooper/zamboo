# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: IdeaSprint
def print_record(record):
    if not record:
        return "Нет записи."
    name = record.get('name', 'Без имени')
    status = record.get('status', 'Неизвестно')
    hypothesis = record.get('hypothesis', '')
    tasks = record.get('tasks', [])
    results = record.get('results', [])
    
    print(f"\n📋 Запись: {name} [{status}]")
    if hypothesis:
        print(f"   Гипотеза: {hypothesis}")
    for task in tasks:
        t_name = task.get('task', 'Без задачи')
        t_score = task.get('score', 0)
        t_result = task.get('result', '')
        print(f"   • Задача: {t_name} — Оценка: {t_score}, Результат: {t_result}")
    for result in results:
        r_metric = result.get('metric', 'Без метрики')
        r_value = result.get('value', 0)
        print(f"   ✅ Метрика: {r_metric} — Значение: {r_value}")

demo_data = [
    {"name": "Быстрый старт", "status": "Завершена", "hypothesis": "Простой интерфейс ускорит работу.", 
     "tasks": [{"task": "Установка проекта", "score": 5, "result": "Готово"}, {"task": "Создание структуры", "score": 3, "result": "Готово"}],
     "results": [{"metric": "Время на задачу", "value": "10 мин"}, {"metric": "Количество багов", "value": 2}]},
    {"name": "Добавить оценки", "status": "В работе", "hypothesis": "", 
     "tasks": [{"task": "Система баллов", "score": 4, "result": "Тестирование"}],
     "results": []}
]

for rec in demo_data:
    print_record(rec)
