# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: IdeaSprint
def monthly_stats(data, year):
    """Returns dict of month -> list of records for a given year."""
    stats = {}
    for record in data:
        date_str = record.get('date', '')
        if len(date_str) < 7 or not date_str[4] == '-' or not date_str[6] == '-':
            continue
        month_short, day = int(date_str[5:7]), int(date_str[8:10])
        month_name = {1:'Янв',2:'Фев',3:'Мар',4:'Апр',5:'Май',6:'Июн',
                      7:'Июл',8:'Авг',9:'Сен',10:'Окт',11:'Ноя',12:'Дек'}.get(month_short, '')
        if month_name:
            stats.setdefault(f'{year}-{month_name}', []).append(record)
    return stats

def print_monthly_stats(stats):
    """Pretty-prints monthly statistics in a table-like format."""
    if not stats:
        print("Нет данных по месяцам.")
        return
    months = sorted(stats.keys())
    print(f"\n{'Месяц':<12} {'Количество идей':>16}")
    for m in months:
        print(f"{m:<12} {len(stats[m]):>16}")

# Пример использования:
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'title': 'Идея 1', 'date': '2024-01-15'},
        {'id': 2, 'title': 'Идея 2', 'date': '2024-01-20'},
        {'id': 3, 'title': 'Идея 3', 'date': '2024-02-05'},
    ]
    monthly = monthly_stats(sample_data, 2024)
    print_monthly_stats(monthly)
