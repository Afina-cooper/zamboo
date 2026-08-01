# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: IdeaSprint
class Profile:
    def __init__(self, name, role="idea", avatar_emoji="🧠"):
        self.name = name
        self.role = role
        self.avatar_emoji = avatar_emoji
        self.created_at = datetime.datetime.now(datetime.timezone.utc)

    def to_dict(self):
        return {"name": self.name, "role": self.role, "avatar_emoji": self.avatar_emoji}

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class ProfileManager:
    _profiles = {}

    @staticmethod
    def add(name, role="idea", avatar_emoji="🧠"):
        if name in ProfileManager._profiles:
            raise ValueError(f"Profile '{name}' already exists")
        p = Profile(name, role, avatar_emoji)
        ProfileManager._profiles[name] = p
        return p

    @staticmethod
    def get(name):
        return ProfileManager._profiles.get(name)

    @staticmethod
    def remove(name):
        return ProfileManager._profiles.pop(name, None)

    @staticmethod
    def list():
        return [p.to_dict() for p in sorted(ProfileManager._profiles.values(), key=lambda x: x.name)]

    @staticmethod
    def load_from_file(filepath="profiles.json"):
        import json
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                ProfileManager._profiles[item["name"]] = Profile.from_dict(item)

    @staticmethod
    def save_to_file(filepath="profiles.json"):
        import json
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in ProfileManager._profiles.values()], f, ensure_ascii=False, indent=2)

def load_profiles():
    try:
        ProfileManager.load_from_file("profiles.json")
        return ProfileManager.list()
    except Exception:
        return []
