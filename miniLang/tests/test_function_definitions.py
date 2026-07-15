import unittest
from src.custom_language import CustomLanguage
class TestDefinitions(unittest.TestCase):
 def test_registers_without_running(self):
  l=CustomLanguage(); self.assertIsNone(l.run('def delayed(): missing')); self.assertIn('delayed',l.env.functions)
