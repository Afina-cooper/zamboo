# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: IdeaSprint
def get_next_action(user_id, current_state):
    """
    Рекомендация следующего действия на основе текущего состояния проекта.
    """
    user_actions = current_state.get("user_actions", [])
    if not user_actions:
        return "Заполните данные о себе (имя, возраст, интересы)."

    last_action = user_actions[-1]
    if last_action.get("type") == "self_introduction":
        return "Перейдите к разделу 'Список идей'. Нажмите 'Создать новую идею'."
    elif last_action.get("type") == "create_idea":
        return "Заполните поля: название, описание, категория. Затем нажмите 'Сохранить'."
    elif last_action.get("type") == "save_idea":
        return "Перейдите в 'Список идей'. Выберите идею для оценки. Укажите оценку 1-5 и нажмите 'Сохранить оценку'."
    elif last_action.get("type") == "save_evaluation":
        return "Выберите идею из списка и нажмите 'Удалить' для удаления из проекта."
    elif last_action.get("type") == "delete_idea":
        return "Заполните поля новой идеи и нажмите 'Сохранить'."
    elif last_action.get("type") == "create_task":
        return "Заполните поля: название, описание, оценка, результат. Нажмите 'Сохранить'."
    elif last_action.get("type") == "save_task":
        return "Перейдите в 'Список задач'. Выберите задачу для удаления. Нажмите 'Удалить'."
    elif last_action.get("type") == "delete_task":
        return "Нажмите 'Назад' в верхней части экрана."
    elif last_action.get("type") == "back":
        return "Выберите действие из навигации: создать идею, задачу, или вернуться к списку."
    elif last_action.get("type") == "create_hypothesis":
        return "Заполните поля: название, описание, оценка. Нажмите 'Сохранить'."
    elif last_action.get("type") == "save_hypothesis":
        return "Перейдите в 'Список гипотез'. Выберите гипотезу для удаления. Нажмите 'Удалить'."
    elif last_action.get("type") == "delete_hypothesis":
        return "Нажмите 'Назад' или выберите другое действие из навигации."
    elif last_action.get("type") == "back":
        return "Выберите действие из навигации: создать гипотезу, идею, задачу."
    else:
        return "Выберите действие: создать идею, задачу, гипотезу или вернуться назад."
