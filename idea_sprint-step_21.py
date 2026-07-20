# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: IdeaSprint
class Reminder:
    def __init__(self, task, due_date):
        self.task = task
        self.due_date = due_date

    @staticmethod
    def check_reminders(reminders_list, today=None):
        if today is None:
            from datetime import date
            today = date.today()
        urgent = []
        for r in reminders_list:
            if isinstance(r.due_date, str):
                due = datetime.strptime(r.due_date[:10], "%Y-%m-%d").date()
            else:
                due = r.due_date
            if due <= today:
                urgent.append((r.task, due))
        return sorted(urgent, key=lambda x: x[1])

    @staticmethod
    def add_reminder(reminders_list, task, due_date):
        reminders_list.append(Reminder(task, due_date))
