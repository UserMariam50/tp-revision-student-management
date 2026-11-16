
import unittest
from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades
)
class TestStudentManager(unittest.TestCase):

    # 1. Calcul de moyenne
    def test_calculate_average(self):
        self.assertEqual(calculate_average([12, 15, 18]), 15)

    # 2. Calcul avec notes identiques
    def test_calculate_average_identical(self):
        self.assertEqual(calculate_average([10, 10, 10]), 10)

    # 3. Liste vide : ValueError
    def test_calculate_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    # 4. Mention Échec
    def test_mention_echec(self):
        self.assertEqual(get_mention(8), "Échec")

    # 5. Mention Bien
    def test_mention_bien(self):
        self.assertEqual(get_mention(15), "Bien")

    # 6. Mention Excellent
    def test_mention_excellent(self):
        self.assertEqual(get_mention(18), "Excellent")

    # 7. Étudiant admis
    def test_admitted(self):
        self.assertTrue(is_admitted(12))

    # 8. Étudiant non admis
    def test_not_admitted(self):
        self.assertFalse(is_admitted(9))

    # 9. Notes valides
    def test_valid_grades(self):
        self.assertTrue(validate_grades([12, 15, 18]))

    # 10. Liste vide invalide
    def test_empty_grades(self):
        self.assertFalse(validate_grades([]))

    # 11. Note supérieure à 20
    def test_grade_above_20(self):
        self.assertFalse(validate_grades([12, 25, 18]))

    # 12. Note négative
    def test_negative_grade(self):
        self.assertFalse(validate_grades([-2, 12, 15]))

    def test_admitted_average_10(self):
        self.assertTrue(is_admitted(10))

if __name__ == "__main__":
    unittest.main()
