
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStudentApp(unittest.TestCase):

    # Ouvrir Chrome une seule fois
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 5)

    # Ouvrir la page avant chaque test
    def setUp(self):
        self.driver.get("http://127.0.0.1:5000")

    # Fonction pour saisir les notes et cliquer
    def calculate(self, notes):

        field = self.driver.find_element(By.ID, "grades")
        field.clear()
        field.send_keys(notes)

        button = self.driver.find_element(By.ID, "calculate")
        button.click()

    # Test 1 : moyenne = 15
    def test_average_15(self):
        self.calculate("12,15,18")

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "average"))
        )

        self.assertEqual(result.text, "15.00")

    # Test 2 : moyenne = 10
    def test_average_10(self):
        self.calculate("10,10,10")

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "average"))
        )

        self.assertEqual(result.text, "10.00")

    # Test 3 : mention Échec
    def test_mention_echec(self):
        self.calculate("8,8,8")

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "mention"))
        )

        self.assertEqual(result.text, "Échec")

    # Test 4 : mention Excellent
    def test_mention_excellent(self):
        self.calculate("18,18,18")

        result = self.wait.until(
            EC.visibility_of_element_located((By.ID, "mention"))
        )

        self.assertEqual(result.text, "Excellent")

    # Test 5 : notes invalides
    def test_invalid_grades(self):
        self.calculate("12,25,18")

        error = self.wait.until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        self.assertTrue(error.is_displayed())

    # Test 6 : champ vide
    def test_empty_grades(self):
        self.calculate("")

        error = self.wait.until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        self.assertTrue(error.is_displayed())

    # Fermer Chrome après tous les tests
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
