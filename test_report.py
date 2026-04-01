import unittest
from generate_report import get_priority_weight

class TestBugReport(unittest.TestCase):
    """Pruebas unitarias para validar la logica de negocio del generador."""

    def test_priority_logic(self):
        """Valida que 'critical' sea mas importante que 'low'."""
        bug_critico = {'severity': 'critical'}
        bug_bajo = {'severity': 'low'}
        
        self.assertEqual(get_priority_weight(bug_critico), 1)
        self.assertEqual(get_priority_weight(bug_bajo), 4)

    def test_default_priority(self):
        """Valida que si no hay datos, se asigne prioridad 4 (low)."""
        bug_vacio = {}
        self.assertEqual(get_priority_weight(bug_vacio), 4)

if __name__ == '__main__':
    unittest.main()