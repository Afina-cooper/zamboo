# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: IdeaSprint
import unittest

class TestIdeaSprint(unittest.TestCase):

    def test_add_idea(self):
        from IdeaSprint import IdeaSprint
        app = IdeaSprint()
        app.add_idea("Тестовая идея", "1", "1", "1", "1")
        self.assertEqual(len(app.ideas), 1)
        self.assertEqual(app.ideas[0]['title'], "Тестовая идея")

    def test_add_task(self):
        from IdeaSprint import IdeaSprint
        app = IdeaSprint()
        app.add_task("Задача 1", "1", "1", "1", "1")
        self.assertEqual(len(app.tasks), 1)
        self.assertEqual(app.tasks[0]['title'], "Задача 1")

    def test_add_hypothesis(self):
        from IdeaSprint import IdeaSprint
        app = IdeaSprint()
        app.add_hypothesis("Гипотеза 1", "1", "1", "1", "1")
        self.assertEqual(len(app.hypotheses), 1)
        self.assertEqual(app.hypotheses[0]['title'], "Гипотеза 1")

    def test_add_result(self):
        from IdeaSprint import IdeaSprint
        app = IdeaSprint()
        app.add_result("Результат 1", "1", "1", "1", "1")
        self.assertEqual(len(app.results), 1)
        self.assertEqual(app.results[0]['title'], "Результат 1")

    def test_add_goal(self):
        from IdeaSprint import IdeaSprint
        app = IdeaSprint()
        app.add_goal("Цель 1", "1", "1", "1", "1")
        self.assertEqual(len(app.goals), 1)
        self.assertEqual(app.goals[0]['title'], "Цель 1")

if __name__ == '__main__':
    unittest.main()
