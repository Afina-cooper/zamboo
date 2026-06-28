# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: IdeaSprint
def load_initial_data(json_string):
    import json
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        initial_hypotheses = data.get('hypotheses', [])
        initial_tasks = data.get('tasks', [])
        initial_results = data.get('results', [])
        
        for h in initial_hypotheses:
            hypothesis_id = h['id'] or len([x for x in hypotheses if not hasattr(x, 'id')]) + 1
            h['id'] = hypothesis_id
            hypotheses.append(h)
            
        for t in initial_tasks:
            task_id = t['id'] or len(tasks) + 1
            t['id'] = task_id
            tasks.append(t)
            
        for r in initial_results:
            result_id = r['id'] or len(results) + 1
            r['id'] = result_id
            results.append(r)
            
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
