# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: IdeaSprint
def print_project_metrics():
    """Print key project metrics."""
    tasks = db["tasks"]
    ideas = db["ideas"]
    results = db["results"]
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.get("status") == "completed")
    task_completion_rate = (completed_tasks / total_tasks * 100) if total_tasks else 0
    
    total_ideas = len(ideas)
    implemented_ideas = sum(1 for i in ideas if i.get("implemented", False))
    idea_implement_rate = (implemented_ideas / total_ideas * 100) if total_ideas else 0
    
    total_results = len(results)
    positive_outcomes = sum(1 for r in results if r.get("outcome") == "positive")
    success_rate = (positive_outcomes / total_results * 100) if total_results else 0
    
    print(f"📊 Project Metrics:")
    print(f"   Tasks: {total_tasks} total, {completed_tasks} completed ({task_completion_rate:.1f}%)")
    print(f"   Ideas: {total_ideas} total, {implemented_ideas} implemented ({idea_implement_rate:.1f}%)")
    print(f"   Results: {total_results} total, {positive_outcomes} positive ({success_rate:.1f}%)")
