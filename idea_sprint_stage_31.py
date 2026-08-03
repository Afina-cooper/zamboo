# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: IdeaSprint
import json, os

class ProfileManager:
    def __init__(self, db_path='profiles.json'):
        self.db_path = db_path
        
    def load_profiles(self):
        if not os.path.exists(self.db_path):
            return {'default': {'name': 'Default User', 'email': ''}}
        with open(self.db_path, 'r') as f:
            return json.load(f)
    
    def save_profiles(self, profiles):
        with open(self.db_path, 'w') as f:
            json.dump(profiles, f, indent=2)
    
    def switch_profile(self, profile_name='default'):
        profiles = self.load_profiles()
        if profile_name not in profiles:
            print(f"Профиль '{profile_name}' не найден. Доступные: {', '.join(profiles.keys())}")
            return False
        
        # Сохраняем текущий профиль и переключаемся
        current = profiles.pop('current')
        profiles['current'] = profile_name
        self.save_profiles(profiles)
        
        if profile_name == 'default':
            print(f"Переключено на: {profiles['default']['name']}")
        else:
            print(f"Переключено на профиль: {profile_name}")
        return True
    
    def get_current_profile(self):
        profiles = self.load_profiles()
        current = profiles.get('current', 'default')
        profile_data = profiles[current] if current != 'default' else profiles['default']
        return profile_data

# Инициализация менеджера профилей при запуске приложения
profile_mgr = ProfileManager()
