# === Stage 17: Добавь группировку записей по категориям ===
# Project: IdeaSprint
from collections import defaultdict


def group_by_category(records, key_extractor):
    grouped = defaultdict(list)
    for rec in records:
        cat = key_extractor(rec) or "без_категории"
        grouped[cat].append(rec)
    return dict(grouped)
