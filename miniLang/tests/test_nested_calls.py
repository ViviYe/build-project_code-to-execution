import unittest
from src.custom_language import CustomLanguage
class TestNested(unittest.TestCase):
 def test_nested(self):
  l=CustomLanguage(); l.run('def square(x): x*x'); l.run('def double(x): x*2'); self.assertEqual(l.run('double(square(5))'),50)
 def test_fresh_scope(self):
  l=CustomLanguage(); l.run('def square(x): x*x'); self.assertEqual(l.run('square(5)'),25); self.assertEqual(l.run('square(10)'),100)
