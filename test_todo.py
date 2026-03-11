import unittest
from todo import Task, add_task, format_task


class TestTask(unittest.TestCase):
    def test_default_creation(self):
        task = Task(name="장보기")
        self.assertEqual(task.name, "장보기")
        self.assertFalse(task.done)
        self.assertIsInstance(task.created_at, str)
        self.assertTrue(len(task.created_at) > 0)

    def test_done_true(self):
        task = Task(name="장보기", done=True)
        self.assertTrue(task.done)


class TestAddTask(unittest.TestCase):
    def test_add_to_empty_list(self):
        tasks = []
        result = add_task(tasks, "장보기")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "장보기")

    def test_add_multiple(self):
        tasks = []
        add_task(tasks, "장보기")
        add_task(tasks, "운동하기")
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].name, "장보기")
        self.assertEqual(tasks[1].name, "운동하기")

    def test_returns_same_list(self):
        tasks = []
        result = add_task(tasks, "장보기")
        self.assertIs(result, tasks)


class TestFormatTask(unittest.TestCase):
    def test_undone_task(self):
        task = Task(name="장보기", done=False, created_at="2026-01-01 00:00:00")
        result = format_task(1, task)
        self.assertIn("[ ]", result)

    def test_done_task(self):
        task = Task(name="장보기", done=True, created_at="2026-01-01 00:00:00")
        result = format_task(1, task)
        self.assertIn("[x]", result)

    def test_index_in_output(self):
        task = Task(name="장보기", done=False, created_at="2026-01-01 00:00:00")
        result = format_task(3, task)
        self.assertTrue(result.startswith("3."))

    def test_created_at_in_output(self):
        task = Task(name="장보기", done=False, created_at="2026-01-01 00:00:00")
        result = format_task(1, task)
        self.assertIn("2026-01-01 00:00:00", result)


if __name__ == "__main__":
    unittest.main()
