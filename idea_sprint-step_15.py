# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: IdeaSprint
def weekly_stats(records):
    """Calculate per-week summary: count, avg effort, avg result."""
    if not records:
        return []
    from datetime import datetime
    weeks = {}
    for r in records:
        date = r.get("date") or r.get("created_at")
        try:
            dt = datetime.fromisoformat(date)
        except (ValueError, TypeError):
            continue
        week_key = dt.isocalendar()[:2]  # (year, week_number)
        if week_key not in weeks:
            weeks[week_key] = {"count": 0, "efforts": [], "results": []}
        weeks[week_key]["count"] += 1
        weeks[week_key]["efforts"].append(r.get("effort", r.get("points", 0)))
        weeks[week_key]["results"].append(r.get("result", r.get("outcome", 0)))
    return [
        {**v, "avg_effort": sum(v["efforts"], 0) / v["count"], "avg_result": sum(v["results"], 0) / v["count"]}
        for v in weeks.values()
    ]
