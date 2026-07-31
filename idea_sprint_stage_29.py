# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: IdeaSprint
# IdeaSprint - Step 29: Configuration via Settings Dictionary
# Add this block at the end of your file, before any main execution or interactive loop.

def load_settings():
    """Load application settings from a dictionary-like structure."""
    settings = {
        "app_name": "IdeaSprint",
        "version": "1.0",
        "max_ideas_per_session": 50,
        "default_priority": "medium",
        "priority_levels": ["low", "medium", "high", "urgent"],
        "output_format": "console",
        "color_enabled": True,
        "log_level": "INFO",
    }
    return settings

if __name__ == "__main__":
    print(load_settings())
