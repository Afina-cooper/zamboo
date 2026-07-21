# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: IdeaSprint
def check_overdue_reminders():
    reminders = get_all_reminders()
    now = time.time()
    overdue = [r for r in reminders if r['deadline'] and r['created_at'] < now - 604800]
    if overdue:
        print("\n⚠️ Просроченные напоминания:")
        for item in overdue:
            print(f"  - {item.get('name', 'Без имени')} (срок: {item['deadline']})")
