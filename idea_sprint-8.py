# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: IdeaSprint
import sys, os, json, random, time
from datetime import datetime

def print_menu():
    print("\n=== IDEA SPRINT: Меню действий ===")
    print("1. Показать все идеи")
    print("2. Добавить новую идею")
    print("3. Удалить идею по ID")
    print("4. Обновить статус задачи")
    print("5. Вывести статистику")
    print("0. Выход")

def load_data():
    path = "ideas_sprint.json"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"ideas": [], "last_id": 0}

def save_data(data):
    with open("ideas_sprint.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def show_all(ideas):
    if not ideas:
        print("\nСписок идей пуст.")
        return
    for i, idea in enumerate(ideas, 1):
        status = "✅" if idea.get("done") else "⏳"
        task_status = "🔴" if idea.get("task_done") else "⚪"
        print(f"{i}. [{idea['id']}] {status} | Гипотеза: {idea['hypothesis']}")
        print(f"   Задача: {idea['task']} ({task_status}) | Оценка: {idea.get('score', 'N/A')}")

def add_idea():
    hypothesis = input("Введите гипотезу: ")
    task = input("Опишите задачу для проверки: ")
    score = int(input("Начальная оценка (0-10): ")) or 0
    ideas, last_id = load_data()
    new_id = last_id + 1
    idea = {
        "id": new_id,
        "hypothesis": hypothesis,
        "task": task,
        "score": score,
        "done": False,
        "task_done": False,
        "created_at": datetime.now().isoformat()
    }
    ideas.append(idea)
    last_id = new_id
    save_data({"ideas": ideas, "last_id": last_id})
    print(f"Идея #{new_id} добавлена.")

def delete_idea():
    try:
        idx = int(input("Введите ID идеи для удаления (или 0 чтобы отменить): ")) - 1
        if idx < 0 or idx >= len(ideas_list):
            print("Неверный ID.")
            return
        ideas_list.pop(idx)
        save_data({"ideas": ideas_list, "last_id": max([i["id"] for i in ideas_list], default=0)})
        print(f"Идея #{idx + 1} удалена.")
    except ValueError:
        print("Ошибка ввода ID.")

def update_task_status():
    try:
        idx = int(input("Введите ID идеи для обновления задачи (или 0 чтобы отменить): ")) - 1
        if idx < 0 or idx >= len(ideas_list):
            return
        ideas_list[idx]["task_done"] = not ideas_list[idx].get("task_done", False)
        save_data({"ideas": ideas_list, "last_id": max([i["id"] for i in ideas_list], default=0)})
        print(f"Статус задачи для идеи #{idx + 1} обновлен.")
    except ValueError:
        print("Ошибка ввода ID.")

def show_stats():
    if not ideas_list:
        return
    total = len(ideas_list)
    done_count = sum(1 for i in ideas_list if i.get("done"))
    task_done_count = sum(1 for i in ideas_list if i.get("task_done"))
    avg_score = sum(i.get("score", 0) for i in ideas_list) / total if total else 0
    print(f"\nСтатистика: Всего идей: {total}, Завершено: {done_count}, Готовы задачи: {task_done_count}")
    print(f"Средняя оценка гипотез: {avg_score:.1f}")

# Основной цикл CLI
ideas_list = load_data()["ideas"]
print_menu()
while True:
    choice = input("\nВаш выбор (0-5): ")
    if choice == "1":
        show_all(ideas_list)
    elif choice == "2":
        add_idea()
    elif choice == "3":
        delete_idea()
    elif choice == "4":
        update_task_status()
    elif choice == "5":
        show_stats()
    elif choice == "0":
        print("Выход из IdeaSprint.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
