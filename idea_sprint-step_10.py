# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: IdeaSprint
def export_to_json():
    import json
    data = {
        "hypotheses": hypotheses,
        "tasks": tasks,
        "evaluations": evaluations,
        "results": results,
        "metadata": {
            "version": 10,
            "timestamp": datetime.now().isoformat() if 'datetime' in globals() else None
        }
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
