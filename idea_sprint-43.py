# === Stage 43: Добавь пагинацию длинных списков ===
# Project: IdeaSprint
def paginate(items, page_size=10):
    """Returns (current_page, total_pages, items_on_page)."""
    total_pages = max(1, len(items) // page_size + (1 if len(items) % page_size else 0))
    current_page = min(1, max(1, total_pages))
    start = (current_page - 1) * page_size
    end = min(start + page_size, len(items))
    page_items = items[start:end]
    return page_items, current_page, total_pages
