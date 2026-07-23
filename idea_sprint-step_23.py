# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: IdeaSprint
def print_board_table():
    if not data:
        print("Доска пуста.")
        return
    headers = ["ID", "Тип", "Статус", "Оценка", "Автор"]
    widths = [len(h) for h in headers]
    rows = []
    for item in data:
        row = [str(item.get(h, "")) for h in headers]
        rows.append(row)
        for i, val in enumerate(row):
            if len(val) > widths[i]:
                widths[i] = len(val)
    print("┌" + "─" * sum(widths) + "┐")
    sep = "│" + "─" * sum(widths) + "│"
    print(sep)
    header_line = "│" + "".join(f"{h:<{w}}" for h, w in zip(headers, widths)) + "│"
    print(header_line)
    print(sep)
    data_lines = []
    for row in rows:
        line = "│" + "".join(f"{v:<{w}}" for v, w in zip(row, widths)) + "│"
        data_lines.append(line)
    max_data_len = max(len(l) for l in data_lines) if data_lines else 0
    total_width = sum(widths)
    print(" " * (total_width - 1) + "└" + "─" * sum(widths) + "┘")
    lines = []
    for line in data_lines:
        lines.append(line + "\n")
    longest = max(lines, key=len) if lines else ""
    print(longest.rstrip())
