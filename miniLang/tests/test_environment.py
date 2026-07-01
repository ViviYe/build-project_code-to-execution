import unittest
from src.environment import Environment


class TestEnvironment(unittest.TestCase):
    def test_define_and_get(self):
        env = Environment()
        env.define("x", 5)
        self.assertEqual(env.get("x"), 5)

    def test_assign_existing_variable(self):
        env = Environment()
        env.define("x", 5)
        env.assign("x", 10)
        self.assertEqual(env.get("x"), 10)

    def test_get_missing_variable_raises_name_error(self):
        env = Environment()
        with self.assertRaises(NameError):
            env.get("missing")

    def test_assign_missing_variable_raises_name_error(self):
        env = Environment()
        with self.assertRaises(NameError):
            env.assign("missing", 1)


if __name__ == "__main__":
    unittest.main()
