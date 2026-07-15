import unittest
from src.environment import Environment
class TestEnvironmentScope(unittest.TestCase):
 def test_parent_lookup(self):
  p=Environment(); p.define('x',100); c=Environment(parent=p); self.assertEqual(c.get('x'),100)
 def test_shadowing(self):
  p=Environment(); p.define('x',100); c=Environment(parent=p); c.define('x',5); self.assertEqual(c.get('x'),5); self.assertEqual(p.get('x'),100)
 def test_missing(self):
  with self.assertRaises(NameError): Environment(parent=Environment()).get('missing')
