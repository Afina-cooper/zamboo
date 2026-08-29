# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: IdeaSprint
def repair_simple_problems(board):
    """Repair simple problems: fix broken links, empty labels, and invalid ratings."""
    for i in range(len(board)):
        item = board[i]
        if item.get("broken_link"):
            item["broken_link"] = None
        if not item.get("label"):
            item["label"] = "No Label"
        if item.get("rating") not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            item["rating"] = 1
        if item.get("status") not in ["draft", "active", "done"]:
            item["status"] = "draft"
    return board
