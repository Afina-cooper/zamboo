# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: IdeaSprint
class IdeaSearch:
    def __init__(self, ideas):
        self.ideas = ideas
    
    def search(self, query=None, fields=None):
        if not fields:
            fields = ['hypothesis', 'task']
        
        results = []
        for idea in self.ideas:
            match_score = 0
            normalized_query = (query or '').lower().split()
            
            for field_name in fields:
                value = getattr(idea, field_name, '')
                if not isinstance(value, str): continue
                
                words_in_field = set(word.lower() for word in value.split())
                
                if query is None and len(normalized_query) == 0:
                    match_score += 1.0
                else:
                    matched_words = [w for w in normalized_query if w in words_in_field]
                    if matched_words:
                        match_score += len(matched_words) / max(len(normalized_query), 1)
            
            if match_score > 0 or (query is None and fields):
                results.append((match_score, idea))
        
        return sorted(results, key=lambda x: x[0], reverse=True)
