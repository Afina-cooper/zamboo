# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: IdeaSprint
def generate_summary(project):
    """Генерирует краткую сводку по текущим данным проекта IdeaSprint."""
    lines = ["=== СВОДКА ПРОЕКТА IDEASPRINT ==="]
    
    # Сводка по гипотезам
    hypotheses = project.get("hypotheses", [])
    if hypotheses:
        active_hyp = [h for h in hypotheses if not h.get("resolved")]
        lines.append(f"\n📊 Гипотезы:")
        lines.append(f"   Всего: {len(hypotheses)}, Активных: {len(active_hyp)}")
        for hyp in active_hyp[:5]:  # Ограничиваем вывод до 5 гипотез
            name = hyp.get("name", "Без имени")
            status = hyp.get("status", "Н/Д")
            lines.append(f"   • {name} [{status}]")
    
    # Сводка по задачам
    tasks = project.get("tasks", [])
    if tasks:
        active_tasks = [t for t in tasks if not t.get("completed")]
        done_tasks = [t for t in tasks if t.get("completed")]
        lines.append(f"\n✅ Задачи:")
        lines.append(f"   Всего: {len(tasks)}, Выполнено: {len(done_tasks)}, В работе: {len(active_tasks)}")
    
    # Сводка по оценкам (если есть)
    evaluations = project.get("evaluations", [])
    if evaluations:
        avg_score = sum(e.get("score", 0) for e in evaluations) / len(evaluations) if evaluations else 0
        lines.append(f"\n📈 Оценки:")
        lines.append(f"   Средняя оценка: {avg_score:.1f}")
    
    # Сводка по результатам (если есть)
    results = project.get("results", [])
    if results:
        lines.append(f"\n🏆 Результаты:")
        for r in results[:3]:  # Ограничиваем вывод до 3 результатов
            title = r.get("title", "Без названия")
            date = r.get("date", "")
            lines.append(f"   • {title} ({date})")
    
    return "\n".join(lines)
