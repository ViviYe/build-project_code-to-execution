import unittest
from src.custom_language import CustomLanguage
class TestRegression(unittest.TestCase):
 def test_old_features(self):
  l=CustomLanguage(); self.assertEqual(l.run('1+2*3'),7); l.run('x=0'); l.run('while x<3: x=x+1'); self.assertEqual(l.run('x'),3)
