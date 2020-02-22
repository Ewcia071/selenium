#Import bibliotek
from selenium import webdriver
from time import sleep
import unittest

#Tworzymy klase WsbPlCheck dziedziczaca po TestCase
#z modulu unittest
class WsbPlCheck(unittest.TestCase):
    """
    Analogia: Scenariusz testowy
    """
#warunki wstepne
#(przygotowanie testu)
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
#wlasciciwe tetsy
    def testWsb(self):
        driver=self.driver
        driver.get("http://www.google.pl")
        self.assertIn("Bankowe",driver.title)
#sprzatanie po testach
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
