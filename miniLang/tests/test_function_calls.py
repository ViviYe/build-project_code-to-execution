import unittest
from src.custom_language import CustomLanguage
class TestCalls(unittest.TestCase):
 def test_square(self):
  l=CustomLanguage(); l.run('def square(x): x * x'); self.assertEqual(l.run('square(5)'),25)
 def test_area(self):
  l=CustomLanguage(); l.run('def area(w, h): w * h'); self.assertEqual(l.run('area(4, 5)'),20)
 def test_parent_lookup(self):
  l=CustomLanguage(); l.run('multiplier = 10'); l.run('def scale(x): x * multiplier'); self.assertEqual(l.run('scale(7)'),70)
 def test_global_not_overwritten(self):
  l=CustomLanguage(); l.run('x = 100'); l.run('def square(x): x * x'); self.assertEqual(l.run('square(5)'),25); self.assertEqual(l.run('x'),100)
 def test_arity(self):
  l=CustomLanguage(); l.run('def square(x): x * x')
  with self.assertRaises(TypeError): l.run('square(1,2)')
 def test_unknown_function(self):
  with self.assertRaises(NameError): CustomLanguage().run('missing(5)')
